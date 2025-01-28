from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot, QSettings, QByteArray, QTimer
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtSerialPort import QSerialPort

from style.style import globalStyle

from modules.tempsettings import TempSettings
from modules.backend.projects import getProjects

import importlib
import os

from ui.widgets.leftmenu import LeftMenu
from ui.widgets.simulation import AreaSimulation

import resources.resources

# Creating the central widget
class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__()
        # Setting the widget options
        self.setObjectName("CentralWidget")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.useHardware = False

        self.settings = QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
        self.isDarkMode = self.settings.value("darkMode",defaultValue=TempSettings.get("isDarkModeSystem"), type=bool)

        self.setStyleSheet(globalStyle(self.isDarkMode))

        # Timer for simulation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.writeSerial)

        # Layout
        self.Layout = QtWidgets.QHBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(0)

        self.setLayout(self.Layout)

        # Left Menu
        self.LeftMenu = LeftMenu(self)
        self.LeftMenu.toggleDarkMode.connect(self.toggleTheme)

        # List of projects
        self.listProjects = getProjects()

        for project in self.listProjects:
            self.LeftMenu.selectSimulation.addItem(project)

        self.LeftMenu.selectSimulation.currentTextChanged.connect(self.toggleProject)

        self.LeftMenu.btnOpenSimulation.clicked.connect(self.openProject)

        # Serial
        self.LeftMenu.selectDevice.currentIndexChanged.connect(self.connectSerial)
        self.LeftMenu.closeSerial.connect(self.closeSerial)

        # Simulation controls
        self.LeftMenu.btnPlay.clicked.connect(self.startSimulation)
        self.LeftMenu.btnStop.clicked.connect(self.stopSimulation)

        # Area Simulation
        self.AreaSimulation = AreaSimulation(self)

        # Adding widgets to the layout
        self.Layout.addWidget(self.LeftMenu)
        self.Layout.addWidget(self.AreaSimulation)

        # Serial Manager
        self.serialPort = QSerialPort(parent=self)
        self.serialPort.readyRead.connect(self.readSerial)

    @Slot(bool)
    def toggleTheme(self, isDarkMode:bool):
        self.isDarkMode = isDarkMode
        self.setStyleSheet(globalStyle(isDarkMode))

    @Slot(str)
    def toggleProject(self, project:str):
        if os.path.isabs(project):
            pathProject = project
        else:
            pathProject = os.path.join(TempSettings.get("folderProjects"), f"{project}.py")

        try:
            spec = importlib.util.spec_from_file_location(project, pathProject)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            self.AreaSimulation.layoutScrollAreaWidget.removeWidget(self.AreaSimulation.projeto)
            self.AreaSimulation.projeto.deleteLater()

            self.AreaSimulation.projeto = modulo.Projeto()
            self.AreaSimulation.layoutScrollAreaWidget.addWidget(self.AreaSimulation.projeto)

        except:
            print("Erro ao carregar o projeto")
            pass

    @Slot()
    def openProject(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir Projeto", "", "Arquivos Python (*.py)")
        
        if file:
            self.toggleProject(file)
            self.LeftMenu.selectSimulation.setCurrentIndex(-1)


    @Slot(int)
    def connectSerial(self, index:int):
        if self.serialPort.isOpen():
            self.serialPort.close()
            
        if index >= 0:
            port = TempSettings.get("devices")[index][0]

            TempSettings.set("currentDevice", port)

            self.serialPort.setPortName(port)
            self.serialPort.setBaudRate(QSerialPort.Baud115200)

            # self.serialPort.setDataBits(QSerialPort.Data8)
            # self.serialPort.setParity(QSerialPort.NoParity)
            # self.serialPort.setStopBits(QSerialPort.OneStop)
            # self.serialPort.setFlowControl(QSerialPort.NoFlowControl)

            messageBox = QtWidgets.QMessageBox()

            if self.serialPort.open(QSerialPort.ReadWrite):
                messageBox.setWindowTitle(f"Conectado a {port}")
                messageBox.setIcon(QtWidgets.QMessageBox.Information)
                messageBox.setText("Conexão estabelecida com sucesso.")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

                messageBox.exec()
            else:
                self.LeftMenu.updateDevices(True)
                messageBox.setWindowTitle("Não foi possível conectar")
                messageBox.setIcon(QtWidgets.QMessageBox.Critical)
                messageBox.setText("Não foi possível conectar ao dispositivo.")
                messageBox.setInformativeText("Verifique o dispositivo e tente novamente.")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

                messageBox.exec()

    @Slot()
    def closeSerial(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle(f"Desconectado de {TempSettings.get('currentDevice')}")
            messageBox.setIcon(QtWidgets.QMessageBox.Warning)
            messageBox.setText("Conexão encerrada, escolha um dispositivo para conectar.")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

            messageBox.exec()

    @Slot()
    def readSerial(self):
        if self.useHardware:
            try:
                data = self.serialPort.readAll().data().decode().strip()
            except:
                data = ""

            data = list(data)

            self.AreaSimulation.receiveData(data)

    @Slot()
    def writeSerial(self):
        values = self.AreaSimulation.projeto.getValues()
        data = "".join(values)
        print(data)
        data = QByteArray(data.encode())

        if not self.useHardware:
            self.AreaSimulation.receiveData([])
        elif self.serialPort.isOpen():
            self.serialPort.write(data)
        else:
            self.timer.stop()
            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle("Conexão interrompida")
            messageBox.setIcon(QtWidgets.QMessageBox.Critical)
            messageBox.setText("Verifique o dispositivo e tente novamente.")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

            messageBox.exec()

    @Slot()
    def startSimulation(self):
        self.useHardware = self.AreaSimulation.projeto.useHardware

        if not self.useHardware or self.serialPort.isOpen():
            print("Simulation started")
            self.LeftMenu.selectSimulation.setDisabled(True)
            self.LeftMenu.btnOpenSimulation.setDisabled(True)
            self.LeftMenu.selectDevice.setDisabled(True)
            self.LeftMenu.btnUpdateDevices.setDisabled(True)
            self.LeftMenu.btnPlay.setDisabled(True)
            self.LeftMenu.btnStop.setDisabled(False)
            self.timer.start(30)
        else:
            self.timer.stop()
            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle("Nenhum dispositivo conectado")
            messageBox.setIcon(QtWidgets.QMessageBox.Critical)
            messageBox.setText("Selecione um dispositivo e tente novamente.")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

            messageBox.exec()

    @Slot()
    def stopSimulation(self):
        self.timer.stop()
        
        if self.LeftMenu.selectDevice.count() > 0:
            self.LeftMenu.selectDevice.setDisabled(False)
        
        
        self.LeftMenu.selectSimulation.setDisabled(False)
        self.LeftMenu.btnOpenSimulation.setDisabled(False)
        self.LeftMenu.btnPlay.setDisabled(False)
        self.LeftMenu.btnStop.setDisabled(True)

        self.LeftMenu.btnUpdateDevices.setDisabled(False)
        self.AreaSimulation.projeto.resetSimulation()

# Creating the main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Defining window parameters
        self.setWindowTitle("Simulador Circuitos Digitais")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))

        self.central = CentralWidget(self)
        self.setCentralWidget(self.central)

    @Slot(QCloseEvent)
    def closeEvent(self, event:QCloseEvent):
        QtWidgets.QApplication.quit()
        super().closeEvent(event)
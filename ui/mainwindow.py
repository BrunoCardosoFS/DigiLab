from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot, QSettings, QByteArray, QTimer
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtSerialPort import QSerialPort

from style.style import globalStyle

from modules.tempsettings import TempSettings

from ui.widgets.leftmenu import LeftMenu
from ui.widgets.simulation import AreaSimulation

import resources.resources

# Creating the central widget
class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__()
    
        self.setObjectName("CentralWidget")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.writeSerial)

        self.settings = QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
        self.isDarkMode = self.settings.value("darkMode",defaultValue=TempSettings.get("isDarkModeSystem"), type=bool)

        self.setStyleSheet(globalStyle(self.isDarkMode))

        self.Layout = QtWidgets.QHBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(0)

        self.setLayout(self.Layout)

        self.LeftMenu = LeftMenu(self)
        self.LeftMenu.toggleDarkMode.connect(self.toggleTheme)

        self.LeftMenu.selectDevice.currentIndexChanged.connect(self.connectSerial)
        self.LeftMenu.closeSerial.connect(self.closeSerial)

        self.LeftMenu.btnPlay.clicked.connect(self.startSimulation)
        self.LeftMenu.btnStop.clicked.connect(self.stopSimulation)

        self.AreaSimulation = AreaSimulation(self)

        self.Layout.addWidget(self.LeftMenu)
        self.Layout.addWidget(self.AreaSimulation)

        # Serial Manager
        self.serialPort = QSerialPort(parent=self)

        self.serialPort.readyRead.connect(self.readSerial)

    @Slot(bool)
    def toggleTheme(self, isDarkMode:bool):
        self.isDarkMode = isDarkMode
        self.setStyleSheet(globalStyle(isDarkMode))

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
        try:
            data = self.serialPort.readAll().data().decode().strip()
        except UnicodeDecodeError:
            data = ""

        data = list(data)

        self.AreaSimulation.receiveData(data)

    @Slot()
    def writeSerial(self):
        values = self.AreaSimulation.projeto.getValues()
        data = "".join(values)
        print(data)
        data = QByteArray(data.encode())

        if self.serialPort.isOpen():
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
        if self.serialPort.isOpen():
            self.timer.start(30)
            self.LeftMenu.selectDevice.setDisabled(True)
            self.LeftMenu.btnUpdateDevices.setDisabled(True)
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
        self.LeftMenu.selectDevice.setDisabled(False)
        self.LeftMenu.btnUpdateDevices.setDisabled(False)
        self.AreaSimulation.projeto.resetSimulation()
        
        self.timer.stop()

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
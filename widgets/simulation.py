from PySide6 import QtWidgets, QtCore, QtSerialPort
from widgets.simulationObjects import Valvula, Tanque

from functions.serial import SerialManager

class SimulationScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent: None):
        super().__init__()
        self.serialReceived = ["0", "0", "0", "0", "0", "0"]

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.simulation)

        self.serialManager = SerialManager()
        self.serialManager.setPortName("COM3")
        self.serialManager.setBaudRate(QtSerialPort.QSerialPort.Baud115200)
        self.serialManager.data_received.connect(self.updateData)

        self.connect()

        self.valvulaIn = Valvula(self, -36.5, 5, True, 1)
        self.valvulaOut = Valvula(self, 202.8, 286.5, True, 2)

        self.tanque = Tanque(self, self.valvulaIn, self.valvulaOut, [{"y": 30}, {"y": 50}, {"y": 70}])

        self.addItem(self.tanque)
        self.addItem(self.valvulaIn)
        self.addItem(self.valvulaOut)

    @QtCore.Slot()
    def simulation(self):
        self.sensors = self.tanque.sensors
        self.dataSensors = ""

        for sensor in self.sensors:
            self.dataSensors = self.dataSensors + str(int(sensor.isWater))
        
        self.dataSensors = self.dataSensors + str(int(self.tanque.valveOut.isOpen)) + "00"

        self.tanque.valveIn.controlOpenValv(int(self.serialReceived[0]))

        print(self.dataSensors + "; " + self.serialReceived[0])

        self.dataToSend = QtCore.QByteArray(self.dataSensors.encode())

        self.serialManager.write(self.dataToSend)




        self.tanque.changeWater()

    def startSimulation(self):
        self.timer.start(25)

    def stopSimulation(self):
        self.timer.stop()
        # self.agua.setPos(0, 0)
        # self.agua.setRect(self.agua.rect().x(), self.agua.rect().y(), self.agua.rect().width(), 0)

    # Controles temporários da comunicação serial
    def connect(self):
        print("Conectando...")
        if self.serialManager.open(QtCore.QIODevice.ReadWrite):
            print("Conectado")
        else:
            print("Não foi possível conectar")
    
    def disconnect(self):
        print("Desconectando...")
        if not self.serialManager.close():
            print("Desconectado")
        else:
            print("Não foi possível desconectar")

    def updateData(self, data):
        self.serialReceived = list(data)
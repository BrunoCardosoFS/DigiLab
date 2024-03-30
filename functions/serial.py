import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtSerialPort

current_path = sys.argv[0].replace("main.py", "")

import resources.resources

def listCOM():
    ports = QtSerialPort.QSerialPortInfo.availablePorts()
    listPorts = []
    if ports:
        for port in ports:
            listPorts.append({"name": port.portName(), "description": port.description()})
    else:
        listPorts = None

    return listPorts

class SerialManager(QtSerialPort.QSerialPort):
    data_received = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.readyRead.connect(self.read_data)

    @QtCore.Slot()
    def read_data(self):
        data = self.readAll().data().decode().strip()
        self.data_received.emit(data)
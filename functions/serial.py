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
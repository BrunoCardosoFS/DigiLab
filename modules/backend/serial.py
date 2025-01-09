from PySide6 import QtSerialPort

def listPorts():
    ports = QtSerialPort.QSerialPortInfo.availablePorts()
    listPorts = []
    if ports:
        for port in ports:
            # 0 - Port name
            # 1 - Description
            listPorts.append([port.portName(), port.description()])

    return listPorts

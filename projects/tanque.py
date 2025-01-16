from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Signal
from PySide6.QtCore import Qt

import os

class Valvula(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget = None, valvin: bool = False, valvout: bool = False):
        super().__init__(parent)

        self.styles = f"""
        Valvula #cano{{
            border-top-width: 3px;
            border-left-width: 0px;
            border-bottom-width: 3px;
            border-color: #000;
            border-style: solid;
            {"border-right: 5px solid #fff;" if valvin else ""}
            {"border-left: 5px solid #fff;" if valvout else ""}
        }}

        Valvula #valvula{{
            background: #000;
        }}
        """

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.styles)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setFixedSize(50, 40)

        self.value = 0.0

        self.cano = QtWidgets.QFrame(self)
        self.cano.setObjectName("cano")
        self.cano.setFixedSize(50, 20)
        self.cano.move(0, 20)

        self.valvula = QtWidgets.QFrame(self)
        self.valvula.setObjectName("valvula")
        self.valvula.setFixedSize(3, 25)
        self.valvula.move(23, 13)

    @Slot(float)
    def setValue(self, value: float):
        if value >= 0 and value <= 1:
            self.value = value
            self.valvula.move(23, int(13*(1-value)))

class Sensor(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget = None, x: int = 0, y: int = 0):
        super().__init__(parent)
        self.position = (x, y)
        self.value = 0
        self.setStyleSheet("background: red;")
        self.setFixedSize(15, 7)
        self.move(x, y)

    @Slot(int)
    def setValue(self, value: int):
        self.value = value
        self.setStyleSheet("background: #0f0;" if value else "background: #f00;")


class Tanque(QtWidgets.QFrame):
    def __init__(self, parent: QtWidgets.QWidget = None, ):
        super().__init__(parent)
        self.styles = """
            Tanque{
                background-color: rgba(0,0,0,0.0);
            }
            
            Tanque QPushButton{
                padding: 5px 7px;
            }
            
            Tanque QPushButton#buttonUp{
                qproperty-icon: url(:/images/light/arrow-up.svg);
            }
            
            Tanque QPushButton#buttonDown{
                qproperty-icon: url(:/images/light/arrow-down.svg);
            }
            
            Tanque #agua{
                background: blue;
            }

            Tanque #tanque{
                border-top-width: 0px;
                border-left-width: 3px;
                border-bottom-width: 3px;
                border-right-width: 3px;
                border-color: #000;
                border-style: solid;
            }
            
            #sensor1, #sensor2, #sensor3{
                background: red;
            }
        """

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.styles)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setFixedSize(365, 380)

        self.nivelAgua = 0

        self.agua = QtWidgets.QFrame(self)
        self.agua.setObjectName("agua")
        self.agua.setFixedSize(246, self.nivelAgua)
        self.agua.move(48, (348 - self.nivelAgua))

        self.sensor1 = Sensor(self, x=48, y=300)
        self.sensor2 = Sensor(self, x=48, y=200)
        self.sensor3 = Sensor(self, x=48, y=100)

        self.tanque = QtWidgets.QFrame(self)
        self.tanque.setObjectName("tanque")
        self.tanque.setFixedSize(250, 350)
        self.tanque.move(46, 0)

        self.valvIn = Valvula(self, valvin=True)
        self.valvIn.move(0, 0)

        self.valvOut = Valvula(self, valvout=True)
        self.valvOut.move(292, 305)

        self.buttonUp = QtWidgets.QPushButton(parent=self, text="")
        self.buttonUp.setObjectName("buttonUp")
        self.buttonUp.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonUp.move(325, 293)
        self.buttonUp.clicked.connect(lambda: self.valvOut.setValue((self.valvOut.value + 0.25) if (self.valvOut.value < 1.0) else 1.0))

        self.buttonDown = QtWidgets.QPushButton(parent=self, text="")
        self.buttonDown.setObjectName("buttonDown")
        self.buttonDown.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonDown.move(325, 350)
        self.buttonDown.clicked.connect(lambda: self.valvOut.setValue((self.valvOut.value - 0.25) if self.valvOut.value > 0.0 else 0.0))

    @Slot()
    def updateNivelAgua(self):
        nivelAgua = self.nivelAgua + self.valvIn.value - (2 * self.valvOut.value)

        maxAgua = 328

        if nivelAgua>=0 and nivelAgua <= maxAgua:
            self.nivelAgua = nivelAgua
            self.agua.setFixedHeight(self.nivelAgua)
            self.agua.move(48, (348 - self.nivelAgua))
        elif nivelAgua >=0 and nivelAgua > maxAgua and self.nivelAgua != maxAgua:
            self.nivelAgua = maxAgua
            self.agua.setFixedHeight(maxAgua)
            self.agua.move(48, 20)

        if (341-self.nivelAgua) <= self.sensor1.position[1]:
            self.sensor1.setValue(1)
        else:
            self.sensor1.setValue(0)
        
        if (341-self.nivelAgua) <= self.sensor2.position[1]:
            self.sensor2.setValue(1)
        else:
            self.sensor2.setValue(0)
        
        if (341-self.nivelAgua) <= self.sensor3.position[1]:
            self.sensor3.setValue(1)
        else:
            self.sensor3.setValue(0)

    @Slot()
    def resetTanque(self):
        self.sensor1.setValue(0)
        self.sensor2.setValue(0)
        self.sensor3.setValue(0)

        self.nivelAgua = 0
        self.agua.setFixedHeight(self.nivelAgua)
        self.agua.move(48, 348)



class Projeto(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.tanque = Tanque(self)

        self.Layout.addWidget(self.tanque)

    @Slot()
    def resetSimulation(self):
        self.tanque.resetTanque()

    @Slot(list)
    def updateSimulation(self, data: list):
        if data[0] == "1" and self.tanque.valvIn != 0:
            self.tanque.valvIn.setValue(1)
        elif  self.tanque.valvIn != 1:
            self.tanque.valvIn.setValue(0)

        self.tanque.updateNivelAgua()

    @Slot()
    def getValues(self):
        self.values[0] = str(self.tanque.sensor1.value)
        self.values[1] = str(self.tanque.sensor2.value)
        self.values[2] = str(self.tanque.sensor3.value)

        return self.values
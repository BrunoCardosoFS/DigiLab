from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt

import os

class Valvula(QtWidgets.QWidget):
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

        self.cano = QtWidgets.QFrame(self)
        self.cano.setObjectName("cano")
        self.cano.setFixedSize(50, 20)
        self.cano.move(0, 20)

        self.valvula = QtWidgets.QFrame(self)
        self.valvula.setObjectName("valvula")
        self.valvula.setFixedSize(3, 25)
        self.valvula.move(23, 15)


class Projeto(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.styles = """
            Projeto{
                background-color: rgba(0,0,0,0.05);
            }
            
            Projeto QPushButton{
                padding: 5px 7px;
            }
            
            Projeto QPushButton#buttonUp{
                qproperty-icon: url(:/images/light/arrow-up.svg);
            }
            
            Projeto QPushButton#buttonDown{
                qproperty-icon: url(:/images/light/arrow-down.svg);
            }
            
            Projeto #agua{
                background: blue;
            }

            Projeto #tanque{
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

        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.nivelAgua = 0
        self.agua = QtWidgets.QWidget(self)
        self.agua.setObjectName("agua")
        self.agua.setFixedSize(246, self.nivelAgua)
        self.agua.move(48, (348 - self.nivelAgua))

        self.sensor1 = QtWidgets.QFrame(parent=self)
        self.sensor1.setObjectName("sensor1")
        self.sensor1.setFixedSize(15, 7)
        self.sensor1.move(48, 300)

        self.sensor2 = QtWidgets.QFrame(parent=self)
        self.sensor2.setObjectName("sensor2")
        self.sensor2.setFixedSize(15, 7)
        self.sensor2.move(48, 200)

        self.sensor3 = QtWidgets.QFrame(parent=self)
        self.sensor3.setObjectName("sensor3")
        self.sensor3.setFixedSize(15, 7)
        self.sensor3.move(48, 100)

        self.tanque = QtWidgets.QWidget(self)
        self.tanque.setObjectName("tanque")
        self.tanque.setFixedSize(250, 350)
        self.tanque.move(46, 0)

        self.valv1 = Valvula(self, valvin=True)
        self.valv1.setObjectName("valv1")
        self.valv1.move(0, 0)

        self.valv2 = Valvula(self, valvout=True)
        self.valv2.setObjectName("valv2")
        self.valv2.move(293, 305)

        self.buttonUp = QtWidgets.QPushButton(parent=self, text="")
        self.buttonUp.setObjectName("buttonUp")
        self.buttonUp.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonUp.move(325, 293)

        self.buttonDown = QtWidgets.QPushButton(parent=self, text="")
        self.buttonDown.setObjectName("buttonDown")
        self.buttonDown.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonDown.move(325, 350)

    @Slot(list)
    def updateSimulation(self, data: list):
        if data[0] == "1":
            vazEntrada = 1
        else:
            vazEntrada = 0

        nivelAgua = self.nivelAgua + vazEntrada

        maxAgua = 328

        if nivelAgua <= maxAgua:
            self.nivelAgua = nivelAgua
            self.agua.setFixedHeight(self.nivelAgua)
            self.agua.move(48, (348 - self.nivelAgua))
        elif nivelAgua > maxAgua and self.nivelAgua != maxAgua:
            self.nivelAgua = maxAgua
            self.agua.setFixedHeight(maxAgua)
            self.agua.move(48, 0)

        print(data)

    def getValues(self):
        return self.values
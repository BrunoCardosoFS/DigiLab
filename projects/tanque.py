from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt

import os

class Valvula(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None, valvin: bool = False, valvout: bool = False):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet(f"""
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
        """)

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setFixedSize(50, 40)

        self.cano = QtWidgets.QWidget(self)
        self.cano.setObjectName("cano")
        self.cano.setFixedSize(50, 20)
        self.cano.move(0, 20)

        self.valvula = QtWidgets.QWidget(self)
        self.valvula.setAttribute(Qt.WA_StyledBackground, True)
        self.valvula.setObjectName("valvula")
        self.valvula.setFixedSize(3, 25)
        self.valvula.move(23, 15)





class Projeto(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
                            Projeto{
                                background-color: rgba(0,0,0,0.05);
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
        """)

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setFixedSize(500, 400)

        self.nivelAgua = 0
        self.agua = QtWidgets.QWidget(self)
        self.agua.setObjectName("agua")
        self.agua.setFixedSize(246, self.nivelAgua)
        self.agua.move(48, (348 - self.nivelAgua))

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
        return [0,0,0,0,0,0,0,0,0,0]
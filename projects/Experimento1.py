from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Qt

class Componente(QtWidgets.QWidget):
    def __init__(self, text:str = "", expressão: str = "False", parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
            Componente QLabel {color: #fff; font-size: 20px;}
            QWidget#rectangle {background-color: #000; border-radius: 7px;}
            #ent1, #ent2, #ent3, #saida {background-color: #000; border-radius: 4px;}
            #saidaLed{border-radius: 15px;}
        """)
        self.setFixedSize(225, 128)

        self.expressão = expressão

        self.ents = [False, False, False]

        self.ent1 = QtWidgets.QFrame(parent=self)
        self.ent1.setObjectName("ent1")
        self.ent1.setFixedSize(30, 8)
        self.ent1.move(50, 10)
        self.btEnt1 = QtWidgets.QPushButton(parent=self, text="A: Off")
        self.btEnt1.clicked.connect(lambda: self.setEnt(0))
        self.btEnt1.move(0, 0)

        self.ent2 = QtWidgets.QFrame(parent=self)
        self.ent2.setObjectName("ent2")
        self.ent2.setFixedSize(30, 8)
        self.ent2.move(50, 60)
        self.btEnt2 = QtWidgets.QPushButton(parent=self, text="B: Off")
        self.btEnt2.clicked.connect(lambda: self.setEnt(1))
        self.btEnt2.move(0, 51)

        self.ent3 = QtWidgets.QFrame(parent=self)
        self.ent3.setObjectName("ent3")
        self.ent3.setFixedSize(30, 8)
        self.ent3.move(50, 110)
        self.btEnt3 = QtWidgets.QPushButton(parent=self, text="C: Off")
        self.btEnt3.clicked.connect(lambda: self.setEnt(2))
        self.btEnt3.move(0, 101)

        self.btEnts = [self.btEnt1, self.btEnt2, self.btEnt3]

        self.saida = QtWidgets.QFrame(parent=self)
        self.saida.setObjectName("saida")
        self.saida.setFixedSize(30, 8)
        self.saida.move(170, 60)

        self.saidaLed = QtWidgets.QFrame(parent=self)
        self.saidaLed.setObjectName("saidaLed")
        self.saidaLed.setFixedSize(30, 30)
        self.saidaLed.setStyleSheet("background-color: red;")
        self.saidaLed.move(195, 48)

        self.rectangle = QtWidgets.QFrame(parent=self)
        self.rectangle.setObjectName("rectangle")
        self.rectangle.setFixedSize(100, 128)
        self.rectangle.move(75, 0)

        self.text = QtWidgets.QLabel(parent=self, text=text)
        self.text.setFixedSize(100, 128)
        self.text.move(75, 0)
        self.text.setAlignment(Qt.AlignCenter)
        
    @QtCore.Slot(int)
    def setEnt(self, ent:int):
        self.ents[ent] = not self.ents[ent]
        self.btEnts[ent].setText(f"{chr(65+ent)}: {'On' if self.ents[ent] else 'Off'}")
        # self.btEnts[ent].setStyleSheet("background-color: green;" if self.ents[ent] else "background-color: red;")

    @QtCore.Slot()
    def updateOut(self):
        A = self.ents[0]
        B = self.ents[1]
        C = self.ents[2]

        saída = eval(self.expressão)

        self.saidaLed.setStyleSheet("background-color: green;" if saída else "background-color: red;")


class Projeto(QtWidgets.QWidget):
    updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.useHardware = False
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(60)

        self.componente1 = Componente(text="1", expressão="A and (B or C)", parent=self)
        self.updateSignal.connect(self.componente1.updateOut)

        self.componente2 = Componente(text="2", expressão="A and (B and C)", parent=self)
        self.updateSignal.connect(self.componente2.updateOut)

        self.componente3 = Componente(text="3", expressão="A or (B or C)", parent=self)
        self.updateSignal.connect(self.componente3.updateOut)

        self.componente4 = Componente(text="4", expressão="A and (B != C)", parent=self)
        self.updateSignal.connect(self.componente4.updateOut)

        self.Layout.addWidget(self.componente1, 0, 0)
        self.Layout.addWidget(self.componente2, 0, 1)
        self.Layout.addWidget(self.componente3, 1, 0)
        self.Layout.addWidget(self.componente4, 1, 1)

    @Slot()
    def resetSimulation(self):
        pass

    @Slot(list)
    def updateSimulation(self, data: list):
        self.updateSignal.emit()
        pass

    @Slot()
    def getValues(self):
        self.values[0] = str(1)

        return self.values
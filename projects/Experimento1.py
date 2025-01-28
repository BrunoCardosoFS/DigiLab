from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Qt

class Componente(QtWidgets.QWidget):
    def __init__(self, text:str = "", expressão: str = "False", parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("""
            Componente QLabel {color: #fff; font-size: 25px; font-weight: bold;}
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

class Page1(QtWidgets.QWidget):
    updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = [], loc: list = []):
        super().__init__(parent)

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(60)

        for i, comp in enumerate(components, start=1):
            component = Componente(expressão=comp, text=str(i), parent=self)
            self.updateSignal.connect(component.updateOut)

            self.Layout.addWidget(component, *loc[i-1])

class Page2(QtWidgets.QWidget):
    updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = [], loc: list = []):
        super().__init__(parent)

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(60)

        texto = QtWidgets.QLabel(parent=self, text="Página 2")

        self.Layout.addWidget(texto, 0, 0)
        


class Projeto(QtWidgets.QWidget):
    updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.useHardware = False
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.Layout = QtWidgets.QStackedLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        comp1 = "A and (B or C)"
        comp2 = "A and (B and C)"
        comp3 = "A or (B or C)"
        comp4 = "A and (B != C)"

        components = [comp1, comp2, comp3, comp4]
        loc = [[0,0], [0,1], [1,0], [1,1]]

        self.page1 = Page1(components=components, loc=loc, parent=self)
        self.page2 = Page2(parent=self)

        self.Layout.addWidget(self.page1)
        self.Layout.addWidget(self.page2)

        self.Layout.setCurrentIndex(0)

        

    @Slot()
    def resetSimulation(self):
        pass

    @Slot(list)
    def updateSimulation(self, data: list):
        self.updateSignal.emit()
        self.page1.updateSignal.emit()
        pass

    @Slot()
    def getValues(self):
        self.values[0] = str(1)

        return self.values
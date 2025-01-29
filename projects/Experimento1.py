from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Qt
from PySide6.QtSvgWidgets import QSvgWidget


svg_content = """
<svg width="1000" height="1000" xml:space="preserve" xmlns="http://www.w3.org/2000/svg">
    <rect style="fill:#fff;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" width="1000" height="1000" ry="0"/>
    <path style="fill:#edcf99;fill-opacity:1;stroke-width:1.16646;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M375.225 335.18h249.549v329.64H375.225z"/>
    <path style="fill:#f4f5ed;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M0 0h1000L624.775 335.18h-249.55Z"/>
    <path style="fill:#f3deb9;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M1000 1000V0L624.775 335.18v329.64z"/>
    <path style="fill:#c2a676;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m0 1000 375.225-335.18V335.18L0 0Z"/>
    <path style="fill:#d27857;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m0 1000 375.225-335.18h249.55L1000 1000Z"/>
    <path style="fill:#ffc113;fill-opacity:1;stroke-width:.69453;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M408.928 199.772S434.16 263.827 500 263.827s91.072-64.055 91.072-64.055z"/>
    <path style="fill:#ffa604;fill-opacity:1;stroke-width:1.74962;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M496.915 122.13h6.17v77.642h-6.17z"/>
    <path style="fill:#d68a00;fill-opacity:1;stroke-width:.824063;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M447.235 199.772S443.29 185.634 500 185.634s52.765 14.138 52.765 14.138z"/>
    <path style="fill:#d68a00;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M476.126 115.455h47.748v6.674h-47.748z"/>
    <path style="fill:#a9edf3;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m194.764 686.507 119.204-106.411.458-244.045L194.764 229.16Z"/>
    <path style="fill:#edcf99;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="m314.426 336.051-.458 244.045-8.897 7.942V327.695z"/>
    <path style="fill:#f3deb9;fill-opacity:1;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M194.764 229.16 314.426 336.05l-9.355 2.636-110.307-86.539zM194.764 686.507l119.204-106.411-8.897-4.35-110.307 93.3z"/>
    <path style="fill:#fff;fill-opacity:1;stroke-width:.689446;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M643.386 520.073v24.877l10.258 9.172v-43.221z"/>
    <path style="fill:#e3e3e3;fill-opacity:1;stroke-width:2.12474;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M113.078 540.07V444.72l-70.34-62.892v221.135z"/>
    <path style="fill:#fff;fill-opacity:1;stroke-width:1.5603;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M919.014 504.361v56.301l23.216 20.757v-97.815z"/>
    <path style="fill:#a83837;fill-opacity:1;stroke-width:1.16646;stroke-linecap:round;stroke-linejoin:round;paint-order:markers stroke fill" d="M428.621 379.847H571.38V664.82H428.621z"/>
</svg>
"""



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

        A = self.ents[0]
        B = self.ents[1]
        C = self.ents[2]

        saída = eval(self.expressão)

        self.saidaLed.setStyleSheet("background-color: green;" if saída else "background-color: red;")


class Page1(QtWidgets.QWidget):
    updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = [], position: list = []):
        super().__init__(parent)

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(60)

        for i, comp in enumerate(components, start=1):
            component = Componente(expressão=comp, text=str(i), parent=self)

            self.Layout.addWidget(component, *position[i-1])

class Page2(QtWidgets.QWidget):
    updateSignal = QtCore.Signal(list)
    def __init__(self, parent: QtWidgets.QWidget = None, components: list = []):
        super().__init__(parent)

        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(60)

        # pixmap = QtGui.QPixmap("d:/Arquivos/Projetos/Pesquisa/Simulador-CD/projects/resources/exp1 - IMG1.svg").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # texto = QtWidgets.QLabel(parent=self, text="", pixmap=pixmap)

        # self.Layout.addWidget(texto, 0, 0)

        
        svg_widget = QSvgWidget(parent=self)
        svg_widget.renderer().load(svg_content.encode("utf-8"))

        svg_widget.setFixedSize(300, 300)

        self.Layout.addWidget(svg_widget, 0, 0)
        


class Projeto(QtWidgets.QWidget):
    updateSignal = QtCore.Signal()
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.useHardware = False
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(30)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.Layout.addWidget(self.stackedWidget)

        comp1 = "A and (B or C)"
        comp2 = "A and (B and C)"
        comp3 = "A or (B or C)"
        comp4 = "A and (B != C)"

        components = [comp1, comp2, comp3, comp4]
        position = [[0,0], [0,1], [1,0], [1,1]]

        self.page1 = Page1(components=components, position=position, parent=self.stackedWidget)
        self.page2 = Page2(parent=self.stackedWidget)

        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)

        self.stackedWidget.setCurrentIndex(0)

        self.btTo2 = QtWidgets.QPushButton(parent=self, text="Próximo")
        self.btTo2.clicked.connect(self.nextPage)
        self.Layout.addWidget(self.btTo2)
        
    @Slot(int)
    def togglePage(self, page:int):
        self.stackedWidget.setCurrentIndex(page)
        print(self.stackedWidget.count())

    def nextPage(self):
        c = self.stackedWidget.currentIndex()
        count = self.stackedWidget.count() - 1

        if c < count:
            c = c+1
            self.stackedWidget.setCurrentIndex(c)
        else:
            c = 0
            self.stackedWidget.setCurrentIndex(c)

        if c == count:
            self.btTo2.setText("Voltar")
        else:
            self.btTo2.setText("Próximo")
        
        

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
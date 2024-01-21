from PySide6 import QtWidgets
from PySide6.QtCore import Qt

class Simulation(QtWidgets.QGroupBox):
    def __init__(self, parent: None):
        super().__init__()

        # self.setStyleSheet("QGroupBox{background: red; border: none;}")
        self.setStyleSheet("QGroupBox{background: transparent;}")

        self.setFixedWidth(640)
        self.setFixedHeight(540)

        #Definindo a size policy
        self.policy = self.sizePolicy()
        self.policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)
        self.policy.setVerticalPolicy(QtWidgets.QSizePolicy.Minimum)
        self.setSizePolicy(self.policy)

        self.layout = QtWidgets.QGridLayout(self)

        self.button1 = QtWidgets.QPushButton("Botão 1", self)
        self.button1.setGeometry(50, 50, 100, 30)  # Define a geometria do botão 1

        self.button2 = QtWidgets.QPushButton("Botão 2", self)
        self.button2.setGeometry(150, 100, 100, 30)  # Define a geometria do botão 2

class SimulationScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent: None):
        super().__init__()

        self.item = QtWidgets.QGraphicsRectItem(0, 0, 100, 100)
        self.item1 = QtWidgets.QGraphicsEllipseItem(90, 50, 100, 100)
        self.item.setBrush(Qt.blue)
        self.item1.setBrush(Qt.red)

        self.addItem(self.item)
        self.addItem(self.item1)
        
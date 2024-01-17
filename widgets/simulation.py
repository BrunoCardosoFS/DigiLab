from PySide6 import QtCore, QtWidgets

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
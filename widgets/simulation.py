from PySide6 import QtCore, QtWidgets

class Simulation(QtWidgets.QGroupBox):
    def __init__(self, parent: None):
        super().__init__()

        self.setStyleSheet("QGroupBox{background:red;}")
    
        # self.setMinimumWidth()
        self.setMinimumHeight(460)

        self.setFixedWidth(300)
        self.setFixedHeight(440)

        #Definindo a size policy
        self.policy = self.sizePolicy()
        self.policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)
        self.policy.setVerticalPolicy(QtWidgets.QSizePolicy.Minimum)
        self.setSizePolicy(self.policy)

        print(parent)

        self.button1 = QtWidgets.QPushButton("Botão 1", self)
        self.button1.setGeometry(50, 50, 100, 30)  # Define a geometria do botão 1

        self.button2 = QtWidgets.QPushButton("Botão 2", self)
        self.button2.setGeometry(150, 100, 100, 30)  # Define a geometria do botão 2
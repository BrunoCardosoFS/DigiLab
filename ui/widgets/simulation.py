from PySide6 import QtWidgets
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import Qt, Slot, QUrl

class AreaSimulation(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        
        self.setObjectName("AreaSimulation")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(self.Layout)

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("SimulationScrollArea")

        self.scrollAreaWidget = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidget.setObjectName("SimulationScrollAreaWidget")
        self.layoutScrollAreaWidget = QtWidgets.QVBoxLayout(self.scrollAreaWidget)
        self.layoutScrollAreaWidget.setContentsMargins(3,3,3,3)

        self.quickWidget = QQuickWidget(parent=self)
        self.quickWidget.setSource(QUrl.fromLocalFile('./projects/teste.qml'))
        self.quickWidget.setObjectName("SimulationQuickWidget")
        self.quickWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.layoutScrollAreaWidget.addWidget(self.quickWidget)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.Layout.addWidget(self.scrollArea)
        
from PySide6 import QtWidgets, QtGui, QtCore

class SimulationScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent: None):
        super().__init__()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.aumentar)


        self.bordaTanque = QtWidgets.QGraphicsRectItem(0, 0, 206, 303)
        self.bordaTanque.setBrush(QtCore.Qt.black)
        self.bordaTanque.setPen(QtCore.Qt.NoPen)

        self.tanque = QtWidgets.QGraphicsRectItem(3, -0.5, 200, 300)
        self.tanque.setBrush(QtCore.Qt.white)
        self.tanque.setPen(QtCore.Qt.NoPen)

        self.agua = QtWidgets.QGraphicsRectItem(3, 0, 200, 0)
        self.agua.setBrush(QtCore.Qt.blue)
        self.agua.setPen(QtCore.Qt.NoPen)
        self.agua.setTransformOriginPoint(self.agua.boundingRect().bottomLeft())

        self.addItem(self.bordaTanque)
        self.addItem(self.tanque)
        self.addItem(self.agua)

    @QtCore.Slot()

    def aumentar(self):
        altura_atual = self.agua.rect().height()
        if altura_atual < 290:
            nova_altura_atual = altura_atual + 1
            self.agua.setPos(0, 300.0 - nova_altura_atual)
            self.agua.setRect(self.agua.rect().x(), self.agua.rect().y(), self.agua.rect().width(), nova_altura_atual)
        else:
            self.timer.stop()

    def animation(self):
        self.timer.start(10)

    def stopSimulation(self):
        self.timer.stop()
        self.agua.setPos(0, 0)
        self.agua.setRect(self.agua.rect().x(), self.agua.rect().y(), self.agua.rect().width(), 0)
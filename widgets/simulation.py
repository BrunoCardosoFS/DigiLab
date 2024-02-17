from PySide6 import QtWidgets, QtGui, QtCore

class ButtonValv(QtWidgets.QGraphicsRectItem):
    def __init__(self, x: float, y: float, type: bool):
        super().__init__()
        self.value = 0.25 if(type) else -0.25

        self.setRect(x, y, 20, 20)
        self.setBrush(QtCore.Qt.black)
        self.setPen(QtCore.Qt.NoPen)

class Valvula(QtWidgets.QGraphicsItemGroup):
    def __init__(self, parent: None, x: float, y: float, control: bool, rate: int):
        super().__init__()
        self.rate = rate
        self.opening = 0
        self.isOpen = False

        self.borderPipe = QtWidgets.QGraphicsRectItem((x + 0.3), y, 39, 15)
        self.borderPipe.setBrush(QtCore.Qt.black)
        self.borderPipe.setPen(QtCore.Qt.NoPen)

        self.pipe = QtWidgets.QGraphicsRectItem(x, (y+2), 39.5, 11)
        self.pipe.setBrush(QtCore.Qt.white)
        self.pipe.setPen(QtCore.Qt.NoPen)

        self.valve = QtWidgets.QGraphicsRectItem((x + 19), (y-2), 2, 17)
        self.valve.setBrush(QtCore.Qt.black)
        self.valve.setPen(QtCore.Qt.NoPen)

        self.addToGroup(self.borderPipe)
        self.addToGroup(self.pipe)
        self.addToGroup(self.valve)

        if(control):
            self.textValv = QtWidgets.QGraphicsTextItem("0%")
            self.textValv.setFont(QtGui.QFont("Arial", 11))
            self.textValv.setDefaultTextColor(QtGui.QColor("black"))
            self.textValv.setPos(x + 45, (y - 5))

            self.buttonUp = ButtonValv(x + 50, (y - 25), True)
            self.buttonDown = ButtonValv(x + 50, (y + 20), False)

            self.addToGroup(self.textValv)
            self.addToGroup(self.buttonUp)
            self.addToGroup(self.buttonDown)

    @QtCore.Slot()
    def outValve(self):
        out = self.rate * self.opening
        return out

    def openValv(self):
        self.valve.setPos(0, -13)
        self.opening = 1
        self.isOpen = True

    def closeValv(self):
        self.valve.setPos(0, 0)
        self.opening = 0
        self.isOpen = False

    def mousePressEvent(self, event):
        # print(event.scenePos())
        for item in self.childItems():
            if isinstance(item, ButtonValv) and item.contains(event.scenePos()):
                self.controlValv(item)

    def controlValv(self, item: ButtonValv):
        value = item.value
        if((self.opening>0) and (self.opening<1)):
            self.opening = self.opening + value
        elif(self.opening == 0 and value > 0):
            self.opening = self.opening + value
        elif(self.opening == 1 and value < 0):
            self.opening = self.opening + value
        
        self.textValv.setPlainText(f"{int(self.opening * 100)}%")

        self.valve.setPos(0, (self.opening * -13))

        self.isOpen = True if(self.opening > 0) else False

class Tanque(QtWidgets.QGraphicsItemGroup):
    def __init__(self, parent: None, valvIn: Valvula, valvOut: Valvula):
        super().__init__()
        self.parent = parent
        self.valvIn = valvIn
        self.valvOut = valvOut

        self.bordaTanque = QtWidgets.QGraphicsRectItem(0, 0, 206, 303)
        self.bordaTanque.setBrush(QtCore.Qt.black)
        self.bordaTanque.setPen(QtCore.Qt.NoPen)

        self.tanque = QtWidgets.QGraphicsRectItem(3, -0.5, 200, 300)
        self.tanque.setBrush(QtCore.Qt.white)
        self.tanque.setPen(QtCore.Qt.NoPen)

        self.water = QtWidgets.QGraphicsRectItem(3, 0, 200, 0)
        self.water.setBrush(QtCore.Qt.blue)
        self.water.setPen(QtCore.Qt.NoPen)

        self.addToGroup(self.bordaTanque)
        self.addToGroup(self.tanque)
        self.addToGroup(self.water)

    @QtCore.Slot()
    def changeWater(self):
        currentHeight = self.water.rect().height()
        outValves = self.valvIn.outValve() - self.valvOut.outValve()
        newHeight = currentHeight + outValves

        if((currentHeight >= 295) and (outValves > 0)):
            self.water.setPos(0, 300 - 295)
            self.water.setRect(self.water.rect().x(), self.water.rect().y(), self.water.rect().width(), 295)
            return False
        if((currentHeight <= 0) and (outValves < 0)):
            self.water.setPos(0, 300)
            self.water.setRect(self.water.rect().x(), self.water.rect().y(), self.water.rect().width(), 0)
            return False
        
        self.water.setPos(0, 300 - newHeight)
        self.water.setRect(self.water.rect().x(), self.water.rect().y(), self.water.rect().width(), newHeight)


class SimulationScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent: None):
        super().__init__()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.simulation)

        self.valvulaIn = Valvula(self, -36.5, 5, True, 1)
        self.valvulaOut = Valvula(self, 202.8, 286.5, True, 2)

        self.tanque = Tanque(self, self.valvulaIn, self.valvulaOut)

        self.addItem(self.tanque)
        self.addItem(self.valvulaIn)
        self.addItem(self.valvulaOut)

    @QtCore.Slot()
    def animation(self):
        self.timer.start(25)

    def simulation(self):
        self.tanque.changeWater()

    def startSimulation(self):
        self.timer.start(25)

    def stopSimulation(self):
        self.timer.stop()
        # self.agua.setPos(0, 0)
        # self.agua.setRect(self.agua.rect().x(), self.agua.rect().y(), self.agua.rect().width(), 0)
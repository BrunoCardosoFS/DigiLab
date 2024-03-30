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

    def controlOpenValv(self, open: int):
        if(open == 1):
            self.valve.setPos(0, -13)
            self.opening = 1
            self.isOpen = True
        else:
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

class Sensor(QtWidgets.QGraphicsItemGroup):
    def __init__(self, parent: None, x: float, y: float):
        super().__init__()
        self.parent = parent
        self.isWater = False
        self.vertical = y

        self.sensor = QtWidgets.QGraphicsRectItem((x + 0.3), y, 20, 7)
        self.sensor.setBrush(QtCore.Qt.red)
        self.sensor.setPen(QtCore.Qt.NoPen)

        self.addToGroup(self.sensor)

    @QtCore.Slot()
    def setSensor(self, level: float):
        if((293 - level) <= self.vertical):
            self.isWater = True
            self.sensor.setBrush(QtCore.Qt.green)
        else:
            self.isWater = False
            self.sensor.setBrush(QtCore.Qt.red)

class Tanque(QtWidgets.QGraphicsItemGroup):
    def __init__(self, parent: (QtWidgets.QGraphicsScene | None), valveIn: Valvula, valveOut: Valvula, sensors: list):
        super().__init__()
        self.parent = parent
        self.valveIn = valveIn
        self.valveOut = valveOut
        self.level = 0.0

        self.sensors = []

        # Desenhando o tanque
        borderTank = QtWidgets.QGraphicsRectItem(0, 0, 206, 303)
        borderTank.setBrush(QtCore.Qt.black)
        borderTank.setPen(QtCore.Qt.NoPen)

        tank = QtWidgets.QGraphicsRectItem(3, -0.5, 200, 300)
        tank.setBrush(QtCore.Qt.white)
        tank.setPen(QtCore.Qt.NoPen)

        self.water = QtWidgets.QGraphicsRectItem(3, 0, 200, 0)
        self.water.setBrush(QtCore.Qt.blue)
        self.water.setPen(QtCore.Qt.NoPen)

        # Adicionando os itens ao grupo
        self.addToGroup(borderTank)
        self.addToGroup(tank)
        self.addToGroup(self.water)

        for sensor in sensors:
            posy = ((100 - sensor["y"])*3)
            s = Sensor(self, 0, posy)
            self.sensors.append(s)
            self.addToGroup(s)

    @QtCore.Slot()
    def changeWater(self):
        currentHeight = self.water.rect().height()
        outValves = self.valveIn.outValve() - self.valveOut.outValve()
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

        self.level = (newHeight/3)
        # print(self.level)

        for sensor in self.sensors:
            sensor.setSensor(newHeight)

    
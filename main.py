import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QIcon

from UI.mainwindow import MainWindow

current_path = sys.argv[0].replace("main.py", "")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))

    app.setWindowIcon(QIcon(":/images/icons/icon.ico"))

    # Instanciando a janela principal
    widget = MainWindow()
    # Definindo o tamanho inicial da janela
    widget.resize(800, 500)
    # Mostrando a janela principal
    widget.show()

    sys.exit(app.exec())
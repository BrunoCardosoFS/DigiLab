import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from ui.mainwindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    app.setWindowIcon(QIcon(":/images/icons/icon.ico"))

    # Instantiating the main window
    window = MainWindow()
    # Setting the initial window size
    window.resize(800, 500)
    # Showing the main window
    window.show()

    sys.exit(app.exec())
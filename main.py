import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QIcon, QPalette

from ui.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle(QStyleFactory.create("Fusion"))
    app.setWindowIcon(QIcon(":/images/icons/icon.ico"))

    windowColor = app.palette().color(QPalette.Window)
    isDarkMode = False if windowColor.lightnessF() > 0.5 else True

    # Instantiating the main window
    window = MainWindow(isDarkMode=isDarkMode)
    # Setting the initial window size
    window.resize(800, 500)
    # Showing the main window
    window.show()

    sys.exit(app.exec())
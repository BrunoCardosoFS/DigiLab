#   Copyright (C) 2025 by Bruno Cardoso <brunocardosofs@gmail.com>

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from PySide6.QtGui import QIcon, QPalette

from ui.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    # app.setStyle(QStyleFactory.create("Fusion"))
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
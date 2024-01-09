from PySide6 import QtCore

settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
from styles.variables import lightMode, darkMode

def globalStyle():
    variables = darkMode if (settings.value("darkMode", type=bool)) else lightMode
    style = f"""
        QWidget{{
            color: {variables["txt"]};
        }}

        QWidget#centralwidget{{
            background: {variables["bg1"]}
        }}

        QPushButton{{
            background: {variables["color1"]};
            border: none;
            padding: 7px;
            border-radius: 7px;
        }}

        QComboBox{{
            background: {variables["color1"]};
            border: none;
            padding: 7px;
            border-radius: 7px;
        }}

        QComboBox:editable {{
            background: black;
        }}

        QComboBox:on {{ /* shift the text when the popup opens */
            padding-top: 3px;
            padding-left: 4px;
        }}

        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;

            border-left-width: 1px;
            border-left-color: {variables["color3"]};
            border-left-style: solid; /* just a single line */
            border-top-right-radius: 3px; /* same radius as the QComboBox */
            border-bottom-right-radius: 3px;
        }}

        QComboBox QAbstractItemView {{
            padding: 0;
            border: none;
            background-color: {variables["color1"]}; 
            color: {variables["txt"]};
        }}

        QComboBox QAbstractItemView:item:hover {{
            background-color: {variables["color2"]};
            border:none;
            padding: 5px;
        }}

        QPushButton:hover{{
            background: {variables["color2"]};
        }}

        QGroupBox#LeftMenu{{
            background: {variables["theme"]};
            border: none;
        }}

        QGroupBox#LeftMenu QPushButton{{
            background: {variables["theme1"]};
        }}

        QGroupBox#LeftMenu QPushButton:hover{{
            background: {variables["theme2"]};
        }}

        QGroupBox#ControlSimulator{{
            border: none;
        }}

        QGroupBox#AreaSimulator{{
            background: {variables["bg2"]};
            border: none;
            border-radius: 10px;
            margin: 20px;
        }}
    """

    return style
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

        QPushButton:hover{{
            background: {variables["color2"]};
        }}

        QComboBox{{
            background: {variables["theme1"]};
            border: none;
            padding: 7px;
            border-radius: 7px;
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

        QComboBox:item {{
            height: 30px;
            padding: 0;
            border: none;
            background: {variables["theme1"]}; 
            color: {variables["txt"]};
        }}

        QComboBox:item:hover {{
            background: {variables["theme2"]};
            border:none;
            padding: 5px;
        }}

        QComboBox:item:selected{{
            border: none;
            background: {variables["theme2"]};
        }}

        QComboBox:item:checked{{
            font-weight: bold;
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

        QGroupBox#AreaSimulation{{
            background: {variables["bg2"]};
            border: none;
            border-radius: 10px;
            margin: 20px;
        }}
    """

    return style
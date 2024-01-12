from PySide6 import QtCore

settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
from styles.variables import lightMode, darkMode

def globalStyle(parent: None):
    variables = darkMode if (settings.value("darkMode",defaultValue=parent.isDarkMode, type=bool)) else lightMode

    scrollAreaStyle = f"""
        QScrollArea {{
            border: none;
            border-radius: 0px;
            background-color: transparent;
        }}

        QScrollBar:vertical {{
            width: 10px;
            background-color: transparent;
        }}

        QScrollBar:horizontal {{
            height: 10px;
            background-color: transparent;
        }}

        QScrollBar::handle:vertical, QScrollBar::handle:horizontal {{
            background: {variables["theme2"]};
            border: none;
            border-radius: 5px;
        }}

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
            background: transparent;
            border:none;
        }}
        
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal, QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
            background: transparent;
            border:none;
        }}
    """


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

        {scrollAreaStyle}
    """

    return style
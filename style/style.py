from style.themes import lightMode, darkMode

def globalStyle(isDarkMode: bool):
    variables = darkMode if (isDarkMode) else lightMode

    scrollAreaStyle = f"""
        QGraphicsView {{
            border: none;
            border-radius: 10px;
            background-color: {variables["bg2"]};
            margin: 20px;
        }}

        QScrollBar:vertical {{
            width: 10px;
            background-color: transparent;
        }}

        QScrollBar:horizontal {{
            height: 10px;
            background-color: transparent;
        }}

        QScrollBar::handle {{
            background: {variables["bg2"]};
            border: none;
            border-radius: 5px;
        }}

        QScrollBar::add-line, QScrollBar::sub-line, QScrollBar::add-page, QScrollBar::sub-page {{
            background: transparent;
            border:none;
        }}
    """


    style = f"""
        QWidget{{
            color: {variables["txt"]};
        }}

        QPushButton{{
            background-color: {variables["color1"]};
            border: none;
            border-radius: 5px;
        }}

        QPushButton:hover, QComboBox:hover{{
            background-color: {variables["color2"]};
        }}

        QComboBox{{
            background: {variables["color1"]};
            border: none;
            padding: 7px;
            border-radius: 7px;
        }}

        QComboBox QAbstractItemView {{
            border: none;
            outline: none;
            background-color: {variables["color1"]};
            selection-background-color: {variables["color2"]};
            padding: 0px;
            margin: 0px;
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

        QComboBox::down-arrow {{
            image: url({variables["img-down-arrow"]}); /* Substitua pelo caminho do ícone */
            width: 20px; /* Largura da seta */
            height: 20px; /* Altura da seta */
        }}

        QComboBox:item, QComboBox QAbstractItemView:item {{
            height: 30px;
            padding: 0;
            border: none;
            background: {variables["color1"]}; 
            color: {variables["txt"]};
        }}

        QComboBox:item:hover, QComboBox QAbstractItemView:item:hover {{
            background: {variables["color2"]};
            border:none;
            padding: 5px;
        }}

        QComboBox:item:selected, QComboBox QAbstractItemView:item:selected {{
            border: none;
            border-left:1px solid blue;
            background: {variables["color2"]};
            font-weight: bold;
        }}

        QComboBox:item:checked, QComboBox QAbstractItemView:item:checked {{
            font-weight: bold;
        }}

        #CentralWidget, QMainWindow{{
            background-color: {variables['bg1']};
        }}

        #LeftMenu{{
            background-color: {variables['bg2']};
        }}

        #SimulationScrollArea, #SimulationScrollAreaWidget{{
            background-color: {variables['bg3']};
            border: none;
            border-radius: 10px;
        }}


        {scrollAreaStyle}
    """

    return style
from style.colors import lightMode, darkMode

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
            background: {variables["theme2"]};
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

        #CentralWidget{{
            background-color: {variables['theme1']};
        }}

        #LeftMenu{{
            background-color: {variables['theme2']};
        }}

        #SimulationScrollArea, #SimulationScrollAreaWidget{{
            background-color: {variables['theme2']};
            border: none;
            border-radius: 10px;
        }}


        {scrollAreaStyle}
    """

    return style
import os
from modules.nuitkabuild import compile_with_nuitka

pyfile = os.path.abspath("./main.py")
icon = os.path.abspath("./resources/icons/icon.ico")

compile_with_nuitka(
    pyfile=pyfile,
    product_name="Simulador Circuitos Digitais",
    output_filename="simulador",
    file_version="0.0.1.0",
    file_description="Simulador Circuitos Digitais",
    copyright="Copyright 2024 Bruno Cardoso",
    icon=icon,
    windows_disable_console=True,
    onefile=False,
    other_options=["--mingw64", "--enable-plugin=pyside6"]
)

#--include-qt-plugins=qml
import os
from modules.nuitkabuild import compile_with_nuitka

pyfile = os.path.abspath("./main.py")
icon = os.path.abspath("./resources/icons/icon.ico")

compile_with_nuitka(
    pyfile=pyfile,
    product_name="Simulador Circuitos Digitais",
    output_filename="Simulador CD",
    file_version="0.1.0",
    file_description="Um simulador dos sistemas para implementação de circuitos digitais",
    copyright="Copyright 2024 Bruno Cardoso",
    icon=icon,
    disable_console=True,
    onefile=True,
    other_options=["--mingw64", "--enable-plugin=pyside6"]
)
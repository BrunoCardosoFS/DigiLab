import os
from modules.nuitkabuild import compile_with_nuitka

pyfile = os.path.abspath("./main.py")
icon = os.path.abspath("./resources/icons/icon.ico")

projects = os.path.abspath("./projects")
copyright = os.path.abspath("./COPYING")

compile_with_nuitka(
    pyfile=pyfile,
    product_name="Simulador Circuitos Digitais",
    output_filename="DigiLab",
    file_version="0.0.1.5",
    file_description="Simulador Circuitos Digitais",
    copyright="Copyright 2024 Bruno Cardoso",
    icon=icon,
    windows_disable_console=True,
    onefile=False,
    foldersCopy=[[projects]],
    filesCopy=[[copyright]],
    other_options=["--msvc=latest", "--enable-plugin=pyside6"]
)

# --mingw64
# --enable-plugin=pyside6
# --include-qt-plugins=qml
#   Copyright (C) 2024 by Bruno Cardoso <contato@brunocardosofm.com.br>

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


import os
import subprocess
import sys
import platform
import shutil

system = platform.system()

def copyFiles(filesCopy: list, output_dir: str):
    if filesCopy:
        print(f"Copying files {filesCopy}...")
        for file in filesCopy:
            try:
                if(len(file) > 1):
                    output = f"{output_dir}/{file[1]}"
                    if not os.path.exists(output):
                        os.makedirs(output)
                    shutil.copy(file[0], output)
                else:
                    shutil.copy(file[0], output_dir)
            except:
                print(f"Error copying file: {file}")

def ignore_pycache(path, content):
    return {"__pycache__"} if "__pycache__" in content else set()

def copyFolders(foldersCopy: list, output_dir: str):
    if foldersCopy:
        print(f"Copying folders {foldersCopy}...")
        for folder in foldersCopy:
            try:
                if(len(folder) > 1):
                    shutil.copytree(folder[0], f"{output_dir}/{folder[1]}/{os.path.basename(folder[0])}", ignore=ignore_pycache)
                else:
                    shutil.copytree(folder[0], f"{output_dir}/{os.path.basename(folder[0])}", ignore=ignore_pycache)
            except:
                print(f"Error copying folder: {folder}")

def compile_with_nuitka(
        pyfile: str,
        product_name: str,
        file_version: str,
        file_description: str = "",
        copyright: str = "",
        icon: str = "",
        standalone: bool = True,
        output_filename: str = "",
        output_dir: str = ".output",
        windows_disable_console: bool = False,
        onefile: bool = False,
        needs_admin: bool = False,
        foldersCopy: list = [],
        filesCopy: list = [],
        other_options: list = [],
):
    pyfile = pyfile.replace("\\", "/")

    if(os.path.isabs(output_dir)):
        output = output_dir
    else:
        output = f"{os.path.dirname(pyfile)}/{output_dir}"

    output = output.replace("\\", "/")

    nuitka_options = [
        pyfile
    ]

    if(standalone):
        nuitka_options.append('--standalone')
    if(onefile):
        nuitka_options.append('--onefile')

    nuitka_options.append("--assume-yes-for-downloads")
    nuitka_options.append(f'--output-dir={output}')

    if(output_filename != ""):
        nuitka_options.append(f'--output-filename={output_filename}')


    if windows_disable_console and (system == "Windows"):
        nuitka_options.append('--windows-console-mode=disable')

    if icon and (system == "Windows"):
        nuitka_options.append(f'--windows-icon-from-ico={icon}')

    nuitka_options.append(f'--file-version={file_version}')
    nuitka_options.append(f'--product-name={product_name}')

    if file_description:
        nuitka_options.append(f'--file-description={file_description}')
    if copyright:
        nuitka_options.append(f'--copyright={copyright}')
    if(needs_admin):
        nuitka_options.append('--windows-uac-admin')

    nuitka_options = nuitka_options + other_options

    python_exec = sys.executable

    try:
        print(f"Using Python: {python_exec}")
        print("Compiling with Nuitka...")
        command = [python_exec, "-m", "nuitka"] + nuitka_options + ["--noinclude-numba-mode=nofollow", "--follow-imports"]
        subprocess.run(command, check=True)
        print("\nCompilation completed successfully!")
        output = f"{output}/{os.path.splitext(os.path.basename(pyfile))[0]}.dist"
        copyFolders(foldersCopy, output)
        copyFiles(filesCopy, output)
        print(f"\nCompilation output: {output}")
    except subprocess.CalledProcessError as e:
        print("Compilation error:", e)
        exit(1)

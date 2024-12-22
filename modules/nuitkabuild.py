import os
import subprocess
import sys
import platform 

system = platform.system()

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
        disable_console: bool = False,
        onefile: bool = False,
        needs_admin: bool = False,
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


    if(disable_console):
        if (system == "Windows"):
            nuitka_options.append('--windows-console-mode=disable')
        elif (system == "Linux"):
            nuitka_options.append('--no-console')

    if((icon != "") and (system == "Windows")):
        nuitka_options.append(f'--windows-icon-from-ico={icon}')

    nuitka_options.append(f'--file-version={file_version}')
    nuitka_options.append(f'--product-name={product_name}')

    if(file_description != ""):
        nuitka_options.append(f'--file-description={file_description}')
    if(copyright != ""):
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
        print(f"\nCompilation output: {output}")
    except subprocess.CalledProcessError as e:
        print("Compilation error:", e)
        exit(1)

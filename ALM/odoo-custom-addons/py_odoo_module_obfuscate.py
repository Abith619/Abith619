import os
import sys
from pathlib import Path

EXCLUDED_FILES = ['__init__.py', '__manifest__.py']
META_FILE_EXT = '.pyi'
current_file = os.path.dirname(__file__)


def compile_py_files(module_folder):

    if sys.platform == 'win32':
        delete_command = 'erase /S /Q '
    else:
        delete_command = 'rm -r '

    path = Path(os.path.join(current_file, module_folder))
    files = path.glob('**/*.py')

    for file in files:
        if file.name.title().lower() not in EXCLUDED_FILES:
            os.chdir(os.path.realpath(os.path.dirname(file)))
            try:

                if os.system(f'python -m nuitka --module {os.path.join(os.path.dirname(file),file.name.title().lower())}') == 0:
                    print(f'Compiled {file}')
                    os.system(f"{delete_command}{os.path.realpath(file)}")
                    #print(f'Deleted {file}')
                    meta_file = os.path.realpath(file.name.split('.')[0].lower() + META_FILE_EXT)
                    os.system(f"{delete_command}{os.path.realpath(meta_file)}")
                    #print(f'Deleted {meta_file}')
                else:
                    print(f'Failed compiling {file}')

            except Exception as e:
                print(f'Failed compiling {file}')
                continue

    build_files = [path.glob('**/*.build')]

    for files in build_files:
        for file in files:
            if file.name.title().lower() not in EXCLUDED_FILES:
                if file.is_dir():
                    os.system(f"{delete_command}{os.path.realpath(file)}")
                    print(f'Deleted {os.path.realpath(file)}')


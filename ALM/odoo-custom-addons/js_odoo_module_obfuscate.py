import os
import sys
from pathlib import Path

EXCLUDED_FILES = ['request.js']
META_FILE_EXT = '.js'
current_file = os.path.dirname(__file__)


def compile_js_files(module_folder):
    if sys.platform == 'win32':
        delete_command = 'erase '
    else:
        delete_command = 'rm -r '


    path = Path(os.path.join(current_file, module_folder + "\\static"))
    compiler = os.path.realpath('closure-compiler-v20200719.jar')
    files = path.glob('**/*.js')

    for file in files:
        if file.name.title().lower() not in EXCLUDED_FILES:
            os.chdir(os.path.realpath(os.path.dirname(file)))
            try:

                if os.system(f'java -jar {compiler}  {os.path.join(os.path.dirname(file),file.name.title().lower())} --js_output_file'
                             f' {os.path.join(os.path.dirname(file),file.name.title().lower())}.compiled') == 0:
                    print(f'Compiled {file}')
                    os.system(f"{delete_command}{os.path.realpath(file)}")
                    print(f'Deleted {file}')
                else:
                    print(f'Failed compiling {file}')

            except Exception as e:
                print(f'Failed compiling {file}')
                continue

    compiled_files = path.glob('**/*.compiled')

    for file in compiled_files:
        if file.name.title().lower() not in EXCLUDED_FILES:
            old_file_name = file.name.title().lower().split('.')
            new_file_uri = os.path.join(os.path.dirname(file),old_file_name[0]) + '.js'

            os.system(f"mv {os.path.realpath(file)} {new_file_uri}")
            print(f'Renamed {os.path.realpath(file)}')


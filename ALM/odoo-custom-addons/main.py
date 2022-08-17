import subprocess,os,sys
from py_odoo_module_obfuscate import compile_py_files
from js_odoo_module_obfuscate import compile_js_files

dirname = os.path.dirname(os.path.abspath(__file__))

compile_js_files(sys.argv[1])
compile_py_files(sys.argv[1])

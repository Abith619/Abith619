from __future__ import print_function

""" This module loads all the classes from the wrapped Qt libraries into
its namespace."""

__kits_to_load = [ 'Core', 'Gui', 'Widgets', 'Multimedia', 'Network', 'OpenGL', 'Sql', 'Svg', 'UiTools', 'WebKit', 'WebKitWidgets', 'Xml', 'XmlPatterns' ]

# Set to True when debugging
_CTK_VERBOSE_IMPORT = False

for kit in __kits_to_load:
   try:
     exec("from PythonQt.Qt%s import *" % kit)
   except ImportError as detail:
     if _CTK_VERBOSE_IMPORT:
       print(detail)

if "QObject" not in locals():
  from PythonQt.private import QObject

# Removing things the user shouldn't have to see.
del __kits_to_load, _CTK_VERBOSE_IMPORT

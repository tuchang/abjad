from abjad.tools.imports.get_functions_in_module import _get_functions_in_module
import os


def _import_functions_in_package_to_namespace(package, namespace):
   '''Import all the functions defined in the modules of the package given 
   as a string path into the given namespace.
   Example:
   A package structure like so:
      package.mod1.mod1_func1( )
      package.mod2.mod2_func1( )
      package.mod2.mod2_func2( )
      package.mod3.mod3_func1( )
   Ends up as
      package.mod1_func1( )
      package.mod2_func1( )
      package.mod2_func2( )
      package.mod3_func1( )
   '''
   functions = [ ]
   for root, dirs, files in os.walk(package):
      if root.endswith('test'):
         continue
      for file in files:
         if file.endswith('py') and not file.startswith(('_', '.')):
            module = os.sep.join([root, file[:-3]])
            functions.extend(_get_functions_in_module(module))
   for func in functions:
      #print func.__name__
      namespace[func.__name__] = func 

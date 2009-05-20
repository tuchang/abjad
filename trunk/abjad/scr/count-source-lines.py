#! /usr/bin/env python

import os


def _count_source_lines( ):

   source_lines = 0
   source_modules = 0
   test_lines = 0
   test_modules = 0

   for path, subdirectories, files  in os.walk('.'):
      if not '.svn' in path and not 'documentation' in path:
         modules = [x for x in files if x.endswith('.py')]
         for module in modules:
            lines = os.popen('cat %s | wc -l' % os.path.join(path, module))
            lines = lines.read( )
            lines = int(lines)
            if module.startswith('test_'):
               test_lines += lines
               test_modules += 1
            else:
               source_lines += lines
               source_modules += 1

   return source_modules, source_lines, test_modules, test_lines

def _report(source_modules, source_lines, test_modules, test_lines):

   print ''
   print 'source_modules: %s' % source_modules
   print 'test_modules: %s' % test_modules

   print ''
   print 'source_lines: %s' % source_lines
   print 'test_lines: %s' % test_lines

   print ''
   print 'total lines: %s' % (source_lines + test_lines)
   ratio = test_lines / float(source_lines)
   print 'test-to-source ratio is %s : 1' % round(ratio, 1)  
   print ''

if __name__ == '__main__':
   _report(*_count_source_lines( ))

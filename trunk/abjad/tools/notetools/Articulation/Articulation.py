from abjad.core import _Abjad
from abjad.core import _Immutable


class Articulation(_Abjad, _Immutable):
   '''Any staccato, tenuto, portato or other articulation:

   ::

      abjad> t = notetools.Articulation('staccato', 'up')
      Articulation('^\staccato')
   '''

   __slots__ = ('string', 'direction')

   def __init__(self, *args):
      assert len(args) in range(3)
      if 2 <= len(args):
         assert isinstance(args[0], (str, type(None)))
         assert isinstance(args[1], (str, type(None)))
         string, direction = args
      elif len(args) == 1:
         assert isinstance(args[0], (str, type(None)))
         if args[0]:
            splits = args[0].split('\\')
            assert len(splits) in (1, 2)
            if len(splits) == 1:
               string, direction = args[0], None
            elif len(splits) == 2:
               string = splits[1]
               if splits[0]:
                  direction = splits[0]
               else:
                  direction = None
         else:
            string, direction = None, None
      else:
         string, direction = None, None

      if direction in ('^', 'up'):
         direction = '^'
      elif direction in ('_', 'down'):
         direction = '_'
      elif direction in ('-', 'default', None):
         direction = '-'
      else:
         raise ValueError('can not set articulation direction.')

      object.__setattr__(self, '_string', string)
      object.__setattr__(self, '_direction', direction)

   ## OVERLOADS ##

   def __eq__(self, expr):
      assert isinstance(expr, Articulation)
      if expr.string == self.string and self.direction == expr.direction:
         return True
      else:
         return False

   def __repr__(self):
      return "%s('%s')" % (self.__class__.__name__, self)

   def __str__(self):
      if self.string:
         string = self._shortcut_to_word.get(self.string)
         if not string:
            string = self.string
         return '%s\%s' % (self.direction, string)
      else:
         return ''

   ## PRIVATE ATTRIBUTES ##

   _articulations_supported = ('accent', 'marcato', 
        'staccatissimo',      'espressivo'
        'staccato',           'tenuto'             'portato'
        'upbow',              'downbow'            'flageolet'
        'thumb',              'lheel'              'rheel'
        'ltoe',               'rtoe'               'open'
        'stopped',            'turn'               'reverseturn'
        'trill',              'prall'              'mordent'
        'prallprall'          'prallmordent',      'upprall',
        'downprall',          'upmordent',         'downmordent',
        'pralldown',          'prallup',           'lineprall',
        'signumcongruentiae', 'shortfermata',      'fermata',
        'longfermata',        'verylongfermata',   'segno',
        'coda',               'varcoda', 
        '^', '+', '-', '|', '>', '.', '_',
        )

   _shortcut_to_word = {
         '^':'marcato', '+':'stopped', '-':'tenuto', '|':'staccatissimo', 
         '>':'accent', '.':'staccato', '_':'portato' }

   ## PUBLIC ATTRIBUTES ##

   @property
   def direction(self):
      '''Direction string of articulation:

      ::

         abjad> articulation = notetools.Articulation('staccato', 'up')
         abjad> articulation.direction
         '^'
      '''
      return self._direction

   @property
   def format(self):
      '''LilyPond format string of articulation:

      ::

         abjad> articulation = notetools.Articulation('staccato', 'up')
         abjad> articulation.format
         '^\staccato'
      '''
      return str(self)

   @property
   def string(self):
      '''Name string of articulation:

      ::

         abjad> articulation = notetools.Articulation('staccato', 'up')
         abjad> articulation.string
         'staccato'
      '''
      return self._string

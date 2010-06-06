from abjad.container import Container
from abjad.exceptions import MeasureContiguityError
from abjad.exceptions import MissingMeasureError
from abjad.leaf import _Leaf
from abjad.measure import _Measure
from abjad.tools.iterate.naive_backward_in import naive_backward_in
from abjad.tools.iterate.naive_forward_in import naive_forward_in
from _get_contemporaneous_measure import _get_contemporaneous_measure


def _measure_get(component, direction):
   '''.. versionadded:: 1.1.1

   When `component` is voice, staff or other sequential context,
   and when `component` contains a measure, return first measure 
   in `component`.

   When `component` is voice, staff or other sequential context,
   and when `component` contains no measure, 
   raise :exc:`MissingMeasureError`. 

   When `component` is a measure and there is a measure immediately
   following `component`, return measure immediately following component.

   When `component` is a measure and there is not measure immediately
   following `component`, raise :exc:`MeasureContiguityError`.

   When `component` is a leaf and there is a measure in the parentage
   of `component`, return the measure in the parentage of `component`.

   When `component` is a leaf and there is no measure in the parentage
   of `component`, raise :exc:`MissingMeasureError`.
   '''

   if isinstance(component, _Leaf):
      for parent in component.parentage.parentage[1:]:
         if isinstance(parent, _Measure):
            return parent
      raise MissingMeasureError
   elif isinstance(component, _Measure):
      if direction == '_next':
         return component._navigator._nextNamesake
      elif direction == '_prev':
         return component._navigator._prevNamesake
      else:
         raise ValueError('direction must be _next or _prev.')
   elif isinstance(component, Container):
      return _get_contemporaneous_measure(component, direction)
   elif isinstance(component, (list, tuple)):
      if direction == '_next':
         measure_generator = naive_forward_in(component, _Measure)
      elif direction == '_prev':
         measure_generator = naive_backward_in(component, _Measure)
      else:
         raise ValueError('direction must be _next or _prev.')
      try:
         measure = measure_generator.next( )
         return measure
      except StopIteration:
         raise MissingMeasureError
   else:
      raise TypeError('"%s" is unknown Abjad component.' % component)

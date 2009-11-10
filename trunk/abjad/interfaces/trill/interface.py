from abjad.core.grobhandler import _GrobHandler
from abjad.interfaces.interface.interface import _Interface
from abjad.interfaces.spanner_receptor.receptor import _SpannerReceptor
from abjad.spanners import Trill


class TrillInterface(_Interface, _GrobHandler, _SpannerReceptor):
   '''Handle LilyPond TrillSpanner grob and Abjad Trill spanner.'''

   def __init__(self, client):
      '''Bind to client and LilyPond TrillSpanner grob.
      Receive Abjad Trill spanner.'''
      _Interface.__init__(self, client)
      _GrobHandler.__init__(self, 'TrillSpanner')
      _SpannerReceptor.__init__(self, (Trill, ))

from abjad.spanner.format import _SpannerFormatInterface


class _PianoPedalSpannerFormatInterface(_SpannerFormatInterface):

   def __init__(self, spanner):
      _SpannerFormatInterface.__init__(self, spanner)

   ## PUBLIC METHODS ##

   def before(self, leaf):
      '''Spanner format contribution before leaf.'''
      result = [ ]
      spanner = self.spanner
      if spanner._isMyFirstLeaf(leaf):
         result.append(r"\set Staff.pedalSustainStyle = #'%s" % spanner.style)
      return result

   def right(self, leaf):
      '''Spanner format contribution right of leaf.'''
      result = [ ]
      spanner = self.spanner
      if spanner._isMyFirstLeaf(leaf):
         result.append(spanner._kinds[spanner.kind][0])
      if spanner._isMyLastLeaf(leaf):
         result.append(spanner._kinds[spanner.kind][1])
      return result

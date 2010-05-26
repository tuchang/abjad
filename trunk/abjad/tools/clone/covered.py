from abjad.tools import check
from abjad.tools.parenttools.ignore import _ignore
from abjad.tools.parenttools.restore import _restore
from abjad.tools import spannertools
import copy


def covered(components, n = 1):
   r'''Clone thread-contiguous `components` together with 
   spanners that cover `components`.

   The steps taken in this function are as follows.
   Withdraw `components` from crossing spanners.
   Preserve spanners that `components` cover.
   Deep copy `components`.
   Reapply crossing spanners to source `components`.
   Return copied components with covered spanners. ::

      abjad> voice = Voice(RigidMeasure((2, 8), construct.run(2)) * 3)
      abjad> pitchtools.diatonicize(voice)
      abjad> beam = Beam(voice.leaves[:4])
      abjad> f(voice)
      \new Voice {
              {
                      \time 2/8
                      c'8 [
                      d'8
              }
              {
                      \time 2/8
                      e'8
                      f'8 ]
              }
              {
                      \time 2/8
                      g'8
                      a'8
              }
      }

   ::

      abjad> result = clone.covered(voice.leaves)
      abjad> result
      (Note(c', 8), Note(d', 8), Note(e', 8), Note(f', 8), Note(g', 8), Note(a', 8))

   ::

      abjad> new_voice = Voice(result)
      abjad> f(new_voice)
      \new Voice {
              c'8 [
              d'8
              e'8
              f'8 ]
              g'8
              a'8
      }

   ::

      abjad> voice.leaves[0] is new_voice.leaves[0]
      False

   ::

      abjad> voice.leaves[0].beam.spanner is new_voice.leaves[0].beam.spanner
      False

   Clone `components` a total of `n` times. ::

      abjad> result = clone.covered(voice.leaves[:2], n = 3)
      abjad> result
      (Note(c', 8), Note(d', 8), Note(c', 8), Note(d', 8), Note(c', 8), Note(d', 8))

   ::

      abjad> new_voice = Voice(result)
      abjad> f(new_voice)
      \new Voice {
              c'8
              d'8
              c'8
              d'8
              c'8
              d'8
      }
   '''
   
   if n < 1:
      return [ ]

   check.assert_components(components, contiguity = 'thread')

   spanners = spannertools.get_crossing(components) 
   for spanner in spanners:
      spanner._blockAllComponents( )

   receipt = _ignore(components)

   result = copy.deepcopy(components)
   for component in result:
      component._update._markForUpdateToRoot( )

   _restore(receipt)

   for spanner in spanners:
      spanner._unblockAllComponents( )

   for i in range(n - 1):
      result += covered(components)
      
   return result

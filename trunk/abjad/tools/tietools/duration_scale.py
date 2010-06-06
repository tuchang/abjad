from abjad.rational import Rational
from abjad.tools.tietools.is_chain import is_chain
from abjad.tools.tietools.duration_change import duration_change
from abjad.tools.tietools.get_duration_written import get_duration_written
#from abjad.tools.tietools.get_tie_chain_duration_preprolated import \
#   get_tie_chain_duration_preprolated


def duration_scale(tie_chain, multiplier):
   '''Scale tie chain by multiplier.
      Wraps tie_chain_duration_change.
      Returns tie chain.'''

   ## TODO: Find out why get_tie_chain_duration_preprolated( )
   ##       fails split!
   ##       This can only be changed in tietools.duration_change( ). ##
   ##       Check tietools.duration_change( ). ##

   ## find new tie chain written duration
   new_written_duration = \
      multiplier * get_duration_written(tie_chain)
   #new_written_duration = \
   #  multiplier * get_tie_chain_duration_preprolated(tie_chain)

   ## assign new tie chain written duration and return tie chain
   return duration_change(tie_chain, new_written_duration)

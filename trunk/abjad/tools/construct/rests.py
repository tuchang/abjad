from abjad.helpers.is_duration_token import _is_duration_token
from abjad.tools.construct.helpers import _construct_tied_rest

def rests(durations, direction='big-endian', tied=False):
   '''Constructs a list of rests.
      Parameters:
      durations:  a sinlge duration or a list of durations.
      direction:  may be 'big-endian' or 'little-endian'.
            'big-endian' returns a list of notes of decreasing duration.
            'little-endian' returns a list of notes of increasing duration.
      tied: Set to True to return tied rests. False otherwise.  '''

   if _is_duration_token(durations):
      durations = [durations]

   result = [ ]
   for d in durations:
      result.extend(_construct_tied_rest(d, direction, tied))
   return result




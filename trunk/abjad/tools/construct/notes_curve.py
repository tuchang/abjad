from abjad.helpers.duration_token_unpack import _duration_token_unpack
from abjad.note.note import Note
from abjad.rational.rational import Rational
from abjad.tools import interpolate


def notes_curve(pitches, total, start, stop, exp='cosine', 
   written=Rational(1, 8)):
   '''Returns a train of notes with 'continuously' changing effective durations
      given as the written duration argument times the computed interpolated 
      multipliers. The default written duration is 1/8 note.
      The durations are interpolated from start duration
      argument to stop duration argument. 
      The function returns as many interpolation values as necessary to 
      fill the total duration requested.
      The pitches of the notes are set cyclically from the pitches list.'''

   total = Rational(*_duration_token_unpack(total))
   start = Rational(*_duration_token_unpack(start))
   stop = Rational(*_duration_token_unpack(stop))
   written = Rational(*_duration_token_unpack(written))

   dts = interpolate.divide(total, start, stop, exp)
   result = [ ]
   for i, dt in enumerate(dts):
      note = Note(pitches[i % len(pitches)], written)
      note.duration.multiplier = dt / written 
      result.append(note)
   return result

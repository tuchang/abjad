from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import sequencetools
from experimental.quantizationtools.PitchedQEvent import PitchedQEvent
from experimental.quantizationtools.TerminalQEvent import TerminalQEvent
from experimental.quantizationtools.SilentQEvent import SilentQEvent


def milliseconds_to_q_events(milliseconds, fuse_silences=False):
    '''Convert a list of millisecond durations to a list of
    :py:class:`~abjad.tools.quantizationtools.QEvent` objects.

    Negative duration values can be used to indicate silence.  Any resulting
    pitched :py:class:`~abjad.tools.quantizationtools.QEvent` objects will
    default to using middle-C.

    ::

        >>> from experimental.quantizationtools import milliseconds_to_q_events
        >>> durations = [100, -250, 500]
        >>> for x in milliseconds_to_q_events(durations): x
        ...
        quantizationtools.PitchedQEvent(
            durationtools.Offset(0, 1),
            (NamedChromaticPitch("c'"),),
            attachments=()
            )
        quantizationtools.SilentQEvent(
            durationtools.Offset(100, 1),
            attachments=()
            )
        quantizationtools.PitchedQEvent(
            durationtools.Offset(350, 1),
            (NamedChromaticPitch("c'"),),
            attachments=()
            )
        quantizationtools.TerminalQEvent(
            durationtools.Offset(850, 1)
            )

    Return a list of :py:class:`~abjad.tools.quantizationtools.QEvent` objects.
    '''

    if fuse_silences:
        durations = [x for x in sequencetools.sum_consecutive_sequence_elements_by_sign(milliseconds, sign=[-1]) if x]
    else:
        durations = milliseconds
    offsets = mathtools.cumulative_sums_zero([abs(x) for x in durations])

    q_events = []
    for pair in zip(offsets, durations):
        offset = durationtools.Offset(pair[0])
        duration = pair[1]
        if duration < 0: # negative duration indicates silence
            q_event = SilentQEvent(offset)
        else:
            q_event = PitchedQEvent(offset, [0])
        q_events.append(q_event)

    q_events.append(TerminalQEvent(durationtools.Offset(offsets[-1])))

    return q_events

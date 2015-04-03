# -*- encoding: utf-8 -*-
from abjad.tools.abctools import AbjadValueObject
from abjad.tools import durationtools


class DurationBeatMaker(AbjadValueObject):
    r'''Beat maker.

    Models one way of decomposing meters into beats.

    Maker decomposes meters into beats of approximately equal duration.
    Affordances allow the duration of beats in simple and compound meters to be
    set separately. Beats returned as output from this maker can subsequently
    be passed to a beat group maker to assemble conductors' groupings.

    ..  container:: example

        **Example 1.** Makes quarter-note-durated beats for all meters.

        ::

            >>> maker = rhythmmakertools.DurationBeatMaker(
            ...     compound_beat_duration=Duration(1, 4),
            ...     simple_beat_duration=Duration(1, 4),
            ...     )

        Quarter-note-durated beats for simple meters:

        ::

            >>> maker([metertools.Meter((3, 4))])
            [[Duration(1, 4), Duration(1, 4), Duration(1, 4)]]
            >>> maker([metertools.Meter((3, 2))])
            [[Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4)]]

        Quarter-note-durated beats for compound meters:

        ::

            >>> maker([metertools.Meter((6, 8))])
            [[Duration(1, 4), Duration(1, 4), Duration(1, 4)]]
            >>> maker([metertools.Meter((6, 4))])
            [[Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4)]]

    ..  container:: example

        **Example 2.** Makes dotted-quarter-note-durated beats for all meters.

        ::

            >>> maker = rhythmmakertools.DurationBeatMaker(
            ...     compound_beat_duration=Duration(3, 8),
            ...     simple_beat_duration=Duration(3, 8),
            ...     )

        Dotted-quarter-note-durated beats for simple meters:

        ::

            >>> maker([metertools.Meter((3, 4))])
            [[Duration(3, 8), Duration(3, 8)]]
            >>> maker([metertools.Meter((3, 2))])
            [[Duration(3, 8), Duration(3, 8), Duration(3, 8), Duration(3, 8)]]

        Dotted-quarter-note-durated beats for compound meters:

        ::

            >>> maker([metertools.Meter((6, 8))])
            [[Duration(3, 8), Duration(3, 8)]]
            >>> maker([metertools.Meter((6, 4))])
            [[Duration(3, 8), Duration(3, 8), Duration(3, 8), Duration(3, 8)]]

    ..  container:: example

        **Example 3.** Makes quarter-note-durated-beats for simple meters and
        dotted-quarter-note-durated beats for compound meters.

        ::

            >>> maker = rhythmmakertools.DurationBeatMaker(
            ...     compound_beat_duration=Duration(3, 8),
            ...     simple_beat_duration=Duration(1, 4),
            ...     )

        Quarter-note-durated beats for simple meters:

        ::

            >>> maker([metertools.Meter((3, 4))])
            [[Duration(1, 4), Duration(1, 4), Duration(1, 4)]]
            >>> maker([metertools.Meter((3, 2))])
            [[Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4), Duration(1, 4)]]

        Dotted-quarter-note-durated beats for compound meters:

        ::

            >>> maker([metertools.Meter((6, 8))])
            [[Duration(3, 8), Duration(3, 8)]]
            >>> maker([metertools.Meter((6, 4))])
            [[Duration(3, 8), Duration(3, 8), Duration(3, 8), Duration(3, 8)]]

    Follows the two-step instantiate-once / call-repeatedly pattern shown here.

    Takes a list of meters as input at call-time.

    Returns a list of beat lists as output.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_compound_beat_duration',
        '_simple_beat_duration',
        )

    ### INITIALIZER ###

    def __init__(
        self, 
        compound_beat_duration=None,
        simple_beat_duration=None,
        ):
        if simple_beat_duration is not None:
            simple_beat_duration = durationtools.Duration(simple_beat_duration)
        self._simple_beat_duration = simple_beat_duration
        if compound_beat_duration is not None:
            compound_beat_duration = durationtools.Duration(
                compound_beat_duration)
        self._compound_beat_duration = compound_beat_duration

    ### SPECIAL METHODS ###

    def __call__(self, meters):
        r'''Calls beat-maker on `meters`.

        ..  container:: example

            **Example 1.** Makes quarter-note-durated beats from very short 
            meters:

            ::

                >>> maker = rhythmmakertools.DurationBeatMaker(
                ...     compound_beat_duration=Duration(1, 4),
                ...     simple_beat_duration=Duration(1, 4),
                ...     )

            ::

                >>> maker([metertools.Meter((1, 16))])
                [[Duration(1, 16)]]

            ::

                >>> maker([metertools.Meter((1, 4))])
                [[Duration(1, 4)]]

            ::

                >>> maker([metertools.Meter((5, 16))])
                [[Duration(5, 16)]]

            ::

                >>> maker([metertools.Meter((7, 16))])
                [[Duration(7, 16)]]

            Meters less than two complete beats decompose into a single beat.

        ..  container:: example

            **Example 2a.** Makes quarter-note- and dotted-quarter-note-durated
            beats. Large beats at the beginning:

            ::

                >>> maker = rhythmmakertools.DurationBeatMaker(
                ...     compound_beat_duration=Duration(3, 8),
                ...     simple_beat_duration=Duration(1, 4),
                ...     )

            ::

                >>> for numerator in range(1, 13):
                ...     meter = metertools.Meter(
                ...         (numerator, 8),
                ...         decrease_durations_monotonically=True,
                ...     )
                ...     beats = maker([meter])[0]
                ...     beats = ' + '.join(str(_) for _ in beats)
                ...     message = '{}: {}'.format(str(meter), beats)
                ...     print(message)
                1/8: 1/8
                2/8: 1/4
                3/8: 3/8
                4/8: 1/4 + 1/4
                5/8: 3/8 + 1/4
                6/8: 3/8 + 3/8
                7/8: 3/8 + 1/4 + 1/4
                8/8: 1/4 + 1/4 + 1/4 + 1/4
                9/8: 3/8 + 3/8 + 3/8
                10/8: 1/4 + 1/4 + 1/4 + 1/4 + 1/4
                11/8: 3/8 + 1/4 + 1/4 + 1/4 + 1/4
                12/8: 3/8 + 3/8 + 3/8 + 3/8

            **Example 2b.** Makes quarter-note- and dotted-quarter-note-durated
            beats. Large beats at the end:

            ::

                >>> maker = rhythmmakertools.DurationBeatMaker(
                ...     compound_beat_duration=Duration(3, 8),
                ...     simple_beat_duration=Duration(1, 4),
                ...     )

            ::

                >>> for numerator in range(1, 13):
                ...     meter = metertools.Meter(
                ...         (numerator, 8),
                ...         decrease_durations_monotonically=False,
                ...     )
                ...     beats = maker([meter])[0]
                ...     beats = ' + '.join(str(_) for _ in beats)
                ...     message = '{}: {}'.format(str(meter), beats)
                ...     print(message)
                1/8: 1/8
                2/8: 1/4
                3/8: 3/8
                4/8: 1/4 + 1/4
                5/8: 1/4 + 3/8
                6/8: 3/8 + 3/8
                7/8: 1/4 + 1/4 + 3/8
                8/8: 1/4 + 1/4 + 1/4 + 1/4
                9/8: 3/8 + 3/8 + 3/8
                10/8: 1/4 + 1/4 + 1/4 + 1/4 + 1/4
                11/8: 1/4 + 1/4 + 1/4 + 1/4 + 3/8
                12/8: 3/8 + 3/8 + 3/8 + 3/8

        Returns list of beat lists.
        '''
        beat_lists = []
        for meter in meters:
            beat_list = self._meter_to_beat_list(meter)
            beat_lists.append(beat_list)
        return beat_lists

    ### PRIVATE METHODS ###

    def _meter_to_beat_list(self, meter):
        beat_list = []
        if meter.is_simple:
            if self.simple_beat_duration is not None:
                beat_duration = self.simple_beat_duration
            else:
                beat_list = [meter.duration]
                return beat_list
        elif meter.is_compound:
            if self.compound_beat_duration is not None:
                beat_duration = self.compound_beat_duration
            else:
                beat_list = [meter.duration]
                return beat_list
        if meter.duration < 2 * beat_duration:
            beat_list.append(meter.duration)
        else:
            remaining_duration = meter.duration
            while beat_duration <= remaining_duration:
                beat_list.append(beat_duration)
                remaining_duration -= beat_duration
            if remaining_duration == 0:
                pass
            elif meter.decrease_durations_monotonically:
                beat_list[0] += remaining_duration
            else:
                beat_list[-1] += remaining_duration
        return beat_list

    ### PUBLIC PROPERTIES ###

    @property
    def compound_beat_duration(self):
        r'''Gets beat duration to be used on compound meter.

        Returns duration.
        '''
        return self._compound_beat_duration

    @property
    def simple_beat_duration(self):
        r'''Gets beat duration to be used on simple meter.

        Returns duration.
        '''
        return self._simple_beat_duration
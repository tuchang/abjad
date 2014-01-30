#[ -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import sequencetools
from abjad.tools.spannertools.ComplexBeam import ComplexBeam


class DuratedComplexBeam(ComplexBeam):
    r'''A durated complex beam.

    ..  container:: example

        ::

            >>> staff = Staff("c'16 d'16 e'16 f'16")
            >>> set_(staff).auto_beaming = False
            >>> show(staff) # doctest: +SKIP

        ::

            >>> durations = [Duration(1, 8), Duration(1, 8)]
            >>> beam = spannertools.DuratedComplexBeam(
            ...     durations=durations, 
            ...     span_beam_count=1,
            ...     )
            >>> attach(beam, staff[:])
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print format(staff)
            \new Staff \with {
                autoBeaming = ##f
            } {
                \set stemLeftBeamCount = #0
                \set stemRightBeamCount = #2
                c'16 [
                \set stemLeftBeamCount = #2
                \set stemRightBeamCount = #1
                d'16
                \set stemLeftBeamCount = #1
                \set stemRightBeamCount = #2
                e'16
                \set stemLeftBeamCount = #2
                \set stemRightBeamCount = #0
                f'16 ]
            }

    Beams all beamable leaves in spanner explicitly.

    Groups leaves in spanner according to `durations`.

    Spans leaves between duration groups according to `span_beam_count`.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_durations',
        '_isolated_nib_direction',
        '_span_beam_count',
        )

    ### INITIALIZER ###

    def __init__(
        self, 
        direction=None,
        durations=None, 
        isolated_nib_direction=False, 
        overrides=None,
        span_beam_count=1, 
        ):
        ComplexBeam.__init__(
            self, 
            direction=direction,
            isolated_nib_direction=isolated_nib_direction,
            overrides=overrides,
            )
        durations = self._coerce_durations(durations)
        self._durations = durations
        assert isinstance(span_beam_count, (int, type(None)))
        self._span_beam_count = span_beam_count

    ### PRIVATE PROPERTIES ###

    @property
    def _span_points(self):
        result = []
        if self.durations is not None:
            result.append(self.durations[0])
            for d in self.durations[1:]:
                result.append(result[-1] + d)
        return result

    ### PRIVATE METHODS ###

    @staticmethod
    def _coerce_durations(durations):
        durations = durations or ()
        assert isinstance(durations, (list, tuple))
        durations = [durationtools.Duration(x) for x in durations]
        durations = tuple(durations)
        return durations

    def _copy_keyword_args(self, new):
        ComplexBeam._copy_keyword_args(self, new)
        if self.durations is not None:
            new._durations = self.durations[:]
        new._span_beam_count = self.span_beam_count

    def _format_before_leaf(self, leaf):
        result = []
        #if leaf.beam.beamable:
        if self._is_beamable_component(leaf):
            if self._is_exterior_leaf(leaf):
                left, right = self._get_left_right_for_exterior_leaf(leaf)
            # just right of span_beam_count gap
            elif self._duration_offset_in_me(leaf) in self._span_points and \
                not (self._duration_offset_in_me(leaf) + leaf._get_duration() in \
                self._span_points):
                assert isinstance(self.span_beam_count, int)
                left = self.span_beam_count
                #right = leaf._get_duration()._flags
                right = leaf.written_duration.flag_count
            # just left of span_beam_count gap
            elif self._duration_offset_in_me(leaf) + leaf._get_duration() in \
                self._span_points and \
                not self._duration_offset_in_me(leaf) in self._span_points:
                assert isinstance(self.span_beam_count, int)
                #left = leaf._get_duration()._flags
                left = leaf.written_duration.flag_count
                right = self.span_beam_count
            else:
                left, right = self._get_left_right_for_interior_leaf(leaf)
            if left is not None:
                string = r'\set stemLeftBeamCount = #{}'.format(left)
                result.append(string)
            if right is not None:
                string = r'\set stemRightBeamCount = #{}'.format(right)
                result.append(string)
        return result

    def _fracture_left(self, i):
        self, left, right = ComplexBeam._fracture_left(self, i)
        weights = [left._get_duration(), right._get_duration()]
        assert sum(self.durations) == sum(weights)
        split_durations = sequencetools.split_sequence_by_weights(
            self.durations, 
            weights, 
            cyclic=False, 
            overhang=False,
            )
        left_durations, right_durations = split_durations
        left._durations = left_durations
        right._durations = right_durations
        return self, left, right

    def _fracture_right(self, i):
        self, left, right = ComplexBeam._fracture_right(self, i)
        weights = [left._get_duration(), right._get_duration()]
        assert sum(self.durations) == sum(weights)
        split_durations = sequencetools.split_sequence_by_weights(
            self.durations, 
            weights, 
            cyclic=False, 
            overhang=False,
            )
        left_durations, right_durations = split_durations
        left._durations = left_durations
        right._durations = right_durations
        return self, left, right

    def _reverse_components(self):
        ComplexBeam._reverse_components(self)
        durations = reversed(self.durations)
        durations = tuple(durations)
        self._durations = durations

    ### PUBLIC PROPERTIES ###

    @property
    def durations(self):
        r'''Gets durations of leaf groups in spanner.

        ..  container:: example

            ::

                >>> staff = Staff("c'16 d'16 e'16 f'16")
                >>> durations = [Duration(1, 8), Duration(1, 8)]
                >>> beam = spannertools.DuratedComplexBeam(
                ...     durations=durations,
                ...     )
                >>> attach(beam, staff[:])
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \set stemLeftBeamCount = #0
                    \set stemRightBeamCount = #2
                    c'16 [
                    \set stemLeftBeamCount = #2
                    \set stemRightBeamCount = #1
                    d'16
                    \set stemLeftBeamCount = #1
                    \set stemRightBeamCount = #2
                    e'16
                    \set stemLeftBeamCount = #2
                    \set stemRightBeamCount = #0
                    f'16 ]
                }

            ::

                >>> beam.durations
                (Duration(1, 8), Duration(1, 8))

        Returns tuple of durations or none.
        '''
        return self._durations

    @property
    def span_beam_count(self):
        r'''Gets span beam count of spanner.

        ..  container:: example

            Creates a single span beam between adjacent groups in spanner:

            ::

                >>> staff = Staff("c'32 d'32 e'32 f'32")
                >>> durations = [Duration(1, 16), Duration(1, 16)]
                >>> beam = spannertools.DuratedComplexBeam(
                ...     durations=durations, 
                ...     span_beam_count=1,
                ...     )
                >>> attach(beam, staff[:])
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \set stemLeftBeamCount = #0
                    \set stemRightBeamCount = #3
                    c'32 [
                    \set stemLeftBeamCount = #3
                    \set stemRightBeamCount = #1
                    d'32
                    \set stemLeftBeamCount = #1
                    \set stemRightBeamCount = #3
                    e'32
                    \set stemLeftBeamCount = #3
                    \set stemRightBeamCount = #0
                    f'32 ]
                }

            ::

                >>> beam.span_beam_count
                1

        ..  container:: example

            Creates a double span beam between adjacent groups in spanner:

            ::

                >>> staff = Staff("c'32 d'32 e'32 f'32")
                >>> durations = [Duration(1, 16), Duration(1, 16)]
                >>> beam = spannertools.DuratedComplexBeam(
                ...     durations=durations, 
                ...     span_beam_count=2,
                ...     )
                >>> attach(beam, staff[:])
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \set stemLeftBeamCount = #0
                    \set stemRightBeamCount = #3
                    c'32 [
                    \set stemLeftBeamCount = #3
                    \set stemRightBeamCount = #2
                    d'32
                    \set stemLeftBeamCount = #2
                    \set stemRightBeamCount = #3
                    e'32
                    \set stemLeftBeamCount = #3
                    \set stemRightBeamCount = #0
                    f'32 ]
                }

            ::

                >>> beam.span_beam_count
                2

        ..  container:: example

            Creates no span beam between adjacent groups in spanner:

            ::

                >>> staff = Staff("c'32 d'32 e'32 f'32")
                >>> durations = [Duration(1, 16), Duration(1, 16)]
                >>> beam = spannertools.DuratedComplexBeam(
                ...     durations=durations, 
                ...     span_beam_count=0,
                ...     )
                >>> attach(beam, staff[:])
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \set stemLeftBeamCount = #0
                    \set stemRightBeamCount = #3
                    c'32 [
                    \set stemLeftBeamCount = #3
                    \set stemRightBeamCount = #0
                    d'32
                    \set stemLeftBeamCount = #0
                    \set stemRightBeamCount = #3
                    e'32
                    \set stemLeftBeamCount = #3
                    \set stemRightBeamCount = #0
                    f'32 ]
                }

            ::

                >>> beam.span_beam_count
                0

        Defaults to ``1``.

        Returns nonnegative integer.
        '''
        return self._span_beam_count

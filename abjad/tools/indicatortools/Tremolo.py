# -*- encoding: utf-8 -*-
from abjad.tools.abctools.AbjadValueObject import AbjadValueObject


class Tremolo(AbjadValueObject):
    r'''A (two-note) tremolo.
    
    ..  container:: example

        **Example 1.** Chord with one tremolo beam:

        ::

            >>> chord = Chord("<cs' e'>4")
            >>> tremolo = indicatortools.Tremolo(beam_count=1)
            >>> attach(tremolo, chord)
            >>> show(chord) # doctest: +SKIP

        ..  doctest::

            >>> print(format(chord))
            \repeat tremolo 1
            {
            cs'8 e'8
            }

    ..  container:: example

        **Example 2.** Chord with two tremolo beams:

        ::

            >>> chord = Chord("<cs' e'>4")
            >>> tremolo = indicatortools.Tremolo(beam_count=2)
            >>> attach(tremolo, chord)
            >>> show(chord) # doctest: +SKIP

        ..  doctest::

            >>> print(format(chord))
            \repeat tremolo 2
            {
            cs'16 e'16
            }

    ..  container:: example

        **Example 3.** Chord with three tremolo beams:

        ::

            >>> chord = Chord("<cs' e'>4")
            >>> tremolo = indicatortools.Tremolo(beam_count=3)
            >>> attach(tremolo, chord)
            >>> show(chord) # doctest: +SKIP

        ..  doctest::

            >>> print(format(chord))
            \repeat tremolo 4
            {
            cs'32 e'32
            }

    Tremolo affects the formatting of chords.

    Tremolo has no effect when attached to notes or rests.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_beam_count',
        )

    _format_slot = None

    ### INITIALIZER ###

    def __init__(self, beam_count=3):
        assert isinstance(beam_count, int), repr(beam_count)
        assert 0 < beam_count, repr(beam_count)
        self._beam_count = beam_count

    ### SPECIAL METHODS ###

    def __copy__(self, *args):
        r'''Copies tremolo.

        ::

            >>> import copy
            >>> tremolo_1 = indicatortools.Tremolo(beam_count=2)
            >>> tremolo_2 = copy.copy(tremolo_1)

        ::

            >>> tremolo_1 == tremolo_2
            True

        ::

            >>> tremolo_1 is not tremolo_2
            True

        Returns new tremolo.
        '''
        superclass = super(Tremolo, self)
        return superclass.__copy__(*args)

    def __format__(self, format_specification=''):
        r'''Formats stem tremolo.

        ::

            >>> print(format(tremolo))
            indicatortools.Tremolo(
                beam_count=3,
                )

        Returns string.
        '''
        from abjad.tools import systemtools
        if format_specification in ('', 'storage'):
            return systemtools.StorageFormatManager.get_storage_format(self)
        elif format_specification == 'lilypond':
            message = 'no LilyPond format available.'
            raise Exception(message)
        else:
            message = "format_specification must be 'storage' or ''."
            raise Exception(message)

    def __str__(self):
        r'''Gets string representation of tremolo.

        ..  container:: example

            ::

                >>> str(tremolo)
                'Tremolo(beam_count=3)'

        Returns string.
        '''
        superclass = super(Tremolo, self)
        return superclass.__str__()

    ### PUBLIC PROPERTIES ###

    @property
    def beam_count(self):
        r'''Gets beam count of tremolo.

        ..  container:: example

            ::

                >>> tremolo.beam_count
                3

        Returns positive integer.
        '''
        return self._beam_count
from abjad.tools import contexttools
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.instrumenttools.BrassInstrument import BrassInstrument
from abjad.tools.instrumenttools.WindInstrument import WindInstrument


class FrenchHorn(BrassInstrument, WindInstrument):
    r'''.. versionadded:: 2.0

    Abjad model of the French horn:

    ::

        >>> staff = Staff("c'8 d'8 e'8 f'8")

    ::

        >>> instrumenttools.FrenchHorn()(staff)
        FrenchHorn()(Staff{4})

    ::

        >>> f(staff)
        \new Staff {
            \set Staff.instrumentName = \markup { Horn }
            \set Staff.shortInstrumentName = \markup { Hn. }
            c'8
            d'8
            e'8
            f'8
        }

    ::

        >>> show(staff) # doctest: +SKIP

    The French horn targets staff context by default.
    '''

    ### INITIALIZER ###

    def __init__(self, **kwargs):
        BrassInstrument.__init__(self, **kwargs)
        self._default_instrument_name = 'horn'
        self._default_performer_names.append('hornist')
        self._default_short_instrument_name = 'hn.'
        self._is_primary_instrument = True
        self.sounding_pitch_of_fingered_middle_c = \
            pitchtools.NamedChromaticPitch('f')
        self.primary_clefs = [
            contexttools.ClefMark('treble'), contexttools.ClefMark('bass')]
        self._copy_primary_clefs_to_all_clefs()
        self._traditional_pitch_range = pitchtools.PitchRange(-25, 17)

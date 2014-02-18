# -*- encoding: utf-8 -*-
from abjad import *


instrumentation=instrumenttools.InstrumentationSpecifier(
    performers=instrumenttools.PerformerInventory(
        [
            instrumenttools.Performer(
                name='hornist',
                instruments=instrumenttools.InstrumentInventory(
                    [
                        instrumenttools.FrenchHorn(
                            instrument_name='horn',
                            short_instrument_name='hn.',
                            instrument_name_markup=markuptools.Markup(
                                contents=('Horn',),
                                ),
                            short_instrument_name_markup=markuptools.Markup(
                                contents=('Hn.',),
                                ),
                            allowable_clefs=indicatortools.ClefInventory(
                                [
                                    indicatortools.Clef(
                                        name='bass',
                                        ),
                                    indicatortools.Clef(
                                        name='treble',
                                        ),
                                    ]
                                ),
                            pitch_range=pitchtools.PitchRange(
                                '[B1, F5]'
                                ),
                            sounding_pitch_of_written_middle_c=pitchtools.NamedPitch('f'),
                            ),
                        ]
                    ),
                ),
            instrumenttools.Performer(
                name='trombonist',
                instruments=instrumenttools.InstrumentInventory(
                    [
                        instrumenttools.TenorTrombone(
                            instrument_name='tenor trombone',
                            short_instrument_name='ten. trb.',
                            instrument_name_markup=markuptools.Markup(
                                contents=('Tenor trombone',),
                                ),
                            short_instrument_name_markup=markuptools.Markup(
                                contents=('Ten. trb.',),
                                ),
                            allowable_clefs=indicatortools.ClefInventory(
                                [
                                    indicatortools.Clef(
                                        name='tenor',
                                        ),
                                    indicatortools.Clef(
                                        name='bass',
                                        ),
                                    ]
                                ),
                            pitch_range=pitchtools.PitchRange(
                                '[E2, Eb5]'
                                ),
                            sounding_pitch_of_written_middle_c=pitchtools.NamedPitch("c'"),
                            ),
                        ]
                    ),
                ),
            instrumenttools.Performer(
                name='violinist',
                instruments=instrumenttools.InstrumentInventory(
                    [
                        instrumenttools.Violin(
                            instrument_name='violin',
                            short_instrument_name='vn.',
                            instrument_name_markup=markuptools.Markup(
                                contents=('Violin',),
                                ),
                            short_instrument_name_markup=markuptools.Markup(
                                contents=('Vn.',),
                                ),
                            allowable_clefs=indicatortools.ClefInventory(
                                [
                                    indicatortools.Clef(
                                        name='treble',
                                        ),
                                    ]
                                ),
                            default_tuning=indicatortools.Tuning(
                                pitches=pitchtools.PitchSegment(
                                    (
                                        pitchtools.NamedPitch('g'),
                                        pitchtools.NamedPitch("d'"),
                                        pitchtools.NamedPitch("a'"),
                                        pitchtools.NamedPitch("e''"),
                                        ),
                                    item_class=pitchtools.NamedPitch,
                                    ),
                                ),
                            pitch_range=pitchtools.PitchRange(
                                '[G3, G7]'
                                ),
                            sounding_pitch_of_written_middle_c=pitchtools.NamedPitch("c'"),
                            ),
                        ]
                    ),
                ),
            instrumenttools.Performer(
                name='cellist',
                instruments=instrumenttools.InstrumentInventory(
                    [
                        instrumenttools.Cello(
                            instrument_name='cello',
                            short_instrument_name='vc.',
                            instrument_name_markup=markuptools.Markup(
                                contents=('Cello',),
                                ),
                            short_instrument_name_markup=markuptools.Markup(
                                contents=('Vc.',),
                                ),
                            allowable_clefs=indicatortools.ClefInventory(
                                [
                                    indicatortools.Clef(
                                        name='bass',
                                        ),
                                    indicatortools.Clef(
                                        name='tenor',
                                        ),
                                    indicatortools.Clef(
                                        name='treble',
                                        ),
                                    ]
                                ),
                            default_tuning=indicatortools.Tuning(
                                pitches=pitchtools.PitchSegment(
                                    (
                                        pitchtools.NamedPitch('c,'),
                                        pitchtools.NamedPitch('g,'),
                                        pitchtools.NamedPitch('d'),
                                        pitchtools.NamedPitch('a'),
                                        ),
                                    item_class=pitchtools.NamedPitch,
                                    ),
                                ),
                            pitch_range=pitchtools.PitchRange(
                                '[C2, G5]'
                                ),
                            sounding_pitch_of_written_middle_c=pitchtools.NamedPitch("c'"),
                            ),
                        ]
                    ),
                ),
            instrumenttools.Performer(
                name='pianist',
                instruments=instrumenttools.InstrumentInventory(
                    [
                        instrumenttools.Piano(
                            instrument_name='piano',
                            short_instrument_name='pf.',
                            instrument_name_markup=markuptools.Markup(
                                contents=('Piano',),
                                ),
                            short_instrument_name_markup=markuptools.Markup(
                                contents=('Pf.',),
                                ),
                            allowable_clefs=indicatortools.ClefInventory(
                                [
                                    indicatortools.Clef(
                                        name='treble',
                                        ),
                                    indicatortools.Clef(
                                        name='bass',
                                        ),
                                    ]
                                ),
                            pitch_range=pitchtools.PitchRange(
                                '[A0, C8]'
                                ),
                            sounding_pitch_of_written_middle_c=pitchtools.NamedPitch("c'"),
                            ),
                        ]
                    ),
                ),
            instrumenttools.Performer(
                name='percussionist',
                instruments=instrumenttools.InstrumentInventory(
                    []
                    ),
                ),
            ]
        ),
    )
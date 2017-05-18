# -*- coding: utf-8 -*-
from abjad.tools.datastructuretools.TypedList import TypedList


class RegistrationList(TypedList):
    '''Registration list.

    ..  container:: example

        Two registrations:
        
        ::

            >>> registration_1 = pitchtools.Registration(
            ...     [('[A0, C4)', 15), ('[C4, C8)', 27)]
            ...     )
            >>> registration_2 = pitchtools.Registration(
            ...     [('[A0, C8]', -18)]
            ...     )
            >>> registrations = pitchtools.RegistrationList(
            ...     [registration_1, registration_2]
            ...     )

        ::

            >>> f(registrations)
            abjad.RegistrationList(
                [
                    abjad.Registration(
                        [
                            abjad.RegistrationComponent(
                                source_pitch_range=abjad.PitchRange(
                                    range_string='[A0, C4)',
                                    ),
                                target_octave_start_pitch=abjad.NumberedPitch(15),
                                ),
                            abjad.RegistrationComponent(
                                source_pitch_range=abjad.PitchRange(
                                    range_string='[C4, C8)',
                                    ),
                                target_octave_start_pitch=abjad.NumberedPitch(27),
                                ),
                            ]
                        ),
                    abjad.Registration(
                        [
                            abjad.RegistrationComponent(
                                source_pitch_range=abjad.PitchRange(
                                    range_string='[A0, C8]',
                                    ),
                                target_octave_start_pitch=abjad.NumberedPitch(-18),
                                ),
                            ]
                        ),
                    ]
                )

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### PRIVATE PROPERTIES ###

    @property
    def _item_coercer(self):
        from abjad.tools import pitchtools
        return pitchtools.Registration
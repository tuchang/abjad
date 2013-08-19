# -*- encoding: utf-8 -*-


def chromatic_pitch_names_string_to_named_chromatic_pitch_list(chromatic_pitch_names_string):
    '''Change `chromatic_pitch_names_string` to named chromatic pitch list:

    ::

        >>> string = "cs, cs cs' cs''"
        >>> result = pitchtools.chromatic_pitch_names_string_to_named_chromatic_pitch_list(string)

    ::

        >>> for named_chromatic_pitch in result:
        ...     named_chromatic_pitch
        ...
        NamedPitch('cs,')
        NamedPitch('cs')
        NamedPitch("cs'")
        NamedPitch("cs''")

    Return list of named chromatic pitches.
    '''
    from abjad.tools import pitchtools

    pitches = []
    pitch_strings = chromatic_pitch_names_string.split()
    for pitch_string in pitch_strings:
        pitch = pitchtools.NamedPitch(pitch_string)
        pitches.append(pitch)

    return pitches

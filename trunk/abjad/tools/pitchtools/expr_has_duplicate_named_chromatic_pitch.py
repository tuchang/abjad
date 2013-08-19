# -*- encoding: utf-8 -*-


def expr_has_duplicate_named_chromatic_pitch(expr):
    '''True when `expr` has duplicate named chromatic pitch.
    Otherwise false:

    ::

        >>> chord = Chord([13, 13, 14], (1, 4))
        >>> pitchtools.expr_has_duplicate_named_chromatic_pitch(chord)
        True

    Return boolean.
    '''
    from abjad.tools import pitchtools

    pitches = pitchtools.list_named_chromatic_pitches_in_expr(expr)
    pitch_set = pitchtools.NamedPitchSet(pitches)
    return not len(pitches) == len(pitch_set)

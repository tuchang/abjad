from abjad import *


def test_tuplettools_remove_trivial_tuplets_in_expr_01():
    t = Staff(tuplettools.FixedDurationTuplet(Duration(2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    assert len(t) == 2

    r'''
    \new Staff {
            c'8
            d'8
            e'8
            f'8
    }
    '''

    tuplettools.remove_trivial_tuplets_in_expr(t)

    r'''
    \new Staff {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert len(t) == 4
    assert t.lilypond_format == "\\new Staff {\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"

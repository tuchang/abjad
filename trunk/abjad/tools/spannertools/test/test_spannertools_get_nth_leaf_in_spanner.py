# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_spannertools_get_nth_leaf_in_spanner_01():

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
    beam = spannertools.BeamSpanner(staff[:])

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [
            d'8
        }
        {
            \time 2/8
            e'8
            f'8 ]
        }
    }
    '''

    leaves = staff.select_leaves()

    assert spannertools.get_nth_leaf_in_spanner(beam, 0) is leaves[0]
    assert spannertools.get_nth_leaf_in_spanner(beam, 1) is leaves[1]
    assert spannertools.get_nth_leaf_in_spanner(beam, 2) is leaves[2]
    assert spannertools.get_nth_leaf_in_spanner(beam, 3) is leaves[3]

    assert spannertools.get_nth_leaf_in_spanner(beam, -1) is leaves[-1]
    assert spannertools.get_nth_leaf_in_spanner(beam, -2) is leaves[-2]
    assert spannertools.get_nth_leaf_in_spanner(beam, -3) is leaves[-3]
    assert spannertools.get_nth_leaf_in_spanner(beam, -4) is leaves[-4]

    assert py.test.raises(IndexError,
        'spannertools.get_nth_leaf_in_spanner(beam, 99)')
    assert py.test.raises(IndexError,
        'spannertools.get_nth_leaf_in_spanner(beam, -99)')

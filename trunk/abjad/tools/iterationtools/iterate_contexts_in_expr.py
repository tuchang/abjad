# -*- encoding: utf-8 -*-
from abjad.tools import contexttools


def iterate_contexts_in_expr(expr, reverse=False, start=0, stop=None):
    r'''Iterates contexts in `expr`.

    ::

        >>> staff = Staff([Voice("c'8 d'8"), Voice("e'8 f'8 g'8")])
        >>> Tuplet(Multiplier(2, 3), staff[1][:])
        Tuplet(2/3, [e'8, f'8, g'8])
        >>> staff.is_simultaneous = True

    ..  doctest::

        >>> f(staff)
        \new Staff <<
            \new Voice {
                c'8
                d'8
            }
            \new Voice {
                \times 2/3 {
                    e'8
                    f'8
                    g'8
                }
            }
        >>

    ::

        >>> for x in iterationtools.iterate_contexts_in_expr(staff):
        ...   x
        Staff<<2>>
        Voice{2}
        Voice{1}

    Iterate contexts backward in `expr`:

    ::

        >>> for x in iterationtools.iterate_contexts_in_expr(staff, reverse=True):
        ...   x
        Staff<<2>>
        Voice{1}
        Voice{2}

    Iterates across different logical voices.

    Returns generator.
    '''
    from abjad.tools import iterationtools

    return iterationtools.iterate_components_in_expr(
        expr,
        component_class=contexttools.Context,
        reverse=reverse,
        start=start,
        stop=stop,
        )

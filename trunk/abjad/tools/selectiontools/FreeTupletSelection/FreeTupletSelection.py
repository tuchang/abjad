# -*- encoding: utf-8 -*-
import fractions
import math
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools.selectiontools.Selection import Selection


class FreeTupletSelection(Selection):
    r'''A free selection of tuplets.
    '''

    ### PUBLIC METHODS ###

    # TODO: make work with (non-fixed-duration) tuplets
    # TODO: make work with nested tuplets
    def augmented_to_diminished(self):
        '''Change augmented tuplets in selection to diminished tuplets.

        ..  container:: example
        
            **Example:**

            ::

                >>> tuplet = tuplettools.FixedDurationTuplet(Duration(2, 4), [])
                >>> tuplet.extend("c'8 d'8 e'8")

            ::

                >>> tuplet
                FixedDurationTuplet(1/2, [c'8, d'8, e'8])

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 4/3 {
                    c'8
                    d'8
                    e'8
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplets = selectiontools.select_tuplets([tuplet])
                >>> tuplets.augmented_to_diminished()

            ..  doctest::

                >>> f(tuplet)
                \times 2/3 {
                    c'4
                    d'4
                    e'4
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

        Multiply the written duration of the leaves in tuplet
        by the least power of ``2`` necessary to diminshed tuplet.

        .. note:: Does not yet work with nested tuplets.

        .. note:: Currently only works with fixed-duration tuplets.

        Return none.
        '''
        for tuplet in self:
            tuplet._augmented_to_diminished()

    def change_fixed_duration_tuplets_to_tuplets(expr):
        r'''Change fixed-duration tuplets in selection to tuplets.

        ..  container:: example

            **Example:**

            ::

                >>> tuplet = tuplettools.FixedDurationTuplet((2, 8), "c'8 d'8 e'8")
                >>> staff = Staff(2 * tuplet)

            ::

                >>> for tuplet in staff:
                ...     tuplet
                FixedDurationTuplet(1/4, [c'8, d'8, e'8])
                FixedDurationTuplet(1/4, [c'8, d'8, e'8])

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }
                }

            ::

                >>> show(staff) # doctest: +SKIP

            ::

                >>> tuplets = selectiontools.select_tuplets(staff)
                >>> result = tuplets.change_fixed_duration_tuplets_to_tuplets()

            ::

                >>> for tuplet in staff:
                ...     tuplet
                Tuplet(2/3, [c'8, d'8, e'8])
                Tuplet(2/3, [c'8, d'8, e'8])

        Return tuplets.
        '''
        from abjad.tools import containertools
        from abjad.tools import iterationtools
        from abjad.tools import tuplettools
        result = []
        for tuplet in iterationtools.iterate_tuplets_in_expr(expr):
            if isinstance(tuplet, tuplettools.FixedDurationTuplet):
                multiplier = tuplet.multiplier
                new_tuplet = tuplettools.Tuplet(multiplier, [])
                containertools.move_parentage_children_and_spanners_from_components_to_empty_container(
                    [tuplet], new_tuplet)
                result.append(new_tuplet)
        return result

    def change_tuplets_to_fixed_duration_tuplets(self):
        r'''Change tuplets in selection to fixed-duration tuplets.

        ..  container:: example
        
            **Example:**

            ::

                >>> staff = Staff(r"\times 2/3 { c'8 d'8 e'8 }")
                >>> staff.append(r"\times 2/3 { c'8 d'8 e'8 }")

            ::

                >>> for tuplet in staff:
                ...     tuplet
                Tuplet(2/3, [c'8, d'8, e'8])
                Tuplet(2/3, [c'8, d'8, e'8])

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }
                }

            ::

                >>> show(staff) # doctest: +SKIP

            ::

                >>> tuplets = selectiontools.select_tuplets(staff)
                >>> result = tuplets.change_tuplets_to_fixed_duration_tuplets()

            ::

                >>> for tuplet in staff:
                ...     tuplet
                FixedDurationTuplet(1/4, [c'8, d'8, e'8])
                FixedDurationTuplet(1/4, [c'8, d'8, e'8])

        Return modified tuplets.
        '''
        from abjad.tools import containertools
        from abjad.tools import iterationtools
        from abjad.tools import tuplettools
        result = []
        for tuplet in self:
            if type(tuplet) is tuplettools.Tuplet:
                target_duration = tuplet._preprolated_duration
                new_tuplet = tuplettools.FixedDurationTuplet(
                    target_duration, [])
                containertools.move_parentage_children_and_spanners_from_components_to_empty_container(
                    [tuplet], new_tuplet)
                result.append(new_tuplet)
        return result
    
    # TODO: make work with (non-fixed-duration) tuplets
    # TODO: make work with nested tuplets
    def diminished_to_augmented(self):
        '''Change diminished fixed-duration tuplets in selection 
        to augmented tuplets.

        ..  container:: example

            **Example:**

            ::

                >>> tuplet = tuplettools.FixedDurationTuplet(Duration(2, 8), [])
                >>> tuplet.extend("c'8 d'8 e'8")

            ::

                >>> tuplet
                FixedDurationTuplet(1/4, [c'8, d'8, e'8])

            ..  doctest::

                >>> f(tuplet)
                \times 2/3 {
                    c'8
                    d'8
                    e'8
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplets = selectiontools.select_tuplets([tuplet])
                >>> tuplets.diminished_to_augmented()

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 4/3 {
                    c'16
                    d'16
                    e'16
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

        .. note:: Does not yet work with nested tuplets.

        .. note:: Currently only works with fixed-duration tuplets.

        Divide the written duration of the leaves in `tuplet`
        by the least power of 2 necessary to augment `tuplet`:

        Return none.
        '''
        for tuplet in self:
            tuplet._diminished_to_augmented()

    def fix(self):
        r'''Scale contents of each fixed-duration tuplet in selection 
        by power of two if tuplet multiplier less than ``1/2`` 
        or greater than ``2``.

        ..  container:: example

            **Example:**

                >>> tuplet = tuplettools.FixedDurationTuplet(Duration(2, 8), [])
                >>> tuplet.extend("c'4 d'4 e'4")

            ::

                >>> tuplet
                FixedDurationTuplet(1/4, [c'4, d'4, e'4])

            ..  doctest::

                >>> f(tuplet)
                \times 1/3 {
                    c'4
                    d'4
                    e'4
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplets = selectiontools.select_tuplets([tuplet])
                >>> tuplets.fix()

            ..  doctest::

                >>> f(tuplet)
                \times 2/3 {
                    c'8
                    d'8
                    e'8
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

        Return none.
        '''
        from abjad.tools import leaftools
        from abjad.tools import tuplettools
        for tuplet in self:
            tuplet._fix()

    # TODO: reimplement as a keyword variation on self.remove()
    def move_prolation_to_contents_and_remove(self):
        r'''Move prolation of tupets in selection to contents of 
        of tuplets in selection and then remove tuplets in selection.

        ..  container:: example

            **Example:**

            ::

                >>> staff = Staff(
                ...     r"\times 3/2 { c'8 [ d'8 } \times 3/2 { c'8 d'8 ] }"
                ...     )

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/2 {
                        c'8 [
                        d'8
                    }
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/2 {
                        c'8
                        d'8 ]
                    }
                }

            ::

                >>> show(staff) # doctest: +SKIP

            ::

                >>> selection = selectiontools.select_tuplets(staff[0])
                >>> selection.move_prolation_to_contents_and_remove()

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    c'8. [
                    d'8.
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/2 {
                        c'8
                        d'8 ]
                    }
                }

            ::

                >>> show(staff) # doctest: +SKIP

        Return none.
        '''
        from abjad.tools import componenttools
        from abjad.tools import containertools
        for tuplet in self:
            containertools.scale_contents_of_container(
                tuplet, tuplet.multiplier)
            componenttools.move_parentage_and_spanners_from_components_to_components(
                [tuplet], tuplet[:])
        
    def remove(self):
        r'''Remove tuplets in selection.

        ..  container:: example

            **Example.** Remove trivial tuplets in selection:

            ::

                >>> tuplet_1 = Tuplet((2, 3), "c'4 d'4 e'4")
                >>> tuplet_2 = Tuplet((1, 1), "g'4 fs'4")
                >>> staff = Staff([tuplet_1, tuplet_2])

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \times 2/3 {
                        c'4
                        d'4
                        e'4
                    }
                    {
                        g'4
                        fs'4
                    }
                }

            ::

                >>> show(staff) # doctest: +SKIP

            ::

                >>> selection = selectiontools.select_tuplets(
                ...     staff,
                ...     include_augmented_tuplets=False,
                ...     include_diminished_tuplets=False,
                ...     include_trivial_tuplets=True,
                ...     )

            ::

                >>> selection
                FreeTupletSelection(Tuplet(1, [g'4, fs'4]),)

            ::

                >>> selection.remove()

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \times 2/3 {
                        c'4
                        d'4
                        e'4
                    }
                    g'4
                    fs'4
                }

            ::

                >>> show(staff) # doctest: +SKIP

        Return none.
        '''
        from abjad.tools import componenttools
        for tuplet in self:
            componenttools.move_parentage_and_spanners_from_components_to_components(
                [tuplet], tuplet[:])

    def scale_contents(self, multiplier):
        r'''Scale contents of fixed-duration tuplets in selection
        by `multiplier`.

        ..  container:: example

            **Example.** Double duration of tuplets in selection:

            ::

                >>> tuplet = tuplettools.FixedDurationTuplet((3, 8), [])
                >>> tuplet.extend("c'8 d'8 e'8 f'8 g'8")

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/5 {
                    c'8
                    d'8
                    e'8
                    f'8
                    g'8
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> selection = selectiontools.select_tuplets(tuplet)
                >>> selection.scale_contents(Multiplier(2))

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/5 {
                    c'4
                    d'4
                    e'4
                    f'4
                    g'4
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

        Preserve tuplet multipliers.

        Return none.
        '''
        from abjad.tools import leaftools
        from abjad.tools import tuplettools
        multiplier = durationtools.Multiplier(multiplier)
        for tuplet in self:
            if isinstance(tuplet, tuplettools.FixedDurationTuplet):
                # find new target duration
                old_target_duration = tuplet.target_duration
                new_target_duration = multiplier * old_target_duration
                # change tuplet target duration
                tuplet.target_duration = new_target_duration
                # if multiplier is note head assignable, 
                # scale contents graphically
                if multiplier.is_assignable:
                    for component in tuplet[:]:
                        if isinstance(component, leaftools.Leaf):
                            leaftools.scale_preprolated_leaf_duration(
                                component, multiplier)
            else:
                for component in tuplet[:]:
                    if isinstance(component, leaftools.Leaf):
                        leaftools.scale_preprolated_leaf_duration(
                            component, multiplier)
        self.fix()

    def set_denominator_to_at_least(self, n):
        r'''Set denominator of tuplets in selection to at least `n`.

        ..  container:: example

            **Example.** Set denominator of tuplets to at least ``8``:

            ::

                >>> tuplet = Tuplet(Fraction(3, 5), "c'4 d'8 e'8 f'4 g'2")

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/5 {
                    c'4
                    d'8
                    e'8
                    f'4
                    g'2
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplets = selectiontools.select_tuplets(tuplet)
                >>> tuplets.set_denominator_to_at_least(8)

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 6/10 {
                    c'4
                    d'8
                    e'8
                    f'4
                    g'2
                }

            ::

                >>> show(tuplet) # doctest: +SKIP

        Return none.
        '''
        from abjad.tools import tuplettools

        assert mathtools.is_nonnegative_integer_power_of_two(n)
        Duration = durationtools.Duration
        #for tuplet in iterationtools.iterate_tuplets_in_expr(expr):
        for tuplet in self:
            tuplet.force_fraction = True
            durations = [
                tuplet._contents_duration, 
                tuplet._preprolated_duration, 
                (1, n),
                ]
            duration_pairs = Duration.durations_to_nonreduced_fractions_with_common_denominator(
                durations)
            tuplet.preferred_denominator = duration_pairs[1].numerator

def timespan_2_intersects_timespan_1(
    timespan_1=None, timespan_2=None, hold=False
):
    """
    Makes time relation indicating that ``timespan_2`` intersects
    ``timespan_1``.

    ..  container:: example

        >>> relation = abjad.timespans.timespan_2_intersects_timespan_1()
        >>> abjad.f(relation)
        abjad.timespans.TimespanTimespanTimeRelation(
            inequality=abjad.timespans.CompoundInequality(
                [
                    abjad.timespans.CompoundInequality(
                        [
                            abjad.TimespanInequality('timespan_1.start_offset <= timespan_2.start_offset'),
                            abjad.TimespanInequality('timespan_2.start_offset < timespan_1.stop_offset'),
                            ],
                        logical_operator='and',
                        ),
                    abjad.timespans.CompoundInequality(
                        [
                            abjad.TimespanInequality('timespan_2.start_offset <= timespan_1.start_offset'),
                            abjad.TimespanInequality('timespan_1.start_offset < timespan_2.stop_offset'),
                            ],
                        logical_operator='and',
                        ),
                    ],
                logical_operator='or',
                ),
            )

    Returns time relation or boolean.
    """
    from abjad import timespans

    inequality = timespans.CompoundInequality(
        [
            timespans.CompoundInequality(
                [
                    "timespan_1.start_offset <= timespan_2.start_offset",
                    "timespan_2.start_offset < timespan_1.stop_offset",
                ],
                logical_operator="and",
            ),
            timespans.CompoundInequality(
                [
                    "timespan_2.start_offset <= timespan_1.start_offset",
                    "timespan_1.start_offset < timespan_2.stop_offset",
                ],
                logical_operator="and",
            ),
        ],
        logical_operator="or",
    )

    time_relation = timespans.TimespanTimespanTimeRelation(
        inequality, timespan_1=timespan_1, timespan_2=timespan_2
    )

    if time_relation.is_fully_loaded and not hold:
        return time_relation()
    else:
        return time_relation

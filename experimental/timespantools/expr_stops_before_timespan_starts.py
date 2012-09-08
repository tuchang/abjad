def expr_stops_before_timespan_starts(timespan=None):
    r'''.. versionadded:: 1.0

    Make timespan inequality template indicating that expression happens during timespan::

        >>> from experimental import *

    ::

        >>> timespantools.expr_stops_before_timespan_starts()
        TimespanInequalityTemplate('expr_2.stop <= expr_1.start')

    Return timespan inequality or timespan inequality template.
    '''
    from experimental import timespantools

    template = timespantools.TimespanInequalityTemplate('expr_2.stop <= expr_1.start')

    if timespan is None:
        return template
    else:
        return timespantools.TimespanInequality(template, timespan)

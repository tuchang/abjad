def expr_stops_during_timespan(timespan=None):
    r'''.. versionadded:: 1.0

    Make timespan inequality template indicating that expression stops during timespan::

        >>> from experimental import *

    ::

        >>> timespantools.expr_stops_during_timespan()
        TimespanInequalityTemplate('expr_1.start < expr_2.stop <= expr_1.stop')

    Return timespan inequality or timespan inequality template.
    '''
    from experimental import timespantools

    template = timespantools.TimespanInequalityTemplate('expr_1.start < expr_2.stop <= expr_1.stop')

    if timespan is None:
        return template
    else:
        return timespantools.TimespanInequality(template, timespan)

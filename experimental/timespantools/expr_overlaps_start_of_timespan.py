def expr_overlaps_start_of_timespan(timespan=None):
    r'''.. versionadded:: 1.0

    Make timespan inequality template indicating that expression overlaps start of timespan::

        >>> from experimental import *

    ::

        >>> timespantools.expr_overlaps_start_of_timespan()
        TimespanInequalityTemplate('expr_2.start < expr_1.start < expr_2.stop')

    Return timespan inequality or timespan inequality template.
    '''
    from experimental import timespantools

    template = timespantools.TimespanInequalityTemplate('expr_2.start < expr_1.start < expr_2.stop')

    if timespan is None:
        return template
    else:
        return timespantools.TimespanInequality(template, timespan)

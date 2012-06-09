from abjad.tools import containertools
from abjad.tools.rhythmtreetools._RTMParser import _RTMParser


def parse_rtm_syntax(rtm):
    '''Parse RTM syntax:

    ::

        >>> from abjad.tools.rhythmtreetools import parse_rtm_syntax

    ::

        >>> rtm = '(1 (1 (1 (1 1)) 1))'
        >>> result = parse_rtm_syntax(rtm)
        >>> result
        FixedDurationTuplet(1/4, [c'8, c'16, c'16, c'8])

    Return `FixedDurationTuplet` or `Container` instance.
    '''

    result = _RTMParser()(rtm)

    if 1 < len(result):
        con = containertools.Container()
        for node in result:
            tuplet = node()
            if tuplet.is_trivial:
                con.extend(tuplet[:])
            else:
                con.append(tuplet)
        return con

    else:
        tuplet = result[0]()
        if tuplet.is_trivial:
            con = containertools.Container()
            con.extend(tuplet[:])
            return con
        return tuplet

from abjad.tools import abctools


class CodeBlock(abctools.AbjadObject):

    ### CLASS ATTRIBUTES ###

    __slots__ = ('_ending_line_number', '_hide', '_lines',
        '_starting_line_number', '_strip_prompt')

    ### INITIALIZER ###

    def __init__(self, lines, starting_line_number, ending_line_number,
        hide=False, strip_prompt=False):
        assert starting_line_number < ending_line_number
        self._lines = tuple(lines)
        self._starting_line_number = starting_line_number
        self._ending_line_number = ending_line_number
        self._hide = bool(hide)
        self._strip_prompt = bool(strip_prompt)

    ### PUBLIC READ-ONLY PROPERTIES ###

    @property
    def ending_line_number(self):
        return self._ending_line_number

    @property
    def hide(self):
        return self._hide

    @property
    def lines(self):
        return self._lines

    @property
    def starting_line_number(self):
        return self._starting_line_number

    @property
    def strip_prompt(self):
        return self._strip_prompt

import re

### MAPPINGS ###

_direction_number_to_direction_symbol = {
    0: '',
    1: '+',
    -1: '-',
}

_accidental_abbreviation_to_name = {
    'ss': 'double sharp',
    'ses': 'seven-eighths sharp', # new
    'tqs': 'three-quarters sharp',
    'fes': 'five-eighths sharp', # new
    's': 'sharp',
    'tes': 'three-eighths sharp', # new
    'qs': 'quarter sharp',
    'es': 'eighth sharp', # new
    '': 'natural',
    'ef': 'eighth flat', # new
    'qf': 'quarter flat',
    'tef': 'three-eighths flat', # new
    'f': 'flat',
    'fef': 'five-eighths flat', # new
    'tqf': 'three-quarters flat',
    'sef': 'seven-eighths flat', # new
    'ff': 'double flat',
}

_accidental_abbreviation_to_semitones = {
    'ff': -2,
    'sef': -1.75, # new
    'tqf': -1.5,
    'fef': -1.25, # new
    'f': -1,
    'tef': -0.75, # new
    'qf': -0.5,
    'ef': -0.25, # new
    '': 0,
    'es': 0.25, # new
    'qs': 0.5,
    'tes': 0.75, # new
    's': 1,
    'fes': 1.25, # new
    'tqs': 1.5,
    'ses': 1.75, # new
    'ss': 2,
}

_accidental_abbreviation_to_symbol = {
    'ff': 'bb',
    'sef': '8____', # new TO DO: reassess symbol
    'tqf': 'b~',
    'fef': '8___',  # new TO DO: reassess symbol
    'f': 'b',
    'tef': '8__',   # new TO DO: reassess symbol
    'qf': '~',
    'ef': '8_',     # new TO DO: reassess symbol
    '': '',
    'es': '8^',     # new TO DO: reassess symbol
    'qs': '+',
    'tes': '8^^',   # new TO DO: reassess symbol
    's': '#',
    'fes': '8^^^',  # new TO DO: reassess symbol
    'tqs': '#+',
    'ses': '8^^^^', # new TO DO: reassess symbol
    'ss': '##',
}

_accidental_name_to_abbreviation = {
    'double sharp': 'ss',
    'seven-eighths sharp': 'ses', # new
    'three-quarters sharp': 'tqs',
    'five-eighths sharp': 'fes', # new
    'sharp': 's',
    'three-eighths sharp': 'tes', # new
    'quarter sharp': 'qs',
    'eighth sharp': 'es', # new
    'natural': '',
    'eighth flat': 'ef', # new
    'quarter flat': 'qf',
    'three-eighths flat': 'tef', # new
    'flat': 'f',
    'five-eighths flat': 'fef', # new
    'three-quarters flat': 'tqf',
    'seven-eighths flat': 'sef', # new
    'double flat': 'ff',
}

_accidental_semitones_to_abbreviation = {
    -2: 'ff',
    -1.75: 'sef', # new
    -1.5: 'tqf',
    -1.25: 'fef',   # new
    -1: 'f',
    -0.75: 'tef',   # new
    -0.5: 'qf',
    -0.25: 'ef',    # new
    0: '',
    0.25: 'es',     # new
    0.5: 'qs',
    0.75: 'tes',    # new
    1: 's',
    1.25: 'fes',    # new
    1.5: 'tqs',
    1.75: 'ses', # new
    2: 'ss',
}

_symbolic_accidental_to_abbreviation = {
    'bb': 'ff',
    '8____': 'sef', # new
    'b~': 'tqf',
    '8___': 'fef', # new
    'b': 'f',
    '8__': 'tef', # new
    '~': 'qf',
    '8_': 'ef', # new
    '': '',
    '!': '!',
    '8^': 'es', # new
    '+': 'qs',
    '8^^': 'tes', # new
    '#': 's',
    '8^^^': 'fes', # new
    '#+': 'tqs',
    '8^^^^': 'ses', # new
    '##': 'ss',
}

_symbolic_accidental_to_semitones = {
    'bb': -2,
    '8____': -1.75, # new
    'b~': -1.5,
    '8___': -1.25, # new
    'b': -1,
    '8__': -0.75, # new
    '~': -0.5,
    '8_': -0.25, # new
    '': 0,
    '8^': 0.25, # new
    '+': 0.5,
    '8^^': 0.75, # new
    '#': 1,
    '8^^^': 1.25, # new
    '#+': 1.5,
    '8^^^^': 1.75, # new
    '##': 2,
    'ff': -2,
    'sef': -1.75, # new why are abbreviations to semitones here as well?
    'tqf': -1.5,
    'fef': -1.25, # new
    'f': -1,
    'tef': -0.75, # new
    'qf': -0.5,
    'ef': -0.25, # new
    '': 0,
    'es': 0.25, # new
    'qs': 0.5,
    'tes': 0.75, # new
    's': 1,
    'fes': 1.25, # new
    'tqs': 1.5,
    'ses': 1.75, # new
    'ss': 2,
}

_diatonic_pc_name_to_diatonic_pc_number = {
    'c': 0,
    'd': 1,
    'e': 2,
    'f': 3,
    'g': 4,
    'a': 5,
    'b': 6,
}

_diatonic_pc_name_to_pitch_class_number = {
    'c': 0,
    'd': 2,
    'e': 4,
    'f': 5,
    'g': 7,
    'a': 9,
    'b': 11,
}

_diatonic_pc_number_to_diatonic_pc_name = {
    0: 'c',
    1: 'd',
    2: 'e',
    3: 'f',
    4: 'g',
    5: 'a',
    6: 'b',
}

_diatonic_pc_number_to_pitch_class_number = {
    0: 0,
    1: 2,
    2: 4,
    3: 5,
    4: 7,
    5: 9,
    6: 11,
}

_pitch_class_number_to_diatonic_pc_number = {
    0: 0,
    2: 1,
    4: 2,
    5: 3,
    7: 4,
    9: 5,
    11: 6,
}

_pitch_class_number_to_pitch_class_name = {
    0.0: 'c',
    0.25: 'ces', # new
    0.5: 'cqs',
    0.75: 'ctes', # new
    1.0: 'cs',
    1.25: 'dtef', # new
    1.5: 'dqf',
    1.75: 'def', # new
    2.0: 'd',
    2.25: 'des', # new
    2.5: 'dqs',
    2.75: 'dtes', #new
    3.0: 'ef',
    3.25: 'etef', # new
    3.5: 'eqf',
    3.75: 'eef', # new
    4.0: 'e',
    4.25: 'ees', # new
    4.5: 'eqs',
    4.75: 'etes', # new
    5.0: 'f',
    5.25: 'fes', # new
    5.5: 'fqs',
    5.75: 'ftes', # new
    6.0: 'fs',
    6.25: 'gtef', # new
    6.5: 'gqf',
    6.75: 'gef', # new
    7.0: 'g',
    7.25: 'ges', # new
    7.5: 'gqs',
    7.75: 'gtes', # new
    8.0: 'af',
    8.25: 'atef', # new
    8.5: 'aqf',
    8.75: 'aef', # new
    9.0: 'a',
    9.25: 'aes', # new
    9.5: 'aqs',
    9.75: 'ates', # new
    10.0: 'bf',
    10.25: 'btef', # new
    10.5: 'bqf',
    10.75: 'bef', # new
    11.0: 'b',
    11.25: 'bes', # new
    11.5: 'bqs',
    11.75: 'btes', # new
}

_pitch_class_number_to_pitch_class_name_with_flats = {
    0.0: 'c',
    0.24: 'dsef', # new
    0.5: 'dtqf',
    0.75: 'dfef', # new
    1.0: 'df',
    1.25: 'dtef', # new
    1.5: 'dqf',
    1.75: 'def', # new
    2.0: 'd',
    2.25: 'esef', # new
    2.5: 'etqf',
    2.75: 'efef', # new
    3.0: 'ef',
    3.25: 'etef', # new
    3.5: 'eqf',
    3.75: 'eef', # new
    4.0: 'e',
    4.25: 'ftef', # new
    4.5: 'fqf',
    4.75: 'fef', # new
    5.0: 'f',
    5.25: 'gsef', # new
    5.5: 'gtqf',
    5.75: 'gfef', # new
    6.0: 'gf',
    6.25: 'gtef', # new
    6.5: 'gqf',
    6.75: 'gef', # new
    7.0: 'g',
    7.25: 'asef', # new
    7.5: 'atqf',
    7.75: 'afef', # new
    8.0: 'af',
    8.25: 'atef', # new
    8.5: 'aqf',
    8.75: 'aef', # new
    9.0: 'a',
    9.25: 'bsef', # new
    9.5: 'btqf',
    9.75: 'bfef', # new
    10.0: 'bf',
    10.25: 'btef', # new
    10.5: 'bqf',
    10.75: 'bef', # new
    11.0: 'b',
    11.25: 'ctef', # new
    11.5: 'cqf',
    11.75: 'cef', # new
}

_pitch_class_number_to_pitch_class_name_with_sharps = {
    0.0: 'c',
    0.25: 'ces', # new
    0.5: 'cqs',
    0.75: 'ctes', # new
    1.0: 'cs',
    1.25: 'cfes', # new
    1.5: 'ctqs',
    1.75: 'cses', # new
    2.0: 'd',
    2.25: 'des', # new
    2.5: 'dqs',
    2.75: 'dtes', # new
    3.0: 'ds',
    3.25: 'dfes', # new
    3.5: 'dtqs',
    3.75: 'dses', # new
    4.0: 'e',
    4.25: 'ees', # new
    4.5: 'eqs',
    4.75: 'etes', # new
    5.0: 'f',
    5.25: 'fes', # new
    5.5: 'fqs',
    5.75: 'ftes', # new
    6.0: 'fs',
    6.25: 'ffes', # new
    6.5: 'ftqs',
    6.75: 'fses', # new
    7.0: 'g',
    7.25: 'ges', # new
    7.5: 'gqs',
    7.75: 'gtes', # new
    8.0: 'gs',
    8.25: 'gfes', # new
    8.5: 'gtqs',
    8.75: 'gses', # new
    9.0: 'a',
    9.25: 'aes', # new
    9.5: 'aqs',
    9.75: 'ates', # new
    10.0: 'as',
    10.25: 'afes', # new
    10.5: 'atqs',
    10.75: 'ases', # new
    11.0: 'b',
    11.25: 'bes', # new
    11.5: 'bqs',
    11.75: 'btes', # new
}

_diatonic_number_and_quality_to_semitones = {
    1: {'d': -1, 'P': 0, 'A': 1},
    2: {'d': 0, 'm': 1, 'M': 2, 'A': 3},
    3: {'d': 2, 'm': 3, 'M': 4, 'A': 5},
    4: {'d': 4, 'P': 5, 'A': 6},
    5: {'d': 6, 'P': 7, 'A': 8},
    6: {'d': 7, 'm': 8, 'M': 9, 'A': 10},
    7: {'d': 9, 'm': 10, 'M': 11, 'A': 12},
    8: {'d': 11, 'P': 12, 'A': 13},
}

_semitones_to_quality_and_diatonic_number = {
    0: ('P', 1),
    1: ('m', 2),
    2: ('M', 2),
    3: ('m', 3),
    4: ('M', 3),
    5: ('P', 4),
    6: ('d', 5),
    7: ('P', 5),
    8: ('m', 6),
    9: ('M', 6),
    10: ('m', 7),
    11: ('M', 7),
    12: ('P', 8),
}

_quality_abbreviation_to_quality_string = {
    'M': 'major',
    'm': 'minor',
    'P': 'perfect',
    'aug': 'augmented',
    'dim': 'diminished',
    'A': 'augmented',
    'd': 'diminished',
    }

_quality_string_to_quality_abbreviation = {
    'major': 'M',
    'minor': 'm',
    'perfect': 'P',
    'augmented': 'A',
    'diminished': 'd',
    }

_semitones_to_quality_string_and_number = {
    0: ('perfect', 1),
    1: ('minor', 2),
    2: ('major', 2),
    3: ('minor', 3),
    4: ('major', 3),
    5: ('perfect', 4),
    6: ('diminished', 5),
    7: ('perfect', 5),
    8: ('minor', 6),
    9: ('major', 6),
    10: ('minor', 7),
    11: ('major', 7),
    }

_start_punctuation_to_inclusivity_string = {
    '[': 'inclusive',
    '(': 'exclusive',
}

_stop_punctuation_to_inclusivity_string = {
    ']': 'inclusive',
    ')': 'exclusive',
}

### REGEX ATOMS ###

_integer_regex_atom = '-?\d+'
#fix this
_alphabetic_accidental_regex_atom = """
    (?P<alphabetic_accidental>
    [s]*(qs)?
    |[s]*(es)?
    |[f]*(es)?
    |[f]*(qf)?
    |[f]*(ef)?
    |t?q?e?[fs]
    |)
    """
#fix this
_symbolic_accidental_regex_atom = '''
    (?P<symbol>
    [#]+[+]?
    |[b]+[~]?
    |[+]
    |[~]
    |[_]
    |[^]
    |[8]_+
    |[8]\^+
    |
    )
    '''

_octave_number_regex_atom = (
    '(?P<octave_number>{}|)'.format(_integer_regex_atom)
)

_octave_tick_regex_atom = (
    '(?P<octave_tick>'
    ',+'
    "|'+"
    '|'
    ')'
)

_diatonic_pc_name_regex_atom = (
    '(?P<diatonic_pc_name>'
    '[A-Ga-g]'
    ')'
)

### REGEX BODIES ###

_comprehensive_accidental_regex_body = (
    '(?P<comprehensive_accidental>{}|{})'
).format(
    _alphabetic_accidental_regex_atom,
    _symbolic_accidental_regex_atom,
)

_comprehensive_octave_regex_body = (
    '(?P<comprehensive_octave>{}|{})'
).format(
    _octave_number_regex_atom,
    _octave_tick_regex_atom,
)

_comprehensive_pitch_class_name_regex_body = (
    '(?P<comprehensive_pitch_class_name>{}{})'
).format(
    _diatonic_pc_name_regex_atom,
    _comprehensive_accidental_regex_body,
)

_comprehensive_pitch_name_regex_body = (
    '(?P<comprehensive_pitch_name>{}{}{})'
).format(
    _diatonic_pc_name_regex_atom,
    _comprehensive_accidental_regex_body,
    _comprehensive_octave_regex_body,
)

_pitch_class_name_regex_body = (
    '(?P<pitch_class_name>{}{})'
).format(
    _diatonic_pc_name_regex_atom,
    _alphabetic_accidental_regex_atom,
)

_pitch_class_octave_number_regex_body = (
    '(?P<pitch_class_octave_number>{}{}{})'
).format(
    _diatonic_pc_name_regex_atom,
    _comprehensive_accidental_regex_body,
    _octave_number_regex_atom,
)

_pitch_name_regex_body = (
    '(?P<pitch_name>{}{}{})'
).format(
    _diatonic_pc_name_regex_atom,
    _alphabetic_accidental_regex_atom,
    _octave_tick_regex_atom,
)

_range_string_regex_body = '''
    (?P<open_bracket>
        [\[(]       # open bracket or open parenthesis
    )
    (?P<start_pitch>
        {}|{}|(?P<start_pitch_number>-?\d+) # start pitch
    )
    ,               # comma
    [ ]*            # any amount of whitespace
    (?P<stop_pitch>
        {}|{}|(?P<stop_pitch_number>-?\d+) # stop pitch
    )
    (?P<close_bracket>
        [\])]       # close bracket or close parenthesis
    )
    '''.format(
    _pitch_class_octave_number_regex_body.replace('<', '<us_start_'),
    _pitch_name_regex_body.replace('<', '<ly_start_'),
    _pitch_class_octave_number_regex_body.replace('<', '<us_stop_'),
    _pitch_name_regex_body.replace('<', '<ly_stop_'),
)

_interval_name_abbreviation_regex_body = '''
    (?P<direction>[+,-]?)  # one plus, one minus, or neither
    (?P<quality>           # exactly one quality abbreviation
        M|                 # major
        m|                 # minor
        P|                 # perfect
        aug|               # augmented
        A+|                # (possibly) multi-augmented
        dim|               # dimished
        d+                 # (possibly) multi-diminished
    )
    (?P<quartertone>[+~]?) # followed by an optional quartertone inflection
    (?P<number>\d+)        # followed by one or more digits
    '''

### REGEX PATTERNS ###

_alphabetic_accidental_regex = re.compile(
    '^{}$'.format(_alphabetic_accidental_regex_atom),
    re.VERBOSE,
)

_symbolic_accidental_regex = re.compile(
    '^{}$'.format(_symbolic_accidental_regex_atom),
    re.VERBOSE,
)

_comprehensive_accidental_regex = re.compile(
    '^{}$'.format(_comprehensive_accidental_regex_body),
    re.VERBOSE,
)

_octave_tick_regex = re.compile(
    '^{}$'.format(_octave_tick_regex_atom),
    re.VERBOSE,
)

_octave_number_regex = re.compile(
    '^{}$'.format(_octave_number_regex_atom),
    re.VERBOSE,
)

_diatonic_pc_name_regex = re.compile(
    '^{}$'.format(_diatonic_pc_name_regex_atom),
    re.VERBOSE,
)

_comprehensive_accidental_regex = re.compile(
    '^{}$'.format(_comprehensive_accidental_regex_body),
    re.VERBOSE,
)

_comprehensive_octave_regex = re.compile(
    '^{}$'.format(_comprehensive_octave_regex_body),
    re.VERBOSE,
)

_comprehensive_pitch_class_name_regex = re.compile(
    '^{}$'.format(_comprehensive_pitch_class_name_regex_body),
    re.VERBOSE,
)

_comprehensive_pitch_name_regex = re.compile(
    '^{}$'.format(_comprehensive_pitch_name_regex_body),
    re.VERBOSE,
)

_pitch_class_name_regex = re.compile(
    '^{}$'.format(_pitch_class_name_regex_body),
    re.VERBOSE,
)

_pitch_class_octave_number_regex = re.compile(
    '^{}$'.format(_pitch_class_octave_number_regex_body),
    re.VERBOSE,
)

_pitch_name_regex = re.compile(
    '^{}$'.format(_pitch_name_regex_body),
    re.VERBOSE,
)

_range_string_regex = re.compile(
    '^{}$'.format(_range_string_regex_body),
    re.VERBOSE,
)

_interval_name_abbreviation_regex = re.compile(
    '^{}$'.format(_interval_name_abbreviation_regex_body),
    re.VERBOSE,
    )

del re

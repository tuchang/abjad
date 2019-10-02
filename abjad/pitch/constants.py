import re

try:
    from quicktions import Fraction
except ImportError:
    from fractions import Fraction


### MAPPINGS ###

_direction_number_to_direction_symbol = {0: "", 1: "+", -1: "-"}

_accidental_abbreviation_to_semitones = {
    "sxf": Fraction(-7, 6) * 2,
    "ttf": Fraction(-13, 12) * 2,
    "ff": Fraction(-1) * 2,
    "etf": Fraction(-11, 12) * 2,
    "sef": Fraction(-7, 8) * 2,
    "fxf": Fraction(-5, 6) * 2,
    "tqf": Fraction(-3, 4) * 2,
    "trf": Fraction(-2, 3) * 2,
    "fef": Fraction(-5, 8) * 2,
    "stf": Fraction(-7, 12) * 2,
    "f": Fraction(-1, 2) * 2,
    "ftf": Fraction(-5, 12) * 2,
    "tef": Fraction(-3, 8) * 2,
    "rf": Fraction(-1, 3) * 2,
    "qf": Fraction(-1, 4) * 2,
    "xf": Fraction(-1, 6) * 2,
    "ef": Fraction(-1, 8) * 2,
    "tf": Fraction(-1, 12) * 2,
    "": Fraction(0),
    "ts": Fraction(1, 12) * 2,
    "es": Fraction(1, 8) * 2,
    "xs": Fraction(1, 6) * 2,
    "qs": Fraction(1, 4) * 2,
    "rs": Fraction(1, 3) * 2,
    "tes": Fraction(3, 8) * 2,
    "fts": Fraction(5, 12) * 2,
    "s": Fraction(1, 2) * 2,
    "sts": Fraction(7, 12) * 2,
    "fes": Fraction(5, 8) * 2,
    "trs": Fraction(2, 3) * 2,
    "tqs": Fraction(3, 4) * 2,
    "fxs": Fraction(5, 6) * 2,
    "ses": Fraction(7, 8) * 2,
    "ets": Fraction(11, 12) * 2,
    "ss": Fraction(1) * 2,
    "tts": Fraction(13, 12) * 2,
    "sxs": Fraction(7, 6) * 2,
}

_accidental_abbreviation_to_symbol = {
    "ff": "bb",
    "tqf": "b~",
    "f": "b",
    "qf": "~",
    "": "",
    "qs": "+",
    "s": "#",
    "tqs": "#+",
    "ss": "##",
    "rf": "3_",
    "rs": "3^",
    "trf": "3__",
    "trs": "3^^",
    "xf": "6_",
    "xs": "6^",
    "fxf": "6__",
    "fxs": "6^^",
    "sxf": "6___",
    "sxs": "6^^^",
    "ef": "8_",
    "es": "8^",
    "tef": "8__",
    "tes": "8^^",
    "fef": "8___",
    "fes": "8^^^",
    "sef": "8____",
    "ses": "8^^^^",
    "tf": "12_",
    "ts": "12^",
    "ftf": "12__",
    "fts": "12^^",
    "stf": "12___",
    "sts": "12^^^",
    "etf": "12____",
    "ets": "12^^^^",
    "ttf": "12_____",
    "tts": "12^^^^^",
}

_accidental_semitones_to_abbreviation = {
    Fraction(-7, 6) * 2: "sxf",
    Fraction(-13, 12) * 2: "ttf",
    Fraction(-1) * 2: "ff",
    Fraction(-11, 12) * 2: "etf",
    Fraction(-7, 8) * 2: "sef",
    Fraction(-5, 6) * 2: "fxf",
    Fraction(-3, 4) * 2: "tqf",
    Fraction(-2, 3) * 2: "trf",
    Fraction(-5, 8) * 2: "fef",
    Fraction(-7, 12) * 2: "stf",
    Fraction(-1, 2) * 2: "f",
    Fraction(-5, 12) * 2: "ftf",
    Fraction(-3, 8) * 2: "tef",
    Fraction(-1, 3) * 2: "rf",
    Fraction(-1, 4) * 2: "qf",
    Fraction(-1, 6) * 2: "xf",
    Fraction(-1, 8) * 2: "ef",
    Fraction(-1, 12) * 2: "tf",
    Fraction(0): "",
    Fraction(1, 12) * 2: "ts",
    Fraction(1, 8) * 2: "es",
    Fraction(1, 6) * 2: "xs",
    Fraction(1, 4) * 2: "qs",
    Fraction(1, 3) * 2: "rs",
    Fraction(3, 8) * 2: "tes",
    Fraction(5, 12) * 2: "fts",
    Fraction(1, 2) * 2: "s",
    Fraction(7, 12) * 2: "sts",
    Fraction(5, 8) * 2: "fes",
    Fraction(2, 3) * 2: "trs",
    Fraction(3, 4) * 2: "tqs",
    Fraction(5, 6) * 2: "fxs",
    Fraction(7, 8) * 2: "ses",
    Fraction(11, 12) * 2: "ets",
    Fraction(1) * 2: "ss",
    Fraction(13, 12) * 2: "tts",
    Fraction(7, 6) * 2: "sxs",
}

_symbolic_accidental_to_abbreviation = {
    "bb": "ff",
    "b~": "tqf",
    "b": "f",
    "~": "qf",
    "": "",
    "+": "qs",
    "#": "s",
    "#+": "tqs",
    "##": "ss",
    "3_": "rf",
    "3^": "rs",
    "3__": "trf",
    "3^^": "trs",
    "6_": "xf",
    "6^": "xs",
    "6__": "fxf",
    "6^^": "fxs",
    "6___": "sxf",
    "6^^^": "sxs",
    "8_": "ef",
    "8^": "es",
    "8__": "tef",
    "8^^": "tes",
    "8___": "fef",
    "8^^^": "fes",
    "8____": "sef",
    "8^^^^": "ses",
    "12_": "tf",
    "12^": "ts",
    "12__": "ftf",
    "12^^": "fts",
    "12___": "stf",
    "12^^^": "sts",
    "12____": "etf",
    "12^^^^": "ets",
    "12_____": "ttf",
    "12^^^^^": "tts",
}

_symbolic_accidental_to_semitones = {
    "bb": Fraction(-1) * 2,
    "b~": Fraction(-3, 4) * 2,
    "b": Fraction(-1, 2) * 2,
    "~": Fraction(-1, 4) * 2,
    "": Fraction(0),
    "+": Fraction(1, 4) * 2,
    "#": Fraction(1, 2) * 2,
    "#+": Fraction(3, 4) * 2,
    "##": Fraction(1) * 2,
    "3_": Fraction(-1, 3) * 2,
    "3^": Fraction(1, 3) * 2,
    "3__": Fraction(-2, 3) * 2,
    "3^^": Fraction(2, 3) * 2,
    "6_": Fraction(-1, 6) * 2,
    "6^": Fraction(1, 6) * 2,
    "6__": Fraction(-5, 6) * 2,
    "6^^": Fraction(5, 6) * 2,
    "6___": Fraction(-7, 6) * 2,
    "6^^^": Fraction(7, 6) * 2,
    "8_": Fraction(-1, 8) * 2,
    "8^": Fraction(1, 8) * 2,
    "8__": Fraction(-3, 8) * 2,
    "8^^": Fraction(3, 8) * 2,
    "8___": Fraction(-5, 8) * 2,
    "8^^^": Fraction(5, 8) * 2,
    "8____": Fraction(-7, 8) * 2,
    "8^^^^": Fraction(7, 8) * 2,
    "12_": Fraction(-1, 12) * 2,
    "12^": Fraction(1, 12) * 2,
    "12__": Fraction(-5, 12) * 2,
    "12^^": Fraction(5, 12) * 2,
    "12___": Fraction(-7, 12) * 2,
    "12^^^": Fraction(7, 12) * 2,
    "12____": Fraction(-11, 12) * 2,
    "12^^^^": Fraction(11, 12) * 2,
    "12_____": Fraction(-13, 12) * 2,
    "12^^^^^": Fraction(13, 12) * 2,
}

_diatonic_pc_name_to_diatonic_pc_number = {
    "c": 0,
    "d": 1,
    "e": 2,
    "f": 3,
    "g": 4,
    "a": 5,
    "b": 6,
}

_diatonic_pc_name_to_pitch_class_number = {
    "c": 0,
    "d": 2,
    "e": 4,
    "f": 5,
    "g": 7,
    "a": 9,
    "b": 11,
}

_diatonic_pc_number_to_diatonic_pc_name = {
    0: "c",
    1: "d",
    2: "e",
    3: "f",
    4: "g",
    5: "a",
    6: "b",
}

_diatonic_pc_number_to_pitch_class_number = {0: 0, 1: 2, 2: 4, 3: 5, 4: 7, 5: 9, 6: 11}

_pitch_class_number_to_diatonic_pc_number = {0: 0, 2: 1, 4: 2, 5: 3, 7: 4, 9: 5, 11: 6}

_pitch_class_number_to_pitch_class_name = {
    Fraction(0) * 2: "c",
    Fraction(1, 12) * 2: "cts",
    Fraction(1, 8) * 2: "ces",
    Fraction(1, 6) * 2: "cxs",
    Fraction(1, 4) * 2: "cqs",
    Fraction(1, 3) * 2: "crs",
    Fraction(3, 8) * 2: "ctes",
    Fraction(5, 12) * 2: "cfts",
    Fraction(1, 2) * 2: "cs",
    Fraction(7, 12) * 2: "dftf",
    Fraction(5, 8) * 2: "dtef",
    Fraction(2, 3) * 2: "drf",
    Fraction(3, 4) * 2: "dqf",
    Fraction(5, 6) * 2: "dxf",
    Fraction(7, 8) * 2: "def",
    Fraction(11, 12) * 2: "dtf",
    Fraction(1) * 2: "d",
    Fraction(13, 12) * 2: "dts",
    Fraction(9, 8) * 2: "des",
    Fraction(7, 6) * 2: "dxs",
    Fraction(5, 4) * 2: "dqs",
    Fraction(4, 3) * 2: "drs",
    Fraction(11, 8) * 2: "dtes",
    Fraction(17, 12) * 2: "dfts",
    Fraction(3, 2) * 2: "ef",
    Fraction(19, 12) * 2: "eftf",
    Fraction(13, 8) * 2: "etef",
    Fraction(5, 3) * 2: "erf",
    Fraction(7, 4) * 2: "eqf",
    Fraction(11, 6) * 2: "exf",
    Fraction(15, 8) * 2: "eef",
    Fraction(23, 12) * 2: "etf",
    Fraction(2) * 2: "e",
    Fraction(25, 12) * 2: "ets",
    Fraction(17, 8) * 2: "ees",
    Fraction(13, 6) * 2: "exs",
    Fraction(9, 4) * 2: "eqs",
    Fraction(7, 3) * 2: "ers",
    Fraction(19, 8) * 2: "etes",
    Fraction(29, 12) * 2: "efts",
    Fraction(5, 2) * 2: "f",
    Fraction(31, 12) * 2: "fts",
    Fraction(21, 8) * 2: "fes",
    Fraction(8, 3) * 2: "fxs",
    Fraction(11, 4) * 2: "fqs",
    Fraction(17, 6) * 2: "frs",
    Fraction(23, 8) * 2: "ftes",
    Fraction(35, 12) * 2: "ffts",
    Fraction(3) * 2: "fs",
    Fraction(37, 12) * 2: "gftf",
    Fraction(25, 8) * 2: "gtef",
    Fraction(19, 6) * 2: "grf",
    Fraction(13, 4) * 2: "gqf",
    Fraction(10, 3) * 2: "gxf",
    Fraction(27, 8) * 2: "gef",
    Fraction(41, 12) * 2: "gtf",
    Fraction(7, 2) * 2: "g",
    Fraction(43, 12) * 2: "gts",
    Fraction(29, 8) * 2: "ges",
    Fraction(11, 3) * 2: "gxs",
    Fraction(15, 4) * 2: "gqs",
    Fraction(23, 6) * 2: "grs",
    Fraction(31, 8) * 2: "gtes",
    Fraction(47, 12) * 2: "gfts",
    Fraction(4) * 2: "af",
    Fraction(49, 12) * 2: "aftf",
    Fraction(33, 8) * 2: "atef",
    Fraction(25, 6) * 2: "arf",
    Fraction(17, 4) * 2: "aqf",
    Fraction(13, 3) * 2: "axf",
    Fraction(35, 8) * 2: "aef",
    Fraction(53, 12) * 2: "atf",
    Fraction(9, 2) * 2: "a",
    Fraction(55, 12) * 2: "ats",
    Fraction(37, 8) * 2: "aes",
    Fraction(14, 3) * 2: "axs",
    Fraction(19, 4) * 2: "aqs",
    Fraction(29, 6) * 2: "ars",
    Fraction(39, 8) * 2: "ates",
    Fraction(59, 12) * 2: "afts",
    Fraction(5) * 2: "bf",
    Fraction(61, 12) * 2: "bftf",
    Fraction(41, 8) * 2: "btef",
    Fraction(31, 6) * 2: "brf",
    Fraction(21, 4) * 2: "bqf",
    Fraction(16, 3) * 2: "bxf",
    Fraction(43, 8) * 2: "bef",
    Fraction(65, 12) * 2: "btf",
    Fraction(11, 2) * 2: "b",
    Fraction(67, 12) * 2: "bts",
    Fraction(45, 8) * 2: "bes",
    Fraction(17, 3) * 2: "bxs",
    Fraction(23, 4) * 2: "bqs",
    Fraction(35, 6) * 2: "brs",
    Fraction(47, 8) * 2: "btes",
    Fraction(71, 12) * 2: "bfts",
}

_pitch_class_number_to_pitch_class_name_with_flats = {
    Fraction(0) * 2: "c",
    Fraction(1, 12) * 2: "detf",
    Fraction(1, 8) * 2: "dsef",
    Fraction(1, 6) * 2: "dfxf",
    Fraction(1, 4) * 2: "dtqf",
    Fraction(1, 3) * 2: "dtrf",
    Fraction(3, 8) * 2: "dfef",
    Fraction(5, 12) * 2: "dstf",
    Fraction(1, 2) * 2: "df",
    Fraction(7, 12) * 2: "dftf",
    Fraction(5, 8) * 2: "dtef",
    Fraction(2, 3) * 2: "drf",
    Fraction(3, 4) * 2: "dqf",
    Fraction(5, 6) * 2: "dxf",
    Fraction(7, 8) * 2: "def",
    Fraction(11, 12) * 2: "dtf",
    Fraction(1) * 2: "d",
    Fraction(13, 12) * 2: "eetf",
    Fraction(9, 8) * 2: "esef",
    Fraction(7, 6) * 2: "efxf",
    Fraction(5, 4) * 2: "etqf",
    Fraction(4, 3) * 2: "etrf",
    Fraction(11, 8) * 2: "efef",
    Fraction(17, 12) * 2: "estf",
    Fraction(3, 2) * 2: "ef",
    Fraction(19, 12) * 2: "eftf",
    Fraction(13, 8) * 2: "etef",
    Fraction(5, 3) * 2: "erf",
    Fraction(7, 4) * 2: "eqf",
    Fraction(11, 6) * 2: "exf",
    Fraction(15, 8) * 2: "eef",
    Fraction(23, 12) * 2: "etf",
    Fraction(2) * 2: "e",
    Fraction(25, 12) * 2: "fftf",
    Fraction(17, 8) * 2: "ftef",
    Fraction(13, 6) * 2: "frf",
    Fraction(9, 4) * 2: "fqf",
    Fraction(7, 3) * 2: "fxf",
    Fraction(19, 8) * 2: "fef",
    Fraction(29, 12) * 2: "ftf",
    Fraction(5, 2) * 2: "f",
    Fraction(31, 12) * 2: "getf",
    Fraction(21, 8) * 2: "gsef",
    Fraction(8, 3) * 2: "gfxf",
    Fraction(11, 4) * 2: "gtqf",
    Fraction(17, 6) * 2: "gtrf",
    Fraction(23, 8) * 2: "gfef",
    Fraction(35, 12) * 2: "gstf",
    Fraction(3) * 2: "gf",
    Fraction(37, 12) * 2: "gftf",
    Fraction(25, 8) * 2: "gtef",
    Fraction(19, 6) * 2: "grf",
    Fraction(13, 4) * 2: "gqf",
    Fraction(10, 3) * 2: "gxf",
    Fraction(27, 8) * 2: "gef",
    Fraction(41, 12) * 2: "gtf",
    Fraction(7, 2) * 2: "g",
    Fraction(43, 12) * 2: "aetf",
    Fraction(29, 8) * 2: "asef",
    Fraction(11, 3) * 2: "afxf",
    Fraction(15, 4) * 2: "atqf",
    Fraction(23, 6) * 2: "atrf",
    Fraction(31, 8) * 2: "afef",
    Fraction(47, 12) * 2: "astf",
    Fraction(4) * 2: "af",
    Fraction(49, 12) * 2: "aftf",
    Fraction(33, 8) * 2: "atef",
    Fraction(25, 6) * 2: "arf",
    Fraction(17, 4) * 2: "aqf",
    Fraction(13, 3) * 2: "axf",
    Fraction(35, 8) * 2: "aef",
    Fraction(53, 12) * 2: "atf",
    Fraction(9, 2) * 2: "a",
    Fraction(55, 12) * 2: "betf",
    Fraction(37, 8) * 2: "bsef",
    Fraction(14, 3) * 2: "bfxf",
    Fraction(19, 4) * 2: "btqf",
    Fraction(29, 6) * 2: "btrf",
    Fraction(39, 8) * 2: "bfef",
    Fraction(59, 12) * 2: "bstf",
    Fraction(5) * 2: "bf",
    Fraction(61, 12) * 2: "bftf",
    Fraction(41, 8) * 2: "btef",
    Fraction(31, 6) * 2: "brf",
    Fraction(21, 4) * 2: "bqf",
    Fraction(16, 3) * 2: "bxf",
    Fraction(43, 8) * 2: "bef",
    Fraction(65, 12) * 2: "btf",
    Fraction(11, 2) * 2: "b",
    Fraction(67, 12) * 2: "cftf",
    Fraction(45, 8) * 2: "ctef",
    Fraction(17, 3) * 2: "crf",
    Fraction(23, 4) * 2: "cqf",
    Fraction(35, 6) * 2: "cxf",
    Fraction(47, 8) * 2: "cef",
    Fraction(71, 12) * 2: "ctf",
}

_pitch_class_number_to_pitch_class_name_with_sharps = {
    Fraction(0) * 2: "c",
    Fraction(1, 12) * 2: "cts",
    Fraction(1, 8) * 2: "ces",
    Fraction(1, 6) * 2: "cxs",
    Fraction(1, 4) * 2: "cqs",
    Fraction(1, 3) * 2: "crs",
    Fraction(3, 8) * 2: "ctes",
    Fraction(5, 12) * 2: "cfts",
    Fraction(1, 2) * 2: "cs",
    Fraction(7, 12) * 2: "csts",
    Fraction(5, 8) * 2: "cfes",
    Fraction(2, 3) * 2: "ctrs",
    Fraction(3, 4) * 2: "ctqs",
    Fraction(5, 6) * 2: "cfxs",
    Fraction(7, 8) * 2: "cses",
    Fraction(11, 12) * 2: "cets",
    Fraction(1) * 2: "d",
    Fraction(13, 12) * 2: "dts",
    Fraction(9, 8) * 2: "des",
    Fraction(7, 6) * 2: "dxs",
    Fraction(5, 4) * 2: "dqs",
    Fraction(4, 3) * 2: "drs",
    Fraction(11, 8) * 2: "dtes",
    Fraction(17, 12) * 2: "dfts",
    Fraction(3, 2) * 2: "ds",
    Fraction(19, 12) * 2: "dsts",
    Fraction(13, 8) * 2: "dfes",
    Fraction(5, 3) * 2: "dtrs",
    Fraction(7, 4) * 2: "dtqs",
    Fraction(11, 6) * 2: "dfxs",
    Fraction(15, 8) * 2: "dses",
    Fraction(23, 12) * 2: "dets",
    Fraction(2) * 2: "e",
    Fraction(25, 12) * 2: "ets",
    Fraction(17, 8) * 2: "ees",
    Fraction(13, 6) * 2: "exs",
    Fraction(9, 4) * 2: "eqs",
    Fraction(7, 3) * 2: "ers",
    Fraction(19, 8) * 2: "etes",
    Fraction(29, 12) * 2: "efts",
    Fraction(5, 2) * 2: "f",
    Fraction(31, 12) * 2: "fts",
    Fraction(21, 8) * 2: "fes",
    Fraction(8, 3) * 2: "fxs",
    Fraction(11, 4) * 2: "fqs",
    Fraction(17, 6) * 2: "frs",
    Fraction(23, 8) * 2: "ftes",
    Fraction(35, 12) * 2: "ffts",
    Fraction(3) * 2: "fs",
    Fraction(37, 12) * 2: "fsts",
    Fraction(25, 8) * 2: "ffes",
    Fraction(19, 6) * 2: "ftrs",
    Fraction(13, 4) * 2: "ftqs",
    Fraction(10, 3) * 2: "ffxs",
    Fraction(27, 8) * 2: "fses",
    Fraction(41, 12) * 2: "fets",
    Fraction(7, 2) * 2: "g",
    Fraction(43, 12) * 2: "gts",
    Fraction(29, 8) * 2: "ges",
    Fraction(11, 3) * 2: "gxs",
    Fraction(15, 4) * 2: "gqs",
    Fraction(23, 6) * 2: "grs",
    Fraction(31, 8) * 2: "gtes",
    Fraction(47, 12) * 2: "gfts",
    Fraction(4) * 2: "gs",
    Fraction(49, 12) * 2: "gsts",
    Fraction(33, 8) * 2: "gfes",
    Fraction(25, 6) * 2: "gtrs",
    Fraction(17, 4) * 2: "gtqs",
    Fraction(13, 3) * 2: "gfxs",
    Fraction(35, 8) * 2: "gses",
    Fraction(53, 12) * 2: "gets",
    Fraction(9, 2) * 2: "a",
    Fraction(55, 12) * 2: "ats",
    Fraction(37, 8) * 2: "aes",
    Fraction(14, 3) * 2: "axs",
    Fraction(19, 4) * 2: "aqs",
    Fraction(29, 6) * 2: "ars",
    Fraction(39, 8) * 2: "ates",
    Fraction(59, 12) * 2: "afts",
    Fraction(5) * 2: "as",
    Fraction(61, 12) * 2: "asts",
    Fraction(41, 8) * 2: "afes",
    Fraction(31, 6) * 2: "atrs",
    Fraction(21, 4) * 2: "atqs",
    Fraction(16, 3) * 2: "afxs",
    Fraction(43, 8) * 2: "ases",
    Fraction(65, 12) * 2: "aets",
    Fraction(11, 2) * 2: "b",
    Fraction(67, 12) * 2: "bts",
    Fraction(45, 8) * 2: "bes",
    Fraction(17, 3) * 2: "bxs",
    Fraction(23, 4) * 2: "bqs",
    Fraction(35, 6) * 2: "brs",
    Fraction(47, 8) * 2: "btes",
    Fraction(71, 12) * 2: "bfts",
}

_diatonic_number_and_quality_to_semitones = {
    1: {"d": -1, "P": 0, "A": 1},
    2: {"d": 0, "m": 1, "M": 2, "A": 3},
    3: {"d": 2, "m": 3, "M": 4, "A": 5},
    4: {"d": 4, "P": 5, "A": 6},
    5: {"d": 6, "P": 7, "A": 8},
    6: {"d": 7, "m": 8, "M": 9, "A": 10},
    7: {"d": 9, "m": 10, "M": 11, "A": 12},
    8: {"d": 11, "P": 12, "A": 13},
}

_semitones_to_quality_and_diatonic_number = {
    0: ("P", 1),
    1: ("m", 2),
    2: ("M", 2),
    3: ("m", 3),
    4: ("M", 3),
    5: ("P", 4),
    6: ("d", 5),
    7: ("P", 5),
    8: ("m", 6),
    9: ("M", 6),
    10: ("m", 7),
    11: ("M", 7),
    12: ("P", 8),
}

_quality_abbreviation_to_quality_string = {
    "M": "major",
    "m": "minor",
    "P": "perfect",
    "aug": "augmented",
    "dim": "diminished",
    "A": "augmented",
    "d": "diminished",
}

_quality_string_to_quality_abbreviation = {
    "major": "M",
    "minor": "m",
    "perfect": "P",
    "augmented": "A",
    "diminished": "d",
}

_semitones_to_quality_string_and_number = {
    0: ("perfect", 1),
    1: ("minor", 2),
    2: ("major", 2),
    3: ("minor", 3),
    4: ("major", 3),
    5: ("perfect", 4),
    6: ("diminished", 5),
    7: ("perfect", 5),
    8: ("minor", 6),
    9: ("major", 6),
    10: ("minor", 7),
    11: ("major", 7),
}

_start_punctuation_to_inclusivity_string = {"[": "inclusive", "(": "exclusive"}

_stop_punctuation_to_inclusivity_string = {"]": "inclusive", ")": "exclusive"}

### REGEX ATOMS ###

_integer_regex_atom = r"-?\d+"

_alphabetic_accidental_regex_atom = (
    "(?P<alphabetic_accidental>" "[s]*(qs)?" "|[f]*(qf)?" "|t?q?[fs]" "|" ")"
)

_symbolic_accidental_regex_atom = (
    "(?P<symbolic_accidental>"
    "[#]+[+]?"
    "|[b]+[~]?"
    "|[+]"
    "|[~]"
    "|[3681][2]?[\^_]+"
    "|"
    ")"
)

_ekmelily_accidental_regex_atom = (
    "(?P<ekmelily_accidental>"
    "[fset]?[rxet][fs]"
    "|"
    ")"
)

_octave_number_regex_atom = "(?P<octave_number>{}|)".format(_integer_regex_atom)

_octave_tick_regex_atom = "(?P<octave_tick>" ",+" "|'+" "|" ")"

_diatonic_pc_name_regex_atom = "(?P<diatonic_pc_name>" "[A-Ga-g]" ")"

### REGEX BODIES ###

_comprehensive_accidental_regex_body = (
    "(?P<comprehensive_accidental>{}|{}|{})"
).format(
    _alphabetic_accidental_regex_atom,
    _symbolic_accidental_regex_atom,
    _ekmelily_accidental_regex_atom,
)

_comprehensive_octave_regex_body = ("(?P<comprehensive_octave>{}|{})").format(
    _octave_number_regex_atom, _octave_tick_regex_atom
)

_comprehensive_pitch_class_name_regex_body = (
    "(?P<comprehensive_pitch_class_name>{}{})"
).format(_diatonic_pc_name_regex_atom, _comprehensive_accidental_regex_body)

_comprehensive_pitch_name_regex_body = ("(?P<comprehensive_pitch_name>{}{}{})").format(
    _diatonic_pc_name_regex_atom,
    _comprehensive_accidental_regex_body,
    _comprehensive_octave_regex_body,
)

_pitch_class_name_regex_body = ("(?P<pitch_class_name>{}{})").format(
    _diatonic_pc_name_regex_atom, _alphabetic_accidental_regex_atom
)

_pitch_class_octave_number_regex_body = (
    "(?P<pitch_class_octave_number>{}{}{})"
).format(
    _diatonic_pc_name_regex_atom,
    _comprehensive_accidental_regex_body,
    _octave_number_regex_atom,
)

_pitch_name_regex_body = ("(?P<pitch_name>{}{}{})").format(
    _diatonic_pc_name_regex_atom,
    _alphabetic_accidental_regex_atom,
    _octave_tick_regex_atom,
)

_range_string_regex_body = r"""
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
    """.format(
    _pitch_class_octave_number_regex_body.replace("<", "<us_start_"),
    _pitch_name_regex_body.replace("<", "<ly_start_"),
    _pitch_class_octave_number_regex_body.replace("<", "<us_stop_"),
    _pitch_name_regex_body.replace("<", "<ly_stop_"),
)

_interval_name_abbreviation_regex_body = r"""
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
    """

### REGEX PATTERNS ###

_alphabetic_accidental_regex = re.compile(
    "^{}$".format(_alphabetic_accidental_regex_atom), re.VERBOSE
)

_symbolic_accidental_regex = re.compile(
    "^{}$".format(_symbolic_accidental_regex_atom), re.VERBOSE
)

_comprehensive_accidental_regex = re.compile(
    "^{}$".format(_comprehensive_accidental_regex_body), re.VERBOSE
)

_octave_tick_regex = re.compile("^{}$".format(_octave_tick_regex_atom), re.VERBOSE)

_octave_number_regex = re.compile("^{}$".format(_octave_number_regex_atom), re.VERBOSE)

_diatonic_pc_name_regex = re.compile(
    "^{}$".format(_diatonic_pc_name_regex_atom), re.VERBOSE
)

_comprehensive_accidental_regex = re.compile(
    "^{}$".format(_comprehensive_accidental_regex_body), re.VERBOSE
)

_comprehensive_octave_regex = re.compile(
    "^{}$".format(_comprehensive_octave_regex_body), re.VERBOSE
)

_comprehensive_pitch_class_name_regex = re.compile(
    "^{}$".format(_comprehensive_pitch_class_name_regex_body), re.VERBOSE
)

_comprehensive_pitch_name_regex = re.compile(
    "^{}$".format(_comprehensive_pitch_name_regex_body), re.VERBOSE
)

_pitch_class_name_regex = re.compile(
    "^{}$".format(_pitch_class_name_regex_body), re.VERBOSE
)

_pitch_class_octave_number_regex = re.compile(
    "^{}$".format(_pitch_class_octave_number_regex_body), re.VERBOSE
)

_pitch_name_regex = re.compile("^{}$".format(_pitch_name_regex_body), re.VERBOSE)

_range_string_regex = re.compile("^{}$".format(_range_string_regex_body), re.VERBOSE)

_interval_name_abbreviation_regex = re.compile(
    "^{}$".format(_interval_name_abbreviation_regex_body), re.VERBOSE
)

del re

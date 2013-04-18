from experimental import *


def test_InstrumentEditor_instrument_name_markup_01():
    '''Quit, back & studio all work.
    '''

    studio = scoremanagementtools.studio.Studio()
    studio.run(user_input='example~score~i setup performers hornist horn im q')
    assert studio.ts == (13,)

    studio.run(user_input='example~score~i setup performers hornist horn im b q')
    assert studio.ts == (15, (10, 13))

    studio.run(user_input='example~score~i setup performers hornist horn im studio q')
    assert studio.ts == (15, (0, 13))

from experimental import *


def test_UserInputGetter_where_01():

    studio = scoremanagementtools.studio.Studio()
    studio.run(user_input='example~score~i setup performers move where q')
    assert studio.ts == (11,)

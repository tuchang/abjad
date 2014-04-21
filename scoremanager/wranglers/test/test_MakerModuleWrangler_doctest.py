# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MakerModuleWrangler_doctest_01():
    r'''In library.
    '''

    input_ = 'k pyd q'
    score_manager._run(pending_user_input=input_)
    contents = score_manager._transcript.contents

    strings = [
        'Running doctest ...',
        'testable assets found ...',
        'tests passed in',
        ]
    for string in strings:
        assert string in contents

    
def test_MakerModuleWrangler_doctest_02():
    r'''In score package.
    '''

    input_ = 'red~example~score k pyd q'
    score_manager._run(pending_user_input=input_)
    contents = score_manager._transcript.contents

    strings = [
        'Running doctest ...',
        '1 testable asset found ...',
        'RedExampleScoreTemplate.py OK',
        '0 of 0 tests passed in 1 module.',
        ]
    for string in strings:
        assert string in contents
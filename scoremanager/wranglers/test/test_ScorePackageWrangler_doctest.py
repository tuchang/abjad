# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_ScorePackageWrangler_doctest_01():

    input_ = 'pyd default q'
    score_manager._run(pending_user_input=input_)
    contents = score_manager._transcript.contents

    strings = [
        'Running doctest ...',
        'testable assets found ...',
        'tests passed in',
        ]
    for string in strings:
        assert string in contents
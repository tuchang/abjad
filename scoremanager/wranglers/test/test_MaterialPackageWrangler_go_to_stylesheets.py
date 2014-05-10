# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MaterialPackageWrangler_go_to_stylesheets_01():
    r'''Goes from score materials to score stylesheets.
    '''

    input_ = 'red~example~score m y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Red Example Score (2013) - stylesheets',
        ]
    assert score_manager._transcript.titles == titles


def test_MaterialPackageWrangler_go_to_stylesheets_02():
    r'''Goes from material library to stylesheet library.
    '''

    input_ = 'm y q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Score manager - materials',
        'Score manager - stylesheets',
        ]
    assert score_manager._transcript.titles == titles
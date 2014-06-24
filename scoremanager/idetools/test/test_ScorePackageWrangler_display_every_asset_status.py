# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_ScorePackageWrangler_display_every_asset_status_01():
    r'''Works with all scores.
    '''

    input_ = 'rst* q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    assert 'Repository status for' in contents
    assert '... OK' in contents
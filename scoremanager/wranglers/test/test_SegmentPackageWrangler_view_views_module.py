# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_SegmentPackageWrangler_view_views_module_01():

    input_ = 'g vmro q'
    score_manager._run(pending_user_input=input_)

    assert score_manager._session._attempted_to_open_file
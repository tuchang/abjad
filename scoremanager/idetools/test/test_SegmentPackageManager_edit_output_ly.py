# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageManager_edit_output_ly_01():

    input_ = 'red~example~score g A oe q'
    ide._run(input_=input_)

    assert ide._session._attempted_to_open_file
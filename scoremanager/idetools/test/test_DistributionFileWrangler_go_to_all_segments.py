# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_DistributionFileWrangler_go_to_all_segments_01():
    r'''From score distribution files to all segments.
    '''

    input_ = 'red~example~score d G q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - distribution files',
        'Abjad IDE - segments',
        ]
    assert score_manager._transcript.titles == titles


def test_DistributionFileWrangler_go_to_all_segments_02():
    r'''From all distribution files to all segments.
    '''

    input_ = 'D G q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - distribution files',
        'Abjad IDE - segments',
        ]
    assert score_manager._transcript.titles == titles
from abjad.tools import durationtools
from experimental import quantizationtools


def test_ProxyQEvent___init___01():
    q_event = quantizationtools.PitchedQEvent(130, [0])
    proxy = quantizationtools.ProxyQEvent(q_event, 0.5)
    assert proxy.q_event == q_event
    assert proxy.offset == durationtools.Offset(1, 2)


def test_ProxyQEvent___init___02():
    q_event = quantizationtools.PitchedQEvent(130, [0, 1, 4])
    proxy = quantizationtools.ProxyQEvent(q_event, 100, 1000)
    assert proxy.q_event == q_event
    assert proxy.offset == durationtools.Offset(1, 30)

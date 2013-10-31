# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools.lilypondproxytools import LilyPondGrobOverrideComponentPlugIn


def test_lilypondproxytools_LilyPondGrobOverrideComponentPlugIn___repr___01():
    r'''LilyPond grob override component plug-in repr is evaluable.
    '''

    note = Note("c'4")
    override(note).note_head.color = 'red'

    grob_override_component_plug_in_1 = override(note)
    grob_override_component_plug_in_2 = eval(repr(grob_override_component_plug_in_1))

    assert isinstance(grob_override_component_plug_in_1, LilyPondGrobOverrideComponentPlugIn)
    assert isinstance(grob_override_component_plug_in_2, LilyPondGrobOverrideComponentPlugIn)


def test_lilypondproxytools_LilyPondGrobOverrideComponentPlugIn___repr___02():
    r'''LilyPond grob override component plug-in repr does not truncate override strings.
    '''

    note = Note("c'8")
    override(note).beam.breakable = True
    override(note).note_head.color = 'red'

    assert repr(override(note)) == \
        "LilyPondGrobOverrideComponentPlugIn(beam__breakable=True, note_head__color='red')"

import abjad
import inspect
import pytest


ignored_classes = (
    abjad.String,
    abjad.StorageFormatManager,
    abjad.FormatSpecification,
    )

classes = abjad.documentationtools.list_all_abjad_classes(
    ignored_classes=ignored_classes,
    )


@pytest.mark.parametrize('class_', classes)
def test_abjad___radd___01(class_):
    """
    Classes with __add__ also implement __radd__.
    """
    if inspect.isabstract(class_):
        return
    if hasattr(class_, '__add__'):
        assert hasattr(class_, '__radd__')

import abjad


def test_LilyPondParser__leaves__Rest_01():

    target = abjad.Rest((1, 8))
    parser = abjad.parser.LilyPondParser()
    result = parser("{ %s }" % format(target))
    assert format(target) == format(result[0]) and target is not result[0]

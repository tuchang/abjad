import abjad


def test_scoretools_Parentage__get_spanners_01():
    '''Get spanners in proper parentage.
    '''

    container = abjad.Container("c'8 d'8 e'8 f'8")
    beam = abjad.Beam()
    abjad.attach(abjad.Beam(), container[:])
    slur = abjad.Slur()
    abjad.attach(slur, container[:])
    trill = abjad.TrillSpanner()
    abjad.attach(trill, container[:])

    assert format(container) == abjad.String.normalize(
        r'''
        {
            c'8 [ ( \startTrillSpan
            d'8
            e'8
            f'8 ] ) \stopTrillSpan
        }
        '''
        )

    parentage = abjad.inspect(container[0]).get_parentage()
    spanners = abjad.inspect(parentage).get_spanners()
    spanners == set([beam, slur, trill])
    
    parentage = abjad.inspect(container).get_parentage()
    spanners = abjad.inspect(parentage).get_spanners()
    spanners == set([trill])


def test_scoretools_Parentage__get_spanners_02():
    '''Get spanners in improper parentage.
    '''

    container = abjad.Container("c'8 d'8 e'8 f'8")
    beam = abjad.Beam()
    abjad.attach(beam, container[:])
    slur = abjad.Slur()
    abjad.attach(slur, container[:])
    trill = abjad.TrillSpanner()
    abjad.attach(trill, container[:])

    assert format(container) == abjad.String.normalize(
        r'''
        {
            c'8 [ ( \startTrillSpan
            d'8
            e'8
            f'8 ] ) \stopTrillSpan
        }
        '''
        )

    parentage = abjad.inspect(container).get_parentage(include_self=False)
    assert abjad.inspect(parentage).get_spanners() == set([])

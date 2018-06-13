import abjad
import pickle
from abjad import rhythmtree


def test_RhythmTreeNode_pickle_01():

    string = '(1 (1 (2 (1 1 1)) 2))'
    tree = rhythmtree.RhythmTreeParser()(string)[0]

    pickled = pickle.loads(pickle.dumps(tree))

    assert format(pickled) == format(tree)
    assert pickled != tree
    assert pickled is not tree
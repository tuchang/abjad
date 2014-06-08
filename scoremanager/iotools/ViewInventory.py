from abjad.tools.datastructuretools.TypedOrderedDict import TypedOrderedDict


class ViewInventory(TypedOrderedDict):
    r'''View inventory.

    .. todo:: add examples.
    '''

    ### PRIVATE PROPERTIES ###

    @property
    def _item_callable(self):
        from scoremanager import iotools
        return iotools.View
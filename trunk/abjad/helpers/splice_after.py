from abjad.helpers.assert_components import _assert_components
from abjad.helpers.get_dominant_spanners_receipt import \
   get_dominant_spanners_receipt
from abjad.helpers.get_parent_and_index import _get_parent_and_index


def splice_after(component, new_components):
   '''Splice new_components after component.
      Return list of [component] + new_components.'''

   _assert_components([component])
   _assert_components(new_components)

   parent, index = _get_parent_and_index([component])

   if parent is not None:
      for new_component in reversed(new_components):
         new_component.parentage._switchParentTo(parent)
         parent._music.insert(index + 1, new_component)

   receipt = get_dominant_spanners_receipt([component])

   for spanner, index in receipt:
      for new_component in reversed(new_components):
         spanner._insert(index + 1, new_component)
         new_component.spanners._add(spanner)

   return [component] + new_components

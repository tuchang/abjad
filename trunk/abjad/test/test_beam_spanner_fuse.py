from abjad import *


def test_beam_spanner_fuse_01( ):
   t = Staff([Note(n, (1, 8)) for n in range(8)])
   Beam(t[ : 2])
   Beam(t[2 : 4])
   spanners = t.spanners.get( )
   assert len(spanners) == 2
   left, right = spanners
   assert left.leaves == t[ : 2]
   assert right.leaves == t[2 : 4]
   left.fuse('right')
   spanners = t.spanners.get( )
   assert len(spanners) == 1
   spanner = spanners[0]
   assert spanner.leaves == t[ : 4]


def test_beam_spanner_fuse_02( ):
   t = Staff([Note(n, (1, 8)) for n in range(8)])
   Beam(t[ : 2])
   Beam(t[2 : 4])
   spanners = t.spanners.get( )
   assert len(spanners) == 2
   left, right = spanners
   assert left.leaves == t[ : 2]
   assert right.leaves == t[2 : 4]
   right.fuse('left')
   spanners = t.spanners.get( )
   assert len(spanners) == 1
   spanner = spanners[0]
   assert spanner.leaves == t[ : 4]


def test_beam_spanner_fuse_03( ):
   '''Fusing beyond the first leaf does nothing.'''
   t = Staff([Note(n, (1, 8)) for n in range(8)])
   Beam(t[ : 2])
   Beam(t[2 : 4]) 
   spanners = t.spanners.get( )
   assert len(spanners) == 2
   left, right = spanners
   assert left.leaves == t[ : 2]
   assert right.leaves == t[2 : 4]
   left.fuse('left')
   spanners = t.spanners.get( )
   assert len(spanners) == 2
   left, right = spanners
   assert left.leaves == t[ : 2]
   assert right.leaves == t[2 : 4]


def test_beam_spanner_fuse_04( ):
   '''Fusing *beyond last* leaf does nothing.'''
   t = Staff([Note(n, (1, 8)) for n in range(8)])
   Beam(t[ : 2])
   Beam(t[2 : 4])
   spanners = t.spanners.get( )
   assert len(spanners) == 2
   left, right = spanners
   assert left.leaves == t[ : 2]
   assert right.leaves == t[2 : 4]
   right.fuse('right')
   spanners = t.spanners.get( )
   assert len(spanners) == 2
   left, right = spanners
   assert left.leaves == t[ : 2]
   assert right.leaves == t[2 : 4]

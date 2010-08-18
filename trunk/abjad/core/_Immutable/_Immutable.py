class _Immutable(object):
   '''Base from which immutable custom classes can inherit.
   '''

   ## OVERLOADS ##

   def __copy__(self, *args):
      return type(self)(self)

   __deepcopy__ = __copy__

   def __delattr__(self, *args):
      raise AttributeError('%s objects are immutable.' % self.__class__.__name__)

   def __setattr__(self, *args):
      raise AttributeError('%s objects are immutable.' % self.__class__.__name__)

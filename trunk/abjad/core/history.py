from interface import _Interface

class HistoryInterface(_Interface):

   def __init__(self, client):
      _Interface.__init__(self, client, 'History')

   ### PROPERTIES ###

   def __len__(self):
      return len(self.getAttributeNames( ))

   ### ACCESSORS ###

   def getAttributeNames(self):
      result = [ ]
      for key in self.__dict__.iterkeys( ):
         if not key.startswith('_'):
            result.append(key)
      return result

   def clear(self):
      for item in self.__dict__.iteritems( ):
         self.__dict__.pop(item)

   ### FORMATTING ###

   def __repr__(self):
      if len(self) == 0:
         return 'History( )'
      else:
         return 'History(%s)' % len(self)


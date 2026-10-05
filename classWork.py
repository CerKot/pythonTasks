from collections import UserList

class ourNewList(UserList):
    @classmethod
    def __secret_func(cls):
        print('SECRET')


    def _convert_index(self, i):
        if isinstance(i,slice):
            start = i.start - 1
            stop = i.stop - 1
            return slice(start,stop,i.step)
        if i == 0:
            raise IndexError("не с 0")

        return i - 1 if i>0 else i

    def __getitem__(self, index):
        newIndex = self._convert_index(index)
        return super().__getitem__(newIndex)

    def __setitem__(self, index, value):
        newIndex = self._convert_index(index)
        return super().__setitem__(newIndex,value)

    def __delitem__(self,i ):
        newIndex = self._convert_index(i)
        super().__delitem__(newIndex)

list = ourNewList

lst = list([1,2,3,4,5])

print(lst[-1])
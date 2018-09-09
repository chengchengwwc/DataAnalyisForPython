#!/usr/bin/env python
# -*- coding:utf-8 -*-

class BagInterface(object):

    def __init__(self,souceCollection=None):
        pass

    def isEmpty(self):
        return True
    def __len__(self):
        return 0
    def __str__(self):
        return ""
    def __iter__(self):
        return None
    def __add__(self, other):
        return None
    def __eq__(self, other):
        return False
    def clear(self):
        pass

    def add(self,item):
        pass

    def remove(self,item):
        pass

class Arrary(object):

    def __init__(self,capacity,fillValue=None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value

class ArrayBag(object):

    DEFAULT_CAPACITY = 10

    def __init__(self,sourceCollection=None):
        self._items = Arrary(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._items = Arrary(ArrayBag.DEFAULT_CAPACITY)



    def add(self,item):
        self._items[len(self)] = item
        self._size += 1


    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __str__(self):
        return ",".join(map(str,self))

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True


    def __add__(self, other):
        """
        当python 识别到集合中的in运算符时，它会运行集合类中的__contains__方法
        :param other:
        :return:
        """
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def remove(self,item):
        if not item in self:
            raise KeyError(str(item)+ "not in bag")
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1

        for i in range(targetIndex,len(self)-1):
            self._items[i] = self._items[i+1]
        self._size -=1


if __name__ == "__main__":
    new_page = ArrayBag(range(5))














        
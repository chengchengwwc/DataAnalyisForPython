#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Node(object):

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}-{}".format(self.data,self.next)


class LinkedBag(object):

    def __init__(self,sourceCollection=None):
        self._items = None
        self._size = 0


    def add(self,item):
        self._items = Node(item,self._items)
        self._size += 1

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def clear(self):
        self._size = 0
        self._items = None

    def remove(self,item):
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        self._size -=1






#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
python 数组索引的操作有两个步骤
1 获取数组内存块的基本地址
2 给这个地址加上索引，返回其基本的引用
动态数组占具了连续内存块并支持随机访问

通常 逻辑大小和物理大小会告诉你关于数组状态的几件重要事情
如果逻辑大小为0，数组为空，也就是说，该数组不包含数据项
否则，在任何给定的时间，数组中最后一项的索引都是逻辑大小-1

每次增加数组大小时候，可以通过将数组大小加倍，从而获得一个较为合理时间性能

"""

"""
在数组中插入一项
1 在尝试一次插入或者增加数组的物理大小
2 从数组的逻辑末尾开始，直到目标索引位置，将每一项后移动一个单元
3 将新的项赋值给目标索引位置

"""




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


def add_len_of_list(logicaliszie,old_list):
    if logicaliszie == len(old_list):
        temp = Arrary(len(old_list) + 1)
        for i in range(logicaliszie):
            temp[i] = old_list[i]
        old_list = temp
    return old_list

def insert_in_list(logicaliszie,targetIndex,old_list,new_item):
    for i in range(logicaliszie,targetIndex,-1):
        old_list[i] = old_list[i-1]
    old_list[targetIndex] = new_item
    return old_list


def delete_in_list(logicaliszie,targetIndex,old_list,new_item):
    for i in range(targetIndex,logicaliszie-1):
        old_list[i] = old_list[i+1]
    return old_list

class Grid(object):
    """
    定义的二维数组

    """

    def __init__(self,rows,colums,fillValue=None):
        self._data = Arrary(rows)
        for row in range(rows):
            self._data[row] = Arrary(colums,fillValue)

    def getHeight(self):

        return len(self._data)

    def getWidth(self):

        return len(self._data[0])

    def __getitem__(self, item):
        return self._data[item]

    def __str__(self):
        result = ""
        for row  in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self._data[row][col])
            result += "\n"
        return result



if __name__ == "__main__":
    default_capacity = 5
    logicaliszie = 0
    a = Arrary(default_capacity)
    print (len(a))

    if logicaliszie == len(a):
        temp = Arrary(len(a)+1)
        for i in range(logicaliszie):
            temp[i] = a[i]
        a = temp






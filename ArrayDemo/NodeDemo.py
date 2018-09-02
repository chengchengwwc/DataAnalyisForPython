#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
链表：
一旦找到一个插入点或是删除点，就可以进行插入和删除，而不需要再内存中移动数据项
在每一次插入和删除的过程中，链表结构会调整大小，并不需要额外的内存代价，也不需要复制数据项
"""
class Node(object):

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}-{}".format(self.data,self.next)


if __name__ == "__main__":
    """
    指针head生成了链表结构，这个指针以这样的一种方式操作，最近插入的项目总是位于结构的开始处
    因此当显示数据时，他们会按照和插入时相反的顺序出现
    此外，当显示数据的时候，head指针重新设置为下一个节点，直到head指针变为None,因此，在这个过程中
    节点实际上是从链表中删除，对于程序员来说，节点不再可用，并且会在下一次垃圾回收的时候回收
    """
    head = None
    for count in range(1,6):
        head = Node(count,head)
        #print (head)
    """
    遍历
    """
    while head != None:
        head = head.next

    """
    插入
    """
    newNode = Node(8)
    if head is None:
        head = newNode
    else:
        probe = head
        while probe.next != None:
            probe = probe.next
        probe.next = newNode

    """
    删除最后一项
    """
    removedItem = head.data
    if head.next is None:
        head = None
    else:
        probe = head
        while probe.next.next != None:
            probe = probe.next()
        removedItem = probe.next.data
        probe.next = None
    """
    从任意位置插入节点
    """
    index = 10

    if head is None or index <= 0:
        head = Node(10,head)
    else:
        probe = head
        while probe != None and index > 1:
            probe = probe.next
            index -= 1
        probe.next = Node(10,probe.next)

    """
    从任意位置删除节点
    """
    index = 10

    if index <= 0 or head.next is None:
        removeItem  = head.data
        head = head.next
    else:
        probe = head
        while index > 1 and probe.next.next != None:
            probe = probe.next
            index -= 1
        removeItem = probe.next.data
        probe.next = probe.next.next








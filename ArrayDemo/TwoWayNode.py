#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
双链表结构比单链表结构更具有优越性
1 从给定的节点向左移动一个节点
2 直接移动到最后一个节点
"""

class Node(object):

    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class TwoWayNode(Node):

    def __init__(self,data,previous=None,next=None):
        Node.__init__(self,data,next)
        self.previous = previous


head = TwoWayNode(1)
tail = head

for data in range(2,6):
    tail.next = TwoWayNode(data,tail)
    tail = tail.next

probe = tail
while probe != None:
    print (probe.data)
    probe = probe.previous




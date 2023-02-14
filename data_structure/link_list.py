# -*- encoding: utf-8 -*-
'''
@File    :   link_list.py
@Time    :   2023/02/14 22:53:06
@Author  :   ufy
@Contact :   antarm@outlook.com
@Version :   v1.0
@Desc    :   None
'''

# here put the import lib

from typing import Iterable


class ListNode:
    def __init__(self, e, next=None) -> None:
        self.element = e
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def create(self, datas: Iterable):
        '''根据一个可迭代对象,生成一个LinkedList对象。'''
        cur = self.head
        for e in datas:
            node = ListNode(e)
            if cur == None:
                self.head = node
            else:
                cur.next = node
            cur = node
            self.count += 1

    def add_first(self, e) -> None:
        '''在链表头添加元素e'''
        node = ListNode(e)
        node.next = self.head
        self.head = node
        self.count += 1

    def insert(self, i, e) -> None:
        '''在linkedList的第i个位置,插入元素e.'''
        assert i >= 0 and i <= self.count, "i的取值范围为[0,len],且i为整数."
        if i == 0:
            self.add_first(e)
        else:
            cur = self.head
            while i > 0:
                cur = cur.next
                i -= 1
            node = ListNode(e, next=None)
            node.next = cur.next
            cur.next = node
        self.count += 1

    def delete(self, i) -> ListNode:
        '''删除linkedList的第i个位置的元素,并返回该节点的值.'''
        assert i >= 0 and i < self.count, "i的取值范围为[0,len),且i为整数."
        cur = self.head
        if i == 0:
            self.head = cur.next
            out = cur
        else:
            while i - 1 > 0:
                cur = cur.next
                i -= 1
            out = cur.next
            cur.next = out.next

        return out.element

    def get(self, i) -> ListNode:
        '''返回linkedList的第i个位置的节点的值'''
        assert i >= 0 and i < self.count, "i的取值范围为[0,len),且i为整数."
        cur = self.head

        while i > 0:
            cur = cur.next
            i -= 1

        return cur.element

    def set(self, i, e) -> None:
        assert i >= 0 and i < self.count, "i的取值范围为[0,len),且i为整数."
        cur = self.head

        while i > 0:
            cur = cur.next
            i -= 1

        cur.element = e

    def __str__(self) -> str:
        cur = self.head
        datas = []
        while cur:
            datas.append(cur.element)
            cur = cur.next
        out = '[' + '->'.join(datas) + ']'
        return out

    def __repr__(self) -> str:
        cur = self.head
        datas = []
        while cur:
            datas.append(cur.element)
            cur = cur.next
        out = '[' + ','.join(datas) + ']'
        return out
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

from requests import delete


#-----------------------------------------------------------------------------------------
# single linked list
#-----------------------------------------------------------------------------------------
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
        assert i >= 0 and i <= self.count, f"i的取值范围为[0,{len(self)}],且i为整数."
        if i == 0:
            self.add_first(e)
        else:
            cur = self.head
            node = ListNode(e, next=None)
            while i - 1 > 0 and cur.next:
                cur = cur.next
                i -= 1
            if i - 1 > 0:
                cur.next.next = node
            else:
                node.next = cur.next
                cur.next = node
            self.count += 1

    def delete(self, i):
        '''删除linkedList的第i个位置的元素,并返回该节点的值.'''
        assert i >= 0 and i < self.count, f"i的取值范围为[0,{len(self)}),且i为整数."
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

        self.count -= 1
        return out.element

    def get(self, i):
        '''返回linkedList的第i个位置的节点的值'''
        assert i >= 0 and i < self.count, "i的取值范围为[0,{len(self)}),且i为整数."
        cur = self.head

        while i > 0:
            cur = cur.next
            i -= 1
        return cur.element

    def set(self, i, e) -> None:
        assert i >= 0 and i < self.count, "i的取值范围为[0,{len(self)}),且i为整数."
        cur = self.head

        while i > 0:
            cur = cur.next
            i -= 1

        cur.element = e

    def __str__(self) -> str:
        cur = self.head
        datas = []
        while cur:
            datas.append(str(cur.element))
            cur = cur.next
        out = '[' + ' -> '.join(datas) + ']'
        return out

    def __repr__(self) -> str:
        cur = self.head
        datas = []
        while cur:
            datas.append(str(cur.element))
            cur = cur.next
        out = '[' + ','.join(datas) + ']'
        return out

    def __len__(self):
        return self.count


#-----------------------------------------------------------------------------------------
# doublle linked list
#-----------------------------------------------------------------------------------------
class ListNode2Direction:

    def __init__(self, element=None, prior=None, next=None) -> None:
        self.element = element
        self.prior = prior
        self.next = next


class DoubleLinkedList(LinkedList):

    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def create(self, datas: Iterable):
        cur = None
        for e in datas:
            node = ListNode2Direction(element=e)
            if self.head == None:
                self.head = node
                cur = self.head
            else:
                cur.next = node
                node.prior = cur
                cur = node
            self.count += 1

    def add_first(self, e):
        node = ListNode2Direction(element=e)
        if self.head == None:
            self.head = None
        else:
            node.next = self.head
            self.head.prior = node
            self.head = node
        self.count += 1

    def insert(self, i, e):
        """在DoubleLinkedList的第i个位置插入节点(e)"""
        assert i >= 0 and i <= self.count, f"i的取值范围为[0,{len(self)}],且i为整数."
        if i == 0:
            self.add_first(e=e)
        else:
            cur = self.head
            while i - 1 > 0:
                cur = cur.next
                i -= 1
            node = ListNode2Direction(element=e)
            node.prior = cur
            node.next = cur.next
            cur.next = node
        self.count += 1

    def delete(self, i):
        '''删除linkedList的第i个位置的元素,并返回该节点的值.'''
        assert i >= 0 and i < self.count, f"i的取值范围为[0,{len(self)}),且i为整数."
        cur = self.head
        if i == 0:
            self.head = cur.next
            self.head.prior = None
            out = cur
        else:
            while i - 1 > 0:
                cur = cur.next
                i -= 1
            out = cur.next
            cur.next = cur.next.next
            if cur.next:
                cur.next.prior = cur
        self.count -= 1
        return out.element

    def __str__(self) -> str:
        cur = self.head
        datas = []
        while cur:
            datas.append(str(cur.element))
            cur = cur.next
        out = '[' + ' <-> '.join(datas) + ']'
        return out

    def __repr__(self) -> str:
        return str(self)

    def __len__(self):
        return self.count
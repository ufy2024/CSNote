# -*- encoding: utf-8 -*-
'''
@File    :   stack.py
@Time    :   2023/02/17 10:29:39
@Author  :   ufy
@Contact :   antarm@outlook.com
@Version :   v1.0
@Desc    :   None
'''
# here put the import lib
from data_structure.link_list import LinkedList


class Stack:

    def __init__(self) -> None:
        self.data: list = []

    def push(self, e):
        self.data.append(e)

    def pop(self):
        self.data.pop()

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "[" + ",".join(self.data) + ">"

    def __repr__(self) -> str:
        return str(self.data)


class LinkStack:

    def __init__(self) -> None:
        self.data = LinkedList()

    def pop(self, ):
        return self.data.delete(i=self.data.count)

    def push(self, e):
        self.data.insert(i=self.data.count, e=e)

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "[" + ",".join(self.data) + ">"

    def __repr__(self) -> str:
        return str(self.data)

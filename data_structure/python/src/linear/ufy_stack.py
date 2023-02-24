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

from src.linear.ufy_link_list import LinkedList
from src.utils.ufy_exception import Empty


class Stack:

    def __init__(self) -> None:
        self.data: list = []

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if len(self.data):
            return self.data.pop()
        else:
            raise Empty("栈空")

    def top(self):
        if len(self.data):
            return self.data[-1]
        else:
            raise Empty("栈空")

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "[" + ",".join(map(lambda x: str(x), self.data)) + ">"

    def __repr__(self) -> str:
        return str(self.data)


class LinkStack:

    def __init__(self) -> None:
        self.data = LinkedList()

    def push(self, e):
        self.data.insert(i=self.data.count, e=e)

    def pop(self, ):
        if len(self.data):
            return self.data.delete(i=self.data.count - 1)
        else:
            raise Empty("栈空")

    def top(self):
        if len(self.data):
            return self.data.get(i=self.data.count - 1)
        else:
            raise Empty("栈空")

    def __len__(self):
        return len(self.data)

    def __str__(self):
        data = []
        cur = self.data.head
        while cur:
            data.append(str(cur.element))
            cur = cur.next
        return "[" + ",".join(data) + ">"

    def __repr__(self) -> str:
        return str(self.data)

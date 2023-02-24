# -*- encoding: utf-8 -*-
'''
@File    :   queue.py
@Time    :   2023/02/21 16:28:44
@Author  :   ufy
@Contact :   antarm@outlook.com
@Version :   v1.0
@Desc    :   None
'''
# here put the import lib

from ufy_link_list import LinkedList
from utils.ufy_exception import Empty


class Queue:

    def __init__(self) -> None:
        self.data: list = []

    def first(self):
        if len(self.data):
            return self.data[0]
        else:
            raise Empty("队列为空")

    def last(self):
        if len(self.data):
            return self.data[-1]
        else:
            raise Empty("队列为空")

    def enqueue(self, e):
        self.data.append(e)

    def dequeue(self):
        if len(self.data):
            return self.data.pop(0)
        else:
            raise Empty("队列为空")

    def __str__(self) -> str:
        return "<" + "<-".join(map(lambda x: str(x), self.data)) + "<"

    def __repr__(self) -> str:
        return "<" + ",".join(map(lambda x: str(x), self.data)) + "<"

    def __len__(self):
        return len(self.data)


class LinkQueue:

    def __init__(self) -> None:
        self.data = LinkedList()

    def first(self):
        if len(self.data):
            return self.data.get(0)
        else:
            raise Empty("队列为空")

    def last(self):
        if len(self.data):
            return self.data.get(len(self.data) - 1)
        else:
            raise Empty("队列为空")

    def enqueue(self, e):
        self.data.insert(i=len(self), e=e)

    def dequeue(self):
        if len(self.data):
            return self.data.delete(i=0)
        else:
            raise Empty("队列为空")

    def __str__(self) -> str:
        return "<" + "<-".join(map(lambda x: str(x), self.data)) + "<"

    def __repr__(self) -> str:
        return "<" + ",".join(map(lambda x: str(x), self.data)) + "<"

    def __len__(self):
        return len(self.data)
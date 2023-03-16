from inspect import stack

from ufy.linear import linklist, stack

if __name__ == '__main__':
    a = [i for i in range(10)]
    l = linklist.LinkedList()
    for i in a:
        l.add_first(i)
    print(l)
    s = stack.Stack()
    for i in a:
        s.push(i)
    print(s)

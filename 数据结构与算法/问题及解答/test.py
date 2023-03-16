from ufy.linear import linklist

if __name__ == '__main__':
    a = [i for i in range(10)]
    l = linklist.LinkedList()
    for i in a:
        l.add_first(1)
    print(l)
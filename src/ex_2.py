import logging
import math
import os


def lastcall(func):
    def wrapper(*args):
        if not os.path.exists('{}.log'.format(func.__name__)):
            f = open('{}.log'.format(func.__name__), 'w+')
            f.close()
        with open('{}.log'.format(func.__name__), 'r') as file:
            line = ""
            for line in file:
                pass
            lastLine = line
        if str(args) in lastLine:
            print("I'm already told you that the answer is "+str(func(*args))+"!")
            return
        with open('{}.log'.format(func.__name__), 'w') as file:
            file.write(str(args))
        print(func(*args))
    return wrapper

@lastcall
def f(num: int):
    return num**2

@lastcall
def g(x: float, y: float):
    return math.log2(x)+y**3


class List(list):
    
    def __init__(self, myList):
        super().__init__(myList)

    def __getitem__(self, *args):
        if isinstance(args[0], int):
            return super(List, self).__getitem__(args[0])
        result = super(List, self).__getitem__(args[0][0])
        for i in range(1, len(args[0])):
            result = result[args[0][i]]
        return result

















if __name__ == '__main__':
    f(3)
    f(3)
    f(3)
    f(4)
    f(4)
    g(5.9, 8)
    g(8.5, 7)
    g(8.5, 7)
    g(5.9, 8)

    mylist = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ]
    )

    print(mylist[0, 1, 3])
    print(mylist[2, 0, 2])
    print(mylist[1, 1])
    print(mylist[0])







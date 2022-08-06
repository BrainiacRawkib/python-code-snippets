from collections import deque


stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print(stack)


# Stack --- LIFO

class Stack:
    def __init__(self):
        self.container = deque()
        # self.container = []

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def values(self):
        return [i for i in self.container]

    def __str__(self):
        return f'{self.__class__.values(self)}'


if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print(s)
    print(s.peek())
    print(s.pop())
    print(s.size())
    print(s)
    print(s.is_empty())

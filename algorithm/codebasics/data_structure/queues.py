from collections import deque


# Queue ---- FIFO

class Queue:
    def __init__(self):
        self.container = deque()
        # self.container = []  # not recommended to use because of dynamic array

    # def insert(self, value):
    #     self.container.insert(0, value)

    def insert(self, value):
        self.container.appendleft(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def values(self):
        return [i for i in self.container]

    def __getitem__(self, item):
        try:
            return self.container[item]
        except IndexError:
            return IndexError('Index out of range')

    def __len__(self):
        return len(self.container)

    def __str__(self):
        return f'{self.__class__.__name__} --> {self.__class__.values(self)}'


if __name__ == '__main__':
    q = Queue()
    q.insert(12)
    q.insert(13)
    q.insert(14)
    q.insert(15)
    q.insert(16)

    print(q)
    print(q.values())
    print(q.peek())
    print('pop --->', q.pop())
    print('container --->', q.container)
    print(q)
    print(len(q))
    print(q[4])

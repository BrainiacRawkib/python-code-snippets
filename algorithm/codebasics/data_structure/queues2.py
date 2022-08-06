from collections import deque


class Queue:
    
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def values(self):
        return [i for i in self.buffer]

    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

    def __str__(self):
        return f'{self.__class__.__name__} --> {self.__class__.values(self)}'


if __name__ == '__main__':
    q = Queue()
    dict_1 = {'ticker': 'AAPL', 'price': 123.90, 'timestamp': '15 Apr 2022'}
    dict_2 = {'ticker': 'GOOGL', 'price': 125.90, 'timestamp': '15 Apr 2022'}
    dict_3 = {'ticker': 'HLNT', 'price': 1000.90, 'timestamp': '15 Apr 2027'}
    dict_4 = {'ticker': 'MSFT', 'price': 150.90, 'timestamp': '15 Apr 2022'}
    q.enqueue(dict_1)
    q.enqueue(dict_2)
    q.enqueue(dict_3)
    q.enqueue(dict_4)

    print(q)
    print(q.peek())
    print('pop --->', q.dequeue())
    print(q)

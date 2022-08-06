def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t['march 6'] = 130
t['march 1'] = 20

print(t['march 1'])
print(t['march 6'])

print(t.arr)

del t['march 1']
print(t.arr)

if __name__ == '__main__':
    pass

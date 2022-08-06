class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_(self):
        if self.head is None:
            print('Empty Lined list.')
            return
        iterator = self.head
        llstr = ''

        while iterator:
            llstr += str(iterator.data) + '---->'
            iterator = iterator.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        iterator = self.head

        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception(f'Index [{index}] out of range!')
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception(f'Index [{index}] out of range!')

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(90)
    # ll.insert_at_beginning(50)
    # ll.insert_at_end(99)
    # ll.insert_at_end(100)
    # ll.insert_at_end(200)
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.print_()
    ll.remove_at(2)
    ll.print_()
    # ll.remove_at(20)
    # ll.print_()
    ll.insert_at(0, 'jackfruit')
    ll.print_()
    ll.insert_at(3, 'grapefruit')
    ll.print_()
    print(ll.get_length())

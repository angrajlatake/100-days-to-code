import time


class Minheap:

    def __init__(self):
        self.list = []

    def findmin(self):
        pass

    def swap(self, data, swap_data):
        parent_index = self.list.index(swap_data)
        parent_data = self.list[parent_index]
        self.list[self.list.index(data)] = parent_data
        self.list[parent_index] = data

    def del_swap(self):
        min_data = self.list[0]

        self.list[0] = self.list[(len(self.list) - 1)]
        self.list[(len(self.list) - 1)] = min_data
        self.list.pop(len(self.list) - 1)
        return self.list[0]

    def del_align(self, data):

        swap_data = 0
        if self.list[self.child_left(data)] < self.list[self.child_right(data)]:

            swap_data = self.list[self.child_left(data)]

        else:
            swap_data = self.list[self.child_right(data)]
        print(f" swap data = {swap_data}")
        return swap_data

    def parentindex(self, data):
        return self.list.index(data) // 2

    def child_right(self, data):
        index = self.list.index(data)
        if index == 0:
            return index + 2
        index = ((index) * 2) + 1
        if index >= len(self.list):
            return
        return index

    def child_left(self, data):
        index = self.list.index(data)
        if index == 0:
            return index + 1
        index = (index * 2) + 1
        if index >= len(self.list):
            return
        return index

    def insert_key(self, data):
        self.list.append(data)
        while self.list.index(data) != 0 and data < self.list[self.parentindex(data)]:
            self.swap(data, self.list[self.parentindex(data)])

    def deletemin(self):
        data = self.del_swap()
        while data > self.list[self.child_right(data)] and data > self.list[self.child_left(data)]:
            self.swap(data, self.del_align(data))
            self.print_heap()

    def print_heap(self):
        print(self.list)


list = []
heap = Minheap()

heap.insert_key(2)
heap.insert_key(5)
heap.insert_key(6)
heap.insert_key(1)
heap.insert_key(3)
heap.insert_key(0)
heap.insert_key(4)
heap.insert_key(7)

print("original heap")
heap.print_heap()

print("deleted heap")
heap.deletemin()

heap.print_heap()

class Minheap:

    def __init__(self):
        self.tree = []
        self.tree.append("None")



    def insert_key(self, data):
        self.tree.append(data)
        curr = len(self.tree) - 1

        while curr > 1 and self.tree[curr] < self.tree[curr//2]:
            temp = self.tree[curr//2]
            self.tree[curr//2] = self.tree[curr]
            self.tree[curr] = temp
            curr = curr//2
    def swap(self,curr,side):
        temp = self.tree[side]
        self.tree[side] = self.tree[curr]
        self.tree[curr] = temp
        curr = side

    def deletemin(self):
        last = len(self.tree) - 1
        self.tree[1] = self.tree[last]
        self.tree.pop(last)

        last -= 1
        curr = 1
        while curr <= last:
            left = 2*curr
            right = 2*curr+1
            if right <= last:
                if self.tree[left] < self.tree[right]:
                    if self.tree[curr] > self.tree[left]:
                        temp = self.tree[left]
                        self.tree[left] = self.tree[curr]
                        self.tree[curr] = temp
                        curr = left
                    else:
                        break
                else:
                    if self.tree[curr] > self.tree[right]:
                        temp = self.tree[right]
                        self.tree[right] = self.tree[curr]
                        self.tree[curr] = temp
                        curr = right
                    else:
                        break
            elif left <= last:
                if self.tree[curr] > self.tree[left]:
                    temp = self.tree[left]
                    self.tree[left] = self.tree[curr]
                    self.tree[curr] = temp
                    curr = left
                else:
                    break
            else:
                break


    def print_heap(self):
        print(self.tree)


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

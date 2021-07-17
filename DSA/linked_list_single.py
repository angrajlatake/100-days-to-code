
class Node:
    def __str__(self):
        return 'Data = {}, Next = {}'.format(self.data, self.next )

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            itr = self.head
            while (itr.next != None):
                itr = itr.next
            itr.next = Node(data)
        self.size += 1

    def printList(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next

    def find(self, x):
        itr = self.head
        while itr is not None:
            if itr.data == x:
                return True
            itr = itr.next
        return False

    def insert(self, data, pos):
        curr = self.head
        prv = None
        i = 0
        if pos == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        while i < pos and curr is not None:
            prv = curr
            curr = curr.next
            i += 1

        if i == pos:
            new_node = Node(data)
            prv.next = new_node
            new_node.next = curr

    def delete(self, pos):
        curr = self.head
        prev = None

        if pos == 0:
            if curr is None:
                return
            self.head = curr.next
            return

        i = 0
        while i < pos and curr is None:
            prv = curr
            curr = curr.next
            i += 1
        if curr is None:
            prv.next = curr.next


class LinkedListRecursive:
    def __init__(self):
        self.head = None
        self.size = 0

    def __appendInternal(self, data, currNode):
        if currNode is None:
            currNode = Node(data)
            return currNode
        nextNode = self.__appendInternal(data, currNode.next)
        currNode.next = nextNode
        return currNode

    def __printList(self, currNode):
        if currNode is None:
            return
        print(currNode.data)
        self.__printList(currNode.next)

    def __find(self, x, currNode):
        if currNode is None:
            return False
        if currNode.data == x:
            return True
        return self.__find(x, currNode.next)

    def append(self, data):
        self.head = self.__appendInternal(data, self.head)

    def printList(self):
        self.__printList(self.head)

    def find(self, x):
        return self.__find(x, self.head)

    def reverse_list(self):
        prev = None
        curr = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


list = LinkedList()

list.insert(11, 0)
list.append(1)
list.append(5)
list.append(6)
list.insert(3, 2)
list.insert(10, 0)
list.delete(6)

list2 = LinkedListRecursive()
list2.append(1)
list2.append(5)
list2.append(1)
list2.append(4)
list2.append(6)
list2.append(9)


list2.printList()

print(list2.find(11))
print("linked list")
list2.printList()
list2.reverse_list()
print("reverse linked list")
list2.printList()
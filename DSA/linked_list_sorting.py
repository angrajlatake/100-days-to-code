class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = Node(data)
            self.size +=1

    def print(self):
        itr = self.head
        while itr!= None:
            print(itr.data)
            itr = itr.next

    def find(self,x):
        itr = self.head
        while itr.next != None:
            if itr.data ==x:
                return True
            itr= itr.next
        return False

    def insert(self,pos,data):
        curr = self.head
        prv = None
        if pos == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size +=1
        else:
            i = 0
            while i < pos and curr != None:
                prv = curr
                curr = curr.next
                i+1
            if i == pos:
                new_node = Node(data)
                prv.next = new_node
                new_node.next = curr
                self.size +=1
    def delete(self,pos):
        curr = self.head
        prv = None

        if pos == 0:
            if curr == None:
                return
            self.head = curr.next
            return
        i = 0
        while i < pos and curr != None:
            prv = curr
            curr= curr.next
            i+=1
        if curr != None:
            prv.next = curr.next

    def appendList(self, list):
        curr = self.head
        prv = None
        if self.head == None:
            self.head = list.head
            return
        while curr != None:
            prv = curr
            curr = curr.next
        prv.next = list.head



list = LinkedList()

list.append(3)
list.append(4)
list.append(7)
list.append(9)


list2 = LinkedList()
list2.append(3)
list2.append(4)
list2.append(7)
list2.append(9)

list.appendList(list2)

list.print()
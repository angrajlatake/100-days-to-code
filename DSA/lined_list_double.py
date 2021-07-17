class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.last = None
    # def __append(self,data, currNode):
    #     if currNode is None:
    #         currNode = Node(data)
    #
    #         return currNode
    #     next_node = self.__append(data, currNode.next)
    #     currNode.next = next_node
    #     return currNode
    # def append(self,data):
    #     self.head = self.__append(data, self.head)

    def append(self,data):

        if self.head is None:
            self.head = Node(data)
            self.head.prev = None
            self.head.next = None
            self.last = self.head
        else:

            new_node = Node(data)
            curr = self.last
            curr.next = new_node
            new_node.prev = curr
            self.last = new_node
            new_node.next = None

    def __printlist(self,currNode):
        if currNode is None:
            return
        print(f"{currNode.data} -->")
        self.__printlist(currNode.next)

    def printlist(self):
        curr = self.head
        printstring = ""
        if curr is None:
            return
        while curr is not None:
            printstring += str(curr.data) + "<==>"
            curr = curr.next
        print(printstring)

    def printlast(self):
        print(self.last.data)

    def insert(self,data, pos):
        print("started the function")
        curr = self.head
        newnode = Node(data)
        print("new node created")
        if pos == 0:
            print("pos 0")
            newnode.next = curr
            curr.prev = newnode
            self.head = newnode

        else:
            print("running insert else")
            i = 0
            while i < pos:
                curr = curr.next
                i+=1
            prev = curr.prev

            prev.next = newnode
            newnode.prev = prev
            newnode.next = curr
            curr.prev = newnode

    def find(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return curr
            curr= curr.next

    def printnodeinfo(self,data):
        node = self.find(data)
        print(f"Node data = {node.data}")
        print(f"Node prev = {node.prev.data}")
        print(f"Node next = {node.next.data}")

    def del_node(self,data):
        node = self.find(data)
        if node.data == self.head.data:
            next = node.next
            next.prev = None
            node.next = None
            self.head = next

        elif node.data == self.last.data:
            prev = node.prev
            node.prev = None
            prev.next = None
            self.last = prev

        else:
            prev = node.prev
            next = node.next
            node.prev = None
            node.next = None
            prev.next = next
            next.prev = prev

dll = DoubleLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
dll.append(60)
dll.append(70)
dll.append(80)
dll.append(90)

dll.printlist()

dll.printlast()
dll.printnodeinfo(40)
dll.insert(35, 3)
dll.printlist()

dll.printnodeinfo(35)

dll.del_node(35)

dll.printlist()
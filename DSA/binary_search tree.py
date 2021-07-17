
value = 0


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class binary_search_tree:

    def __init__(self):
        self.__root = None


    def insert(self, data):
        newNode = Node(data)
        curr = self.__root
        parent = None

        if self.__root is None:
            self.__root = newNode
            return

        while curr is not None:
            if data > curr.data:
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left

        if data > parent.data:
            parent.right = newNode
        else:
            parent.left = newNode

    def find(self, data):
        curr = self.__root

        while curr != None:
            if curr.data == data:
                return True
            elif data <= curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if curr == None:
            return False

    def find_position(self, data):
        curr = self.__root
        parent = None

        while curr != None:
            if curr.data == data:
                return parent, curr
            elif data <= curr.data:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right

    def __inorder_print(self,root):
        if root is None:
            return
        self.__inorder_print(root.left)
        print(root.data)
        self.__inorder_print(root.right)

    def inorder_print(self):
        self.__inorder_print(self.__root)

    def __preorderprint(self, root):
        if root == None:
            return
        print(root.data)
        self.__preorderprint(root.left)
        self.__preorderprint(root.right)

    def preorderprint(self):
        self.__preorderprint(self.__root)

    def min(self):
        curr = self.__root

        while curr.left != None:
            curr = curr.left
        return curr.data

    def max(self):
        curr = self.__root

        while curr.right != None:
            curr = curr.right
        return curr.data

    def deleteNode(self, data):
        assignednode = None

        prv = None

        parent, delNode = self.find_position(data)

        if delNode.right is not None and delNode.left is not None:
            curr = delNode.right
            prv = delNode
            while curr.left is not None:
                prv = curr
                curr = curr.left

            assignednode = curr
            if parent is not None and parent.left.data == delNode.data:
                parent.left = assignednode
            elif parent is not None and parent.right.data == delNode.data:
                parent.right = assignednode

            if prv.data == delNode.data:
                prv.right = None
            else:
                prv.left = None

            assignednode.left = delNode.left
            assignednode.right = delNode.right

            delNode.left = None
            delNode.right = None

        elif delNode.right is None and delNode.left is None:
            if parent.left.data == delNode.data:
                parent.left = None
            else:
                parent.right = None

        elif delNode.right is None:
            curr = delNode.left
            while curr.right is not None:
                prv = curr
                curr = curr.right
            assignednode = curr
            parent.right = assignednode
            assignednode.left = delNode.left
            prv.right = None

        else:
            curr = delNode.right
            while curr.left is not None:
                curr = curr.left
            assignednode = curr
            parent.left = assignednode
            assignednode.right = delNode.right
            prv.left = None

    def del_replace(self, parent_node, node, empty_side, other_side):
        prv = None
        curr = node.other_side
        assignednode = None

        while curr.empty_side is not None:
            prv = curr
            curr = curr.empty_side
        assignednode = curr
        parent_node.empty_side = assignednode

        assignednode.other_side = node.other_side
        prv.empty_side = None

    def __greater_tree(self, root):
        global value


        if root is None:
            return

        self.__greater_tree(root.right)
        root.data +=value
        value = root.data
        print(f"value{value}")
        self.__greater_tree(root.left)


    def greater_tree(self):

        self.__greater_tree(self.__root)
        return self.__root



arr = [15, 13, 3, 1, 8, 14, 36, 27, 18, 18, 16, 17, 17, 20, 21, 21, 28, 40]
bst = binary_search_tree()

for i in arr:
    bst.insert(i)

print("In_order\n")
bst.inorder_print()
print ("preorder\n")
bst.preorderprint()

print(f"Min Node in this tree :{bst.min()}")

print(f"Max Node in this tree :{bst.max()}")
print("greater_tree")
bst.greater_tree()
print ("preorder Greater_tree\n")
bst.preorderprint()
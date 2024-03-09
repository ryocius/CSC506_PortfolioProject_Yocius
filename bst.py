class BstNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # Comparable methods
    # Equals (=)
    def __eq__(self, otherData):
        if not isinstance(otherData, BstNode):
            return NotImplemented

        return self.data == otherData.data

    # Less Than (<)
    def __lt__(self, otherData):
        if not isinstance(otherData, BstNode):
            return NotImplemented

        return self.data < otherData.data

    # Less than or equal to (<=)
    def __le__(self, otherData):
        if not isinstance(otherData, BstNode):
            return NotImplemented

        return self.data <= otherData.data

    # Greater than (>)
    def __gt__(self, otherData):
        if not isinstance(otherData, BstNode):
            return NotImplemented

        return self.data > otherData.data

    # Greater than or equal to (>+)
    def __ge__(self, otherData):
        if not isinstance(otherData, BstNode):
            return NotImplemented

        return self.data >= otherData.data

    # Print
    def __repr__(self):
        lines = []
        if self.rightChild:
            found = False
            for line in repr(self.rightChild).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.data))
        if self.leftChild:
            found = False
            for line in repr(self.leftChild).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class Tree:
    def __init__(self, inArray):
        self.root = self.build_tree(inArray)

    def build_tree(self, inArray):
        return self.__build_tree_recurs(inArray, 0, len(inArray) - 1)

    def __build_tree_recurs(self, inArray, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = BstNode(inArray[mid])
        node.leftChild = self.__build_tree_recurs(inArray, start, mid - 1)
        node.rightChild = self.__build_tree_recurs(inArray, mid + 1, end)
        return node

    def insert(self, data):
        self.root = self.__insertHelper(self.root, data)

    def __insertHelper(self, root, data):
        if root is None:
            return BstNode(data)
        else:
            if data < root.data:
                root.leftChild = self.__insertHelper(root.leftChild, data)
            else:
                root.rightChild = self.__insertHelper(root.rightChild, data)
        return root


    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.leftChild = self.delete(root.leftChild, data)
        elif data > root.data:
            root.rightChild = self.delete(root.rightChild, data)
        else:
            if root.leftChild is None:
                temp = root.rightChild
                return temp
            elif root.rightChild is None:
                temp = root.left
                return temp

            temp = self.__min_val_node(root.rightChild)
            root.data = temp.data
            root.rightChild = self.delete(root.rightChild, temp.data)

        self.__rebalance()
        return root

    def search(self, data):
        return self.__searchHelper(self.root, data)

    def __searchHelper(self, root, data):
        if root is None or root.data == data:
            return root

        if root.data < data:
            return self.__searchHelper(root.rightChild, data)

        return self.__searchHelper(root.leftChild, data)

    def __min_val_node(self, node):
        current = node
        while current.leftChild is not None:
            current = current.leftChild
        return current

    def __rebalance(self):
        sorted = self.__inorder_traversal(self.root)
        self.root = self.__build_tree_recurs(sorted, 0, len(sorted) - 1)

    def __inorder_traversal(self, node):
        if node is None:
            return []
        return self.__inorder_traversal(node.leftChild) + [node.data] + self.__inorder_traversal(node.rightChild)

    def printSorted(self):
        out = self.__inorder_traversal(self.root)
        print(out)

    def __repr__(self):
        print()
        return repr(self.root)
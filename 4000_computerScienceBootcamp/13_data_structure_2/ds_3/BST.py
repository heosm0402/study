from binary_tree import *

class BST:
    def __init__(self):
        self.root = None


    def get_root(self):
        return self.root


    def preorder_traverse(self, cur, f):
        if not cur:
            return

        f(cur.data)
        self.preorder_traverse(cur.left, f)
        self.preorder_traverse(cur.right, f)


    def insert(self, data):
        new_node = TreeNode()
        new_node.data = data

        cur = self.root

        if cur == None:
            self.root = new_node
            return

        while True:
            parent = cur

            if cur.data > data:
                cur = cur.left

                if not cur:
                    parent.left = new_node
                    return
            else:
                cur = cur.right

                if not cur:
                    parent.right = new_node
                    return

    def search(self, data):
        cur = self.root

        while cur:
            if data == cur.data:
                return cur
            elif cur.data > data:
                cur = cur.left
            elif cur.data < data:
                cur = cur.right

        return cur


    def remove(self, target):
        self.root, removed_node = slef.__remove_recursion(self.root, target)
        removed_node.left = removed_node.right = None

        return removed_node

    def __remove_recursion(self, cur, target):

        if cur == None:
            return None, None
        elif target < cur.data:
            cur.left, rem_node = self.__remove_recursion(cur.left, target)
        elif target > cur.data:
            cur.left, rem_node = self.__remove_recursion(cur.right, target)
        else:
            if not cur.left and not cur.right:
                rem_node = cur
                cur = None
            elif not cur.left:
                rem_node = cur
                cur = cur.left
            elif not cur.right:
                rem_node = cur
                cur = cur.right
            else:
                replace = cur.left
                while replace.right:
                    replace = replace.right

                cur.data, replace.data = replace.data, cur.data
                cur.left, rem_node = self.__remove_recursion(cur.left, replace.data)

        return cur, rem_node
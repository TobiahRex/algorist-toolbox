from typing import Type, TypeVar, Tuple
from collections import deque as Queue

class TreeNode:
    def __init__(self, value: any):
        self.value = value
        self.left = None
        self.right = None

    def level_order_traversal(self):
        print('\nlevel-order')
        q = Queue([self])
        while q:
            level_nodes = []
            for i in range(0, len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_nodes.append(node.value)
            print(level_nodes)

    def pre_order_traversal(self, root=None, results=[]):
        if root is None:
            root = self
        stack = [root]
        while stack:
            node = stack.pop()
            results.append(node.value)
            [stack.append(n) for n in (node.right, node.left) if n]
        print('pre-order: ', results)
        return results

    def in_order_traversal(self, root=None, results=[]):
        if root is None:
            root = self
        stack = []
        node = root
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                results.append(node.value)
                node = node.right
            else:
                break
        print('in-order: ', results)
        return results

    def post_order_traversal(self, root=None):
        if not root:
            root = self
        results = []
        pre = None
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                if root.right is None or root.right is pre:
                    results.append(stack.pop().value)
                    pre = root
                    root = None
                else:
                    root = root.right
        print('post-order: ', results)
        return results

BST = TypeVar('BST', bound='BST')
class BST:
    def __init__(self, *args, **kwargs):
        self.root = self.create(**kwargs)

    def create(self, *args, **kwargs):
        root = None
        if kwargs.get('sorted'):
            root = self.__create_from_sorted_list(kwargs.get('values'))
        else:
            root = self.__sort_and_create(kwargs.get('values'))
        return root

    def __create_from_sorted_list(self, values):
        root = TreeNode(values[0])
        q = Queue()
        q.append(root)
        i = 0
        while q:
            node = q.popleft()
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(values):
                node.left = TreeNode(values[li])
                q.append(node.left)
            if ri < len(values):
                node.right = TreeNode(values[ri])
                q.append(node.right)
            i += 1
        return root

    def __sort_and_create(self, values):
        root = None
        for v in values:
            root, added = self.insert(root, v)
            if not added:
                return root
        root
        return root

    @staticmethod
    def build(values, sorted=False):
        return BST(
            values=values,
            sorted=sorted)

    def insert(self, root=None, value=None) -> Tuple[BST, bool]:
        new_node = TreeNode(value)
        if not root:
            return new_node, True
        current = root
        parent = root
        while current:
            parent = current
            if new_node.value == current.value:
                return root, False  # Already exists: can't have duplicates
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right
        if parent.value < new_node.value:
            parent.right = new_node
        else:
            parent.left = new_node
        return root, True


if __name__ == '__main__':
    bst = BST.build(values=[1, 2, 3, 4, 5, 6, 7], sorted=True)
    bst.root.level_order_traversal()
    bst.root.pre_order_traversal()
    bst.root.in_order_traversal()
    bst.root.post_order_traversal()
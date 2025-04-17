import sys

sys.setrecursionlimit(1 << 21)

class Node:
    __slots__ = ['left', 'right', 'parent', 'size', 'value']

    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.value = value

    def update_size(self):
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size


def rotate_left(node):
    child = node.right
    if not child:
        return

    node.right = child.left
    if child.left:
        child.left.parent = node
    child.left = node
    child.parent = node.parent

    if node.parent:
        if node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child

    node.parent = child
    Node.update_size(node)
    Node.update_size(child)


def rotate_right(node):
    child = node.left
    if not child:
        return

    node.left = child.right
    if child.right:
        child.right.parent = node
    child.right = node
    child.parent = node.parent

    if node.parent:
        if node.parent.left == node:
            node.parent.left = child
        else:
            node.parent.right = child

    node.parent = child
    Node.update_size(node)
    Node.update_size(child)


def splay(node):
    while node.parent:
        parent = node.parent
        grandparent = parent.parent

        if not grandparent:
            # single rotation
            if parent.left == node:
                rotate_right(parent)  # Zig
            else:
                rotate_left(parent)  # Zag
        else:
            if grandparent.left == parent:
                if parent.left == node:
                    # Zig-zig case
                    rotate_right(grandparent)
                    rotate_right(parent)
                else:
                    # Zig-zag
                    rotate_left(parent)
                    rotate_right(grandparent)
            else:
                if parent.right == node:
                    # Zag-zag
                    rotate_left(grandparent)
                    rotate_left(parent)
                else:
                    # Zag-zig
                    rotate_right(parent)
                    rotate_left(grandparent)
    return node


def find(node, pos):
    if not node:
        return None

    current = node
    while True:
        left_size = current.left.size if current.left else 0
        if pos < left_size:
            current = current.left
        else:
            pos -= left_size
            if pos == 0:
                break
            pos -= 1
            current = current.right
        if not current:
            break

    if current:
        splay(current)
    return current


def split(root, pos):
    if pos == 0:
        return (None, root)
    if pos >= root.size:
        return (root, None)

    node = find(root, pos)
    left = node.left
    if left:
        left.parent = None
    node.left = None
    Node.update_size(node)
    return (left, node)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    left_end = left
    while left_end.right:
        left_end = left_end.right

    splay(left_end)
    left_end.right = right
    right.parent = left_end
    Node.update_size(left_end)
    return left_end


def build_tree(s):
    root = None
    for c in s:
        node = Node(c)
        root = merge(root, node)
    return root


def in_order(root):
    res = []
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.value)
        current = current.right
    return ''.join(res)


def main():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()
        n = int(f.readline())
        queries = [tuple(map(int, f.readline().split())) for _ in range(n)]

    root = build_tree(s)

    for i, j, k in queries:
        left_part, temp = split(root, i)
        mid_part, right_part = split(temp, j - i + 1)

        root = merge(left_part, right_part)

        left_new, right_new = split(root, k)

        root = merge(merge(left_new, mid_part), right_new)

    with open('output.txt', 'w') as f:
        f.write(in_order(root) + '\n')


if __name__ == "__main__":
    main()
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

def find_path(root, path, k):
    if root is None:
        return False
    path.append(root.val)
    if root.val == k:
        return True
    if ((root.left and find_path(root.left, path, k)) or
            (root.right and find_path(root.right, path, k))):
        return True
    path.pop()
    return False

def find_lca(root, n1, n2):
    path1 = []
    path2 = []
    if (not find_path(root, path1, n1) or not find_path(root, path2, n2)):
        return -1
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

# Example usage:
nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_tree(nodes)
n1 = 5
n2 = 4
print(find_lca(root, n1, n2))


        
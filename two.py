class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min_value(root):
    if root is None:
        return None
    
    while root.left is not None:
        root = root.left
    
    return root.val

# Приклад використання:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

print("Найменше значення у дереві:", find_min_value(root))

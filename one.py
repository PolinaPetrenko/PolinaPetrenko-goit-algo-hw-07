class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max_value(root):
    if root is None:
        return None
    
    while root.right is not None:
        root = root.right
    
    return root.val

# Приклад використання:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

print("Найбільше значення у дереві:", find_max_value(root))

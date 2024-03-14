class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_of_values(root):
    if root is None:
        return 0
    
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)

# Приклад використання:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)

print("Сума всіх значень у дереві:", sum_of_values(root))

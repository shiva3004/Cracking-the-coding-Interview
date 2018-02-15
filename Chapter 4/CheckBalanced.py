class tree_node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
def is_balanced(root):
  return check_height(root) != -1
  
def check_height(root):
  if root is None:
    return 0
  left_tree_height = check_height(root.left)
  if left_tree_height == -1:
    return -1
  right_tree_height = check_height(root.right)
  if  right_tree_height == -1:
    return -1
  if abs(left_tree_height - right_tree_height) > 1:
    return -1
  return max(left_tree_height, right_tree_height) + 1
  
a = tree_node("a")
b = tree_node("b")
c = tree_node("c")
d = tree_node("d")
e = tree_node("e")
f = tree_node("f")
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
print(is_balanced(a))

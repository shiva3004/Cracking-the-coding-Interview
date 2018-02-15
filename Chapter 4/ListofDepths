class tree_node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class list_of_depths:
  def __init__(self):
    self.current = []
    self.parents = []
    self.result = []
    
  def create_list_of_depths(self, root):
    if root is None:
      return root
    self.current.append(root)
    while len(self.current) > 0:
      self.result.append(self.current)
      self.parents = self.current  # the previous current list will become the parent list and use that
      self.current = []           # to go to the children nodes while adding them to current list
      for parent in self.parents:
        if parent.left is not None:
          self.current.append(parent.left)
        if parent.right is not None:
          self.current.append(parent.right)
    return self.result
  
tree_list = list_of_depths()
a = tree_node(1)
b = tree_node(6)
c = tree_node(7)
d = tree_node(4)
e = tree_node(5)
f = tree_node(2)
g = tree_node(3)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f
d.right = g

l = tree_list.create_list_of_depths(a)

for each in l:
  for another_each in each:
    print(another_each.val)
    

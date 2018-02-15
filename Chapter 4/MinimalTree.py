class tree_node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
def create_binary_search_tree(arr):
  return create_bst(arr, 0, len(arr)-1)
  
def create_bst(arr, start, end):
  if start > end:
    return None
  middle = (start + end) // 2
  root = tree_node(arr[middle])
  root.left = create_bst(arr, start, middle-1)
  root.right = create_bst(arr, middle+1, end)
  return root
  
arr1 = [2,4,5,6,7,9,10,12]
root = create_binary_search_tree(arr1)
print(root.val)
print(root.left.val)
print(root.right.val)

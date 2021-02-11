class Bst:
  def __init__(self, head=None):
    self.root = head

  def insert(self, value):
    #This is where you will insert a value into the Binary Search Tree
    cur = self.root
    node = Node(value)
    if cur is None:
      self.root = node
      return
    else:
      while cur is not None:
        prev = cur
        if value > cur.value:
          cur = cur.left
          to_left = True
        elif value < cur.value:
          cur = cur.right
          to_left = False
        else:
          print('Already exists')
      if to_left:
        prev.left = node
      else:
        prev.right = node

  def contains(self, value):
    # this is where you'll search the BST and return TRUE or FALSE if the value exists in the BST
    cur = self.root
    if cur is None:
      return False
    else:
      while cur is not None:
        if cur.value == value:
          return True
        elif value > cur.value:
          cur = cur.left
        else:
          cur = cur.right
      return False
    

  def remove(self, root, value):
    # this is where you will remove a value from the BST
    if not root: 
      return root
    if root.val > value: 
      root.left = remove(root.left, value)
    elif root.val < value: 
      root.right= remove(root.right, value)
    else:
      if not root.right:
        return root.left
      if not root.left:
        return root.right
      
      temp_val = root.right
      mini_val = temp_val.val
      while temp_val.left:
        temp_val = temp_val.left
        mini_val = temp_val.val
      root.right = remove(root.right,root.val)
    return root



# ----- Node ------
class Node:
  # store your DATA and LEFT and RIGHT values here
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


bst = Bst(Node(50))
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(bst.contains(70))
print(bst.contains(44))
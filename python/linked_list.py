class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, head=None):
    self.head = head
    self.length = 0

  def add(self, data):
    # write your code to ADD an element to the Linked List
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next is not None:
        cur = cur.next
      cur.next = new_node
    self.length += 1

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    cur = self.head
    if cur.value == data:
      self.head = cur.next
    else:
      prev = self.head
      cur = cur.next
      while cur is not None:
        if cur.value == data:
          prev.next = cur.next
          break
        prev = cur
        cur = cur.next
    self.length -= 1
    

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    cur = self.head
    while cur is not None:
      if cur.value == element_to_get:
        return cur
      cur = cur.next
    return

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  def __init__(self, value):
    self.next = None
    self.value = value

ll = LinkList()
ll.add(1)
ll.add(2)
ll.add(3)

print(ll.head)
print(ll.head.value)
print(ll.head.next.value)
print(ll.head.next.next.value)
print(ll.length)

ll.remove(3)

print(ll.head.value)
print(ll.head.next.value)
print(ll.length)


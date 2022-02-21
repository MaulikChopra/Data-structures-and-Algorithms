class Node:
  def __init__(self, value=None, next=None):
    self.value=value
    self.next=next
class linkedlist:
  #creating the node and head
  def __init__(self, value=None, next=None):
    self.value=value
    self.next=next

  def insert(self, value):
    node=linkedlist(value, None) # initialize the node
    p = node
    p.next=node.next
    p = p.next # the pointer of newly added node goes to location of last node.
     # the head now gets assigned the value of node

    # initilize the node and add the value to it
    # the pointer of node ie next is assigned to the value assigned to self.head
    # now self.head gets assigned the value of then new node added.

  def print(self):
    list=""

    while self is not None:
      list += str(self.value) + "-->"
      self= self.next
    print(list + "None")

l=linkedlist()
for i in range(0,9):
  l.insert(i)
l.print()


#REVERSE LINKED LIST
def reverse_list(list):
  pointer = list.head
  
  while pointer is not None:
    node=Node(list.value, list.next)
    node.next.head = list.head  
    pointer = pointer.next

  
#reverse_list(l)
print(l
)
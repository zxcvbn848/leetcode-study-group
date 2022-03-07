
class ListNode:
   def __init__(self, data):
      self.data = data
      self.next = None

   def printList(node):
      while node:
         print(node.data, end = " ")
         node = node.next

   def linkNode(node, nextNode):
      node.next = nextNode

class Partition:
   def beforeAfter(node, x):
      beforeStart = None
      beforeEnd   = None
      afterStart  = None
      afterEnd    = None

      # Partition list
      while node:
         next      = node.next
         node.next = None

         if node.data < x:
            # Insert node into end of before list
            if (beforeStart == None):
               beforeStart = node
               beforeEnd   = beforeStart
            else:
               beforeEnd.next = node # Insert node at end of before list
               beforeEnd      = node # set beforeEnd to new node
         else:
            # Insert node into end of after list
            if (afterStart == None):
               afterStart = node
               afterEnd   = afterStart
            else:
               afterEnd.next = node # Insert node at end of after list
               afterEnd      = node # set afterEnd to new node

         node = next

      if beforeStart == None:
         return afterStart

      # Merge before list and after list
      beforeEnd.next = afterStart

      return beforeStart

   def headTail(node, x):
      head = node
      tail = node

      while node:
         next = node.next

         if node.data < x:
            # Insert node at head
            node.next = head
            head      = node
         else:
            # Insert node at tail
            tail.next = node
            tail      = node
         
         node = next
      
      tail.next = None

      # The head has changed, so we need to return it
      return head

linkedList = [ListNode(3), ListNode(5), ListNode(8), ListNode(5), ListNode(10), ListNode(2), ListNode(1)]

for i in range(len(linkedList) - 1):
   linkedList[i].next = linkedList[i + 1]

result1 = ListNode.printList(Partition.beforeAfter(linkedList[0], 5))
print(result1)

result2 = ListNode.printList(Partition.headTail(linkedList[0], 5))
print(result2)

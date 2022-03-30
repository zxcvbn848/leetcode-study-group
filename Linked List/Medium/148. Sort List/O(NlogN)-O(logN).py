# Sorting visual: https://visualgo.net/en/sorting?slide=1

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

	def printList(node):
		while node:
			print(node.val, end = " ")
			node = node.next

	def linkNode(node, nextNode):
		node.next = nextNode

class Solution:
	def sortList(self, head):
		if not head or not head.next:
			return head
		
		mid = self.getMid(head)
		left = self.sortList(head)
		right = self.sortList(mid)

		return self.merge(left, right)

	def merge(self, left, right):
		dummyHead = ListNode(None)
		tail = dummyHead

		while left and right:
			if left.val < right.val:
				tail.next = left
				left = left.next
				tail = tail.next
			else:
				tail.next = right
				right = right.next
				tail = tail.next
		# 把剩下的部分接起來
		tail.next = left if left else right

		return dummyHead.next

	def getMid(self, head):
		midPrev = None

		while head and head.next:
			midPrev = midPrev.next if midPrev else head
			head = head.next.next

		mid = midPrev.next
		midPrev.next = None

		return mid

linkedList = [ListNode(3), ListNode(5), ListNode(8), ListNode(5), ListNode(10), ListNode(2), ListNode(1)]

for i in range(len(linkedList) - 1):
   linkedList[i].next = linkedList[i + 1]

result1 = ListNode.printList(Solution().sortList(linkedList[0]))
print(result1)
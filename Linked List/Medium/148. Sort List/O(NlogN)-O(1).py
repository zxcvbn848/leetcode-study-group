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

# 參考來源：https://leetcode.com/problems/sort-list/discuss/111266/you-should-use-bottom-up-merge-sort-to-solve-this-with-python-sample-code
class Solution(object):
	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		if not head or not head.next:
			return head

		n = self.getSize(head)

		# create a dummy node before `head`
		dummyHead = ListNode(None)
		dummyHead.next = head

		prev = dummyHead
		groupSize = 1

		while groupSize < n:
			while True:
				print("prev:", prev.val)
				firstEnd = self.subGroup(prev.next, groupSize)

				# TODO: delete
				if firstEnd:
					print("firstEnd: ", firstEnd.val)
					# print("\n")
					# print("first: ")
					# ListNode.printList(firstEnd)
					# print("\n")
				
				if not firstEnd:
					break
				secondEnd = self.subGroup(firstEnd.next, groupSize)

				# TODO: delete
				if secondEnd:
					print("secondEnd: ", secondEnd.val)
					# print("\n")
					# print("second: ")
					# ListNode.printList(secondEnd)
					# print("\n")
				
				if not secondEnd:
					break
				prev = self.mergeGroup(prev, firstEnd, secondEnd)

			# reset to the start of the list
			prev = dummyHead
			head = prev.next

			groupSize *= 2

		return head

	@staticmethod
	def getSize(head):
		'''
		Get the size of the linked list.
		'''
		n = 0
		while head:
			n += 1
			head = head.next
		return n

	@staticmethod
	def subGroup(head, n):
		'''
		Group the top n elements of the linked list. This method doesn't
		actually cut the list, but instead returns the first n-th element
		or the last element.
		'''
		if not head:
			return None

		for _ in range(0, n - 1):
			if head.next:
				head = head.next
			else:
				break

		return head

	@staticmethod
	def mergeGroup(before, firstEnd, secondEnd):
		'''
		Merge two groups (first, second) with order (smaller first). This method
		returns the last element of the merged group.

		before: pointer to the last element before the first group
		firstEnd: pointer to the last element of the first group
		secondEnd: pointer to the last element of the second group
		'''
		try:
			first, second = before.next, firstEnd.next
			while (first is not second) and (second is not secondEnd.next):
				if not secondEnd:
					# the `secondEnd.next` statement in the while loop is
					# evaluated only once at the beginning, therefore it will
					# not throw an AttributeError when secondEnd becomes None
					# later
					break

				if first.val > second.val:
					if second is secondEnd:
						# after moving the current node, the second group
						# will be empty
						secondEnd = None
					# move the node pointed by `second` to before `first`
					before.next = second # before -> second
					before = before.next # (old before) -> new before (old second) -> first
					second = second.next # (old before) -> new before  (old second) -X-> new second  (old first)
					before.next = first # (old before) -> new before  (old second) -O-> new second  (old first)
					firstEnd.next = second # firstEnd -> new second (old first)
				else:
					# just move the `first` (and `before`) pointer forward
					before, first = first, first.next

		except AttributeError:
			# initially at least `second` is None
			pass

		# return the last element
		return secondEnd if secondEnd else firstEnd

linkedList = [ListNode(3), ListNode(5), ListNode(8),  ListNode(10), ListNode(2), ListNode(1)]

for i in range(len(linkedList) - 1):
	linkedList[i].next = linkedList[i + 1]

result1 = ListNode.printList(Solution().sortList(linkedList[0]))
print(result1)
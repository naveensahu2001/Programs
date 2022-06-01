class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:

	def __init__(self):
		self.head = Node("head")
		self.size = 0

	def __str__(self):
		cur = self.head.next
		out = ""
		while cur:
			out += str(cur.value) + "->"
			cur = cur.next
		return out[:-3]


	def getSize(self):
		return self.size


	def isEmpty(self):
		return self.size == 0


	def peeking(self):


		if self.isEmpty():
			raise Exception("Peeking from an empty stack")
		return self.head.next.value


	def pushing(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1


	def popping(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value


if __name__ == "__main__":
	stack = Stack()
	for i in range(0, 11):
		stack.pushing(i)
	print(f"Stack: {stack}")

	for _ in range(1, 6):
		remove = stack.popping()
		print(f"Pop: {remove}")
	print(f"Stack: {stack}")
	peep=stack.peeking()
	print(f"Peep:{peep}")

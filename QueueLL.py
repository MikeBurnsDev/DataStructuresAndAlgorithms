from LinkedListNode import LinkedListNode

class QueueLL:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, value):
		node = LinkedListNode(value)
		if(self.head==None):
			self.head = self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def dequeue(self):
		node = self.head
		self.head = self.head.next
		node.next = None
		return node.value

	def empty(self):
		return self.head == None
	
	@staticmethod
	def test():
		#Linked List Based Queue Tests
		queueLL = QueueLL()
	
		assert queueLL.empty
	
		queueLL.enqueue(0)
		queueLL.enqueue(1)
		queueLL.enqueue(2)
	
		assert queueLL.dequeue() == 0
	
		assert not queueLL.empty()
	
		assert queueLL.dequeue() == 1
		assert queueLL.dequeue() == 2
	
		assert queueLL.empty
	
		print("Linked List Based Queue implementation tests passed.")
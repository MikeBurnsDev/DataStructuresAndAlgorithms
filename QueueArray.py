class QueueArray:
	def __init__(self,length=10):
		self.head = 0
		self.tail = 0
		self.isFull = False
		self.array = [None]*length

	def enqueue(self, value):
		self.array[self.tail] = value		

		self.tail += 1
		if(self.tail == len(self.array)):
			self.tail = 0

		self.isFull = (self.tail == self.head) and not self.isFull

	def dequeue(self):
		value = self.array[self.head]

		self.array[self.head] = None

		self.head += 1
		if(self.head == len(self.array)):
			self.head = 0

		self.isFull = (self.tail == self.head) and self.isFull

		return value

	def empty(self):
		return self.head == self.tail and not self.isFull

	def full(self):
		return self.isFull
	
	@staticmethod
	def test():
		queueArray = QueueArray(3)

		assert queueArray.empty()
		assert not queueArray.full()

		queueArray.enqueue(0)
		queueArray.enqueue(1)
		queueArray.enqueue(2)

		assert not queueArray.empty()
		assert queueArray.full()
		assert queueArray.dequeue() == 0

		queueArray.enqueue(4)

		assert queueArray.dequeue() == 1
		assert queueArray.dequeue() == 2
		assert queueArray.dequeue() == 4

		assert queueArray.empty()

		print("Array Based Queue implementation tests passed.")
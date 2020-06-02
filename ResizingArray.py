#Python arrays are already resizable but this is just for conceptual practice.
class ResizingArray:
	def __init__(self, initSize=0):
		self.array = []
		self.lastIndex = -1

	def __len__(self):
		return self.len()

	def __getitem__(self, index):
		return self.get(index)

	def __setitem__(self, index, element):
		return self.set(index,element)

	def __repr__(self):
		return str(self.array)

	def __str__(self):
		printStr = "["
		for i in range(self.lastIndex+1):
			elemStr = '\'' + str(self.array[i]) + '\''
			if(type(self.array[i])!=str):
				elemStr = elemStr[1:-1]
			printStr += elemStr + ","
		return printStr[:-1] + "]"

	def len(self):
		return self.lastIndex+1

	def push(self, element):
		if(self.lastIndex+1 >= len(self.array)):
			oldArr = self.array
			self.array = [None]*(self.lastIndex+1)*2
			if(self.lastIndex+1==0):
				self.array = [element]
				self.lastIndex = 0
				return self.array

			for oldElemIndex in range(len(oldArr)):
				self.array[oldElemIndex] = oldArr[oldElemIndex]

		self.lastIndex += 1
		self.array[self.lastIndex] = element

		return self.array

	def pop(self):
		if(self.lastIndex == 0):
			raise ValueError('ResizingArray is empty, can\'t pop')

		elem = self.array[self.lastIndex]
		self.array[self.lastIndex] = None
		self.lastIndex -= 1
		return elem

	def get(self, index):
		if(type(index) != int):
			raise ValueError('ResizingArrays index param must be an int')		
		if(index<0 or index>self.lastIndex):
			raise IndexError('Invalid index supplied for ResizingArrays get')

		return self.array[index]

	def set(self, index, element):
		if(type(index) != int):
			raise ValueError('ResizingArrays index param must be an int')		
		if(index<0 or index>self.lastIndex):
			raise IndexError('Invalid index supplied for ResizingArrays set')

		self.array[index] = element

	def internalSize(self):
		return len(self.array)
	
	@staticmethod
	def test():
		vector = ResizingArray()
		assert len(vector) == 0
		assert vector.internalSize() == 0

		vector.push('test')
		assert vector[0] == 'test'

		vector.push('another test')
		assert vector[1] == 'another test'

		vector.push('one more test')
		assert vector.internalSize() == 4
		assert len(vector) == 3

		vector[1] = 'different test'
		assert vector[1] == 'different test'

		assert vector.pop() == 'one more test'

		assert len(vector) == 2

		lol = str(vector)
		assert str(vector) == "['test','different test']"

		print("Resizing Array implementation tests passed.")    
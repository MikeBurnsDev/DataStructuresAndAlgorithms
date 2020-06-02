from LinkedListNode import LinkedListNode

class LinkedList:
	def __init__(self, root=None):
		self.root = root

	def __getitem__(self, index):
		return self.get(index)

	def __setitem__(self, index, element):
		return self.set(index,element)

	def __len__(self):
		return self.size()

	def __iter__(self):
		self.iteratorCurrentNode = self.root
		return self

	def __next__(self):
		if(self.iteratorCurrentNode==None):
			raise StopIteration
		else:
			self.iteratorCurrentNode = self.iteratorCurrentNode.next
			return self.iteratorCurrentNode

	def __repr__(self):
		return self.printAll()

	def __str__(self):
		return self.printAll()

	def printAll(self):
		printString = ""
		nextNode = self.root

		if(nextNode==None):
			return printString

		while(nextNode!=None):
			printString += nextNode.print() + ", "
			nextNode = nextNode.next

		return printString[:-2]

	def size(self):
		node = self.root
		if(node==None):
			return 0

		numNodes = 1
		while(node.next !=None):
			node = node.next
			numNodes+=1

		return numNodes

	def empty(self):
		return self.root==None

	def set(self,index,element):
		newNode = LinkedListNode(element)
		if(index>0):
			prevNode = self.get(index-1)
		newNode.next = prevNode.next.next
		prevNode.next = newNode
		prevNode.next.next = None

	def get(self,index):
		node = self.root
		if(node==None):
			return None

		count=0
		while(True):
			if(index==count or node==None):
				return node	
			node = node.next
			count+=1

		return None

	def push_front(self,element):
		newRoot = LinkedListNode(element)
		oldRoot = self.root
		self.root = newRoot
		newRoot.next = oldRoot

	def push_back(self,element):
		newNode = LinkedListNode(element)

		if(self.root==None):
			self.root = newNode
			return newNode

		self.back().next = newNode
		return newNode

	def pop_front(self):
		oldRoot = self.root

		if(oldRoot == None):
			return oldRoot

		if(oldRoot.next == None):
			self.root = None
			return oldRoot

		self.root = oldRoot.next
		oldRoot.next = None
		return oldRoot

	def pop_back(self):
		node = self.root

		if(node == None):
			return node

		if(node.next == None):
			self.root = None
			return node

		while(node.next.next != None):
			node = node.next

		backNode = node.next
		node.next = None
		return backNode

	def front(self):
		return self.root

	def back(self):
		node = self.root
		if(node == None):
			return None

		while(node.next != None):
			node = node.next

		return node

	def insert(self,index,element):
		newNode = LinkedListNode(element)
		if(index==0):
			self.push_front(newNode)
		else:
			prevNode = self.get(index-1)
			newNode.next = prevNode.next
			prevNode.next = newNode

		return newNode

	def erase(self,index):
		if(index==0):
			self.root = None

		prevElement = self.get(index-1)
		if(prevElement.next.next != None):
			prevElement.next = prevElement.next.next

	def value_n_from_end(self,n):
		#returns the value of the node at nth position from the end of the list
		return self.get(self.size()-n)

	def reverse(self):
		prevNode = None
		currentNode = self.root
		cachedNextNode = None

		while(currentNode != None):
			cachedNextNode = currentNode.next
			currentNode.next = prevNode
			prevNode = currentNode
			currentNode = cachedNextNode

		self.root = prevNode

		return self

	def remove_value(self,value):
		node = self.root
		prevNode = None

		while(node!=None):
			if(node.value == value):
				prevNode.next = node.next
				node.next = None
				return True
			prevNode = node
			node = node.next

		return False
	
	@staticmethod
	def test():
		linkedList = LinkedList()

		assert linkedList.back() == None
		assert linkedList.front() == None
		assert linkedList.empty() == True

		linkedList.push_back(0)

		assert linkedList.get(0).value == 0	
		assert linkedList[0].value == 0
		assert linkedList.back().value == 0
		assert linkedList.front().value == 0
		assert linkedList.empty() == False

		linkedList.push_back(2)
		linkedList.push_back(3)
		linkedList.push_front(1)

		assert linkedList.get(3).value == 3
		assert linkedList[3].value == 3
		assert linkedList.back().value == 3
		assert linkedList.front().value == 1

		linkedList.reverse()

		assert linkedList.pop_back().value == 1
		assert linkedList.pop_front().value == 3
		assert len(linkedList) == 2

		linkedList.insert(1,4)
		assert linkedList[1].value == 4

		assert linkedList.remove_value(4) == True
		assert linkedList.remove_value(4) == False

		print("Linked List implementation tests passed.")
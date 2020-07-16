from BinaryTreeNode import BinaryTreeNode as BtNode

class BinarySearchTree:
	def __init__(self):
		self.head = None

	def insert(self, value):
		parent = self.get_parent(value)
		
		if(parent == None):
			self.head = BtNode(value)
		elif(parent.value < value):
			parent.right = BtNode(value)
		else:
			parent.left = BtNode(value)
		
	#helper method to make inserting many values easier	
	def insertArray(self, arr):
		for val in arr:
			self.insert(val)

	def get_count(self, node=None):
		numNodes = 0

		if(node==None):
			node=self.head

		if(node!=None):
			numNodes += 1
			if(node.left!=None):
				numNodes+=self.get_count(node.left)
			if(node.right!=None):
				numNodes+=self.get_count(node.right)

		return numNodes

	def to_string(self, node=None):
		if(node==None):
			node=self.head
		if(node==None):
			return ""

		printStr = ""

		if(node!=None):
			if(node.left!=None):
				printStr += self.to_string(node.left) + ", "
				
			printStr += node.print() + ", "
				
			if(node.right!=None):
				printStr += self.to_string(node.right) + ", "
			
		return printStr[:-2]
	
	def print(self):
		print(self.to_string())
	
	def contains(self, value):
		return self.get_node(value) != None
	
	def height(self, node=None):
		leftHeight = rightHeight = 0
		
		if(node==None):
			node=self.head
			leftHeight = rightHeight = 1
		
		
		if(node!=None):
			if(node.left!=None):
				leftHeight+=self.height(node.left) + 1
			if(node.right!=None):
				rightHeight+=self.height(node.right) + 1

		return max(leftHeight,rightHeight)

	def max(self):
		node = self.head
		if(node==None):
			return None

		while(node.right!=None):
			node = node.right

		return node.value

	def min(self):
		node = self.head
		if(node==None):
			return None

		while(node.left!=None):
			node = node.left

		return node.value

	def isBst(self, node=None):
		if(node==None):
			node=self.head

		if(self.head==None):
			return True

		if(node.left!=None and 
                   (node.left.value>=node.value or not self.isBst(node.left))):
			return False

		if(node.right!=None and 
                   (node.right.value<=node.value or not self.isBst(node.right))):
			return False

		return True
	
	def remove(self,value):
		parent = self.get_parent(value)
		
		if(parent==None):
			raise ValueError("Value not found for BST removal: " + str(value))
				
		if(parent.left.value==value):
			removeNode = parent.left
		elif(parent.right.value==value):
			removeNode = parent.right
		else:
			raise ValueError("Value not found for BST removal: " + str(value))
		
		#determining if the node we're removing has children to the left and/or right
		hasLeft = removeNode.left!=None
		hasRight = removeNode.right!=None
		
		if(hasLeft and hasRight):
			#go to removal node's right subtree and iterate left to find
			#nearest lesser value to use as a replacement removeNode
			nearestLesserNodeParent = removeNode
			nearestLesserNode = removeNode.right
			
			#iterate left to find nearest lesser value to replace removeNode with
			while(nearestLesserNode.left!=None):
				nearestLesserNodeParent = nearestLesserNode
				nearestLesserNode = nearestLesserNode.left
			
			if(nearestLesserNodeParent == removeNode):
				parent.right.value = removeNode.right.value
			else:
				if(parent.left.value==value):
					parent.left.value = nearestLesserNode.value
				else:
					parent.right.value = nearestLesserNode.value
				
				nearestLesserNodeParent.left = None
		else:
			replacementNode = None
			if(hasLeft):
				#left replaces
				replacementNode = removeNode.left			
			elif(hasRight):
				#right replaces
				replacementNode = removeNode.right
			
			if(parent.left.value==value):
				parent.left = replacementNode
			else:
				parent.right = replacementNode
	
	#Uses iterative DFS to return the parent of the found value node
	#Callback runs on each node
	def get_parent(self, value, startNode=None):
		if(startNode==None):
			startNode = self.head

		prevNode = None
		currNode = startNode

		while(currNode!=None):
			nextNode = None

			if(value == currNode.value):
				return prevNode
			elif(value > currNode.value):
				nextNode = currNode.right
			elif(value < currNode.value):
				nextNode = currNode.left

			if(nextNode!=None):
				prevNode = currNode
				currNode = nextNode
			else:
				return currNode

		return None
	
	def get_node(self,value):
		parent = self.get_parent(value)
		if(parent == None):
			return None
		
		if(parent.left!=None and parent.left.value==value):
			return parent.left
		elif(parent.right != None and parent.right.value==value):
			return parent.right
		
		return None
	
	@staticmethod
	def test():
		bst = BinarySearchTree()
		bst.insert(50)
		bst.insert(30)
		bst.insert(70)
		bst.insert(20)
		
		assert bst.get_parent(30).value == 50
		assert bst.get_parent(70).value == 50
		assert bst.get_parent(20).value == 30
		assert bst.get_node(30).value == 30
		assert bst.get_node(-1) == None
		
		bst.insertArray([40,60,80,32,65,75,85,34,36])
		
		assert bst.get_parent(30).value == 50
		assert bst.get_parent(65).value == 60
		assert bst.get_parent(75).value == 80
		assert bst.get_parent(50) == None
		
		bst.print()
		
		toString = bst.to_string()
		prevVal = None
		for val in toString.split(', '):
			floatVal = float(val)
			if(prevVal==None):
				prevVal = floatVal
			else:
				assert floatVal > prevVal
		
		assert bst.get_count() == 13
		
		assert bst.contains(32)
		assert not bst.contains(33)
		
		assert bst.height() == 6
		
		assert bst.max() == 85
		assert bst.min() == 20
		
		assert bst.isBst()
		
		bst.remove(60)
		bst.print()
		
		bst.remove(40)
		bst.print()
		
		bst.remove(70)		
		bst.print()
		
		assert not bst.contains(40)
		assert bst.height() == 5
		
		toString = bst.to_string()
		prevVal = None
		for val in toString.split(', '):
			floatVal = float(val)
			if(prevVal==None):
				prevVal = floatVal
			else:
				assert floatVal > prevVal
		
		assert bst.get_count() == 10
				
		print("BST implementation tests passed.")
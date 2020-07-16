class BinaryTreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def print(self):
		return str(self.value)
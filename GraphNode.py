class GraphNode:
	def __init__(self, intId):
		self.intId = intId
		self.neighbors = set()

	def print(self):
		return str(self.intId)
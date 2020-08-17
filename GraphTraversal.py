from GraphNode import GraphNode
from collections import deque

class GraphTraversal:
	#suboptimal path
	@staticmethod
	def DFS(startNode,searchNode):
		visited = {startNode.intId}
		
		destinations = [node for node in startNode.neighbors]
		
		while(len(destinations)!=0):
			checkNode = destinations.pop()
			if(checkNode.intId not in visited):
				visited.add(checkNode.intId)
				#print("DFS testing node ",checkNode.intId)				
				if(checkNode==searchNode):
					return visited
				destinations += [node for node in checkNode.neighbors]
		
		return None
	
	#optimal path
	@staticmethod
	def BFS(startNode,searchNode):
		visited = {startNode.intId}

		destinations = deque()
		destinations.extendleft(startNode.neighbors)

		while(len(destinations)!=0):
			checkNode = destinations.pop()
			if(checkNode.intId not in visited):
				visited.add(checkNode.intId)
				#print("BFS testing node ",checkNode.intId)
				if(checkNode==searchNode):
					return visited
				destinations.extendleft(checkNode.neighbors)

		return None
	
	@staticmethod
	def test():
		graphNodes = [GraphNode(intId) for intId in range(0,6)]
		
		graphNodes[0].neighbors = set([graphNodes[1]])
		graphNodes[1].neighbors = set([graphNodes[4],graphNodes[0]])
		graphNodes[2].neighbors = set([graphNodes[4],graphNodes[5]])
		graphNodes[3].neighbors = set([graphNodes[5]])
		graphNodes[4].neighbors = set([graphNodes[1],graphNodes[2],graphNodes[5]])
		graphNodes[5].neighbors = set([graphNodes[3],graphNodes[2],graphNodes[4]])

		"""
		example graph:
		
		0 --- 1 --- 4
		          / |
	                 2  |
		          \ |
		      3 --- 5
		
		"""
		
		DfsVisited = GraphTraversal.DFS(graphNodes[5], graphNodes[0])
		BfsVisited = GraphTraversal.BFS(graphNodes[5], graphNodes[0])
		
		print("Graph Traversal tests passed.")
		
GraphTraversal.test()
from BinaryTreeNode import BinaryTreeNode as BtNode
import math

class Heap:
	def __init__(self):
		self._array = []

	# add a new node/value
	def insert(self, value):
		self._array.append(value)
		self.sift_up(len(self._array)-1)

	#swaps a node that is too large with its parent (thereby moving it up) until it is no larger than the node above it.
	def sift_up(self, childIndex):
		parentIndex = Heap._get_parent_index(childIndex)

		while(childIndex>0 and self._array[childIndex] > self._array[parentIndex]):
			self._swap_indices(childIndex,parentIndex)

			childIndex = parentIndex
			parentIndex = Heap._get_parent_index(childIndex)

	# returns the max item, without removing it
	def get_max(self): 
		if(len(self._array)==0):
			return None

		return self._array[0]

	# return number of elements stored
	def get_size(self): 
		return len(self._array)

	def is_empty(self):
		return len(self._array) == 0

	# returns the max item, removing it
	def extract_max(self): 
		maxVal = self.get_max()
		self.remove(0)
		return maxVal

	#swaps a node that is too small with its largest child (thereby moving it down) until it is at least as large as both nodes below it.
	def sift_down(self, parentIndex):
		while(True):
			leftChildIndex = Heap._get_left_child_index(parentIndex)
			rightChildIndex = leftChildIndex + 1
			swapChildIndex = -1

			if(rightChildIndex < len(self._array) and 
			   self._array[rightChildIndex]>self._array[parentIndex] and
			   self._array[rightChildIndex]>self._array[leftChildIndex]):
				swapChildIndex = rightChildIndex
			elif(leftChildIndex < len(self._array) and 
			     self._array[leftChildIndex]>self._array[parentIndex]):
				swapChildIndex = leftChildIndex

			if(swapChildIndex != -1):
				self._swap_indices(parentIndex,swapChildIndex)
				parentIndex = swapChildIndex
			else:
				break

	# removes item at index x
	def remove(self,removeIndex): 
		self._swap_indices(removeIndex,len(self._array)-1)
		self._array.pop()
		self.sift_down(removeIndex)

	#the main function for taking an array and sorting it into a heap
	def heapify(self,arr): 
		self._array = arr
		parentIndex = Heap._get_parent_index(len(self._array)-1)

		for i in range(parentIndex,-1,-1):
			self.sift_down(i)
	
	@staticmethod
	def _get_parent_index(childIndex):
		return math.ceil(childIndex / 2) - 1
	
	@staticmethod
	def _get_left_child_index(parentIndex):
		return math.ceil(parentIndex * 2) + 1
	
	@staticmethod
	def _get_right_child_index(parentIndex):
		return math.ceil(parentIndex * 2) + 2

	def _swap_indices(self, indexA, indexB):
		buffer = self._array[indexA]
		self._array[indexA] = self._array[indexB]
		self._array[indexB] = buffer
		
	@staticmethod
	def test():
		heap = Heap()
		
		assert heap.is_empty() == True
		
		heap.heapify([84,31,56,1,84,33,98,46,12,45,36,77,68,49,31,95,84,26,34,76])
		
		assert heap.get_max() == 98
		assert heap.extract_max() == 98
		assert heap.get_max() == 95
		
		heap.insert(99)
		
		assert heap.get_max() == 99
		assert heap.is_empty() == False
		assert heap.get_size() == 20
		
		heap.remove(1)
		
		for i in range(1,len(heap._array)-1):
			parentIndex = Heap._get_parent_index(i)
			assert heap._array[i] <= heap._array[parentIndex]
			
		print("Heap tests passed.")
class BinarySearch:
	#O(log n) Time Complexity because halving the problem set each iteration
	#O(log n) Space due to recursive stack
	@staticmethod
	def searchRecursive(array,value,low=0,high=0,first=True):
		if(first==True):
			high = len(array)-1
			
		if(low>high):
			return None
		
		#the // operator divides, floors, and casts to int
		mid = (low+high) // 2
		if(array[mid]<value):
			return BinarySearch.searchRecursive(array,value,mid+1,high,False)
		elif(array[mid]>value):
			return BinarySearch.searchRecursive(array,value,low,mid-1,False)
		else:
			return mid
	
	#O(log n) Time Complexity because halving the problem set each iteration
	#O(1) Space
	@staticmethod
	def searchIterative(array,value):
		low = 0
		high = len(array)-1
		
		while(low<=high):
			#the // operator divides, floors, and casts to int
			mid = (low+high) // 2
			if(array[mid]<value):				
				low = mid+1
			elif(array[mid]>value):				
				high = mid-1
			else:
				return mid			
		
		return None
	
	@staticmethod
	def test():
		testArrs = [[1,6,15,21,25,28,31,37],[1],[1,6,15,21,25,28,31],[-10,-1,0]]
		for testArr in testArrs:
			for findVal in testArr:
				foundIndexRecursive = BinarySearch.searchRecursive(testArr,findVal)
				foundIndexIterative = BinarySearch.searchIterative(testArr,findVal)
				assert testArr[foundIndexRecursive] == testArr[foundIndexIterative] == findVal
			
			foundIndexRecursive = BinarySearch.searchRecursive(testArr,999)
			foundIndexIterative = BinarySearch.searchIterative(testArr,999)
			assert foundIndexRecursive == foundIndexIterative == None		
		print("Binary Search tests passed.")
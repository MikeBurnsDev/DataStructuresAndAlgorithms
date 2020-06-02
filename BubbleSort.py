class BubbleSort:
	#O(n^2) Time Complexity
	@staticmethod
	def sort(arr):		
		isSorted = False

		numSteps = 0

		while(not isSorted):
			isSorted = True
			for index in range(len(arr)-1):
				numSteps+=1
				if(arr[index] > arr[index+1]):
					isSorted=False
					buffer = arr[index]
					arr[index] = arr[index+1]
					arr[index+1] = buffer

		return arr, numSteps

	@staticmethod
	def test():
		sortedArr, numSteps = BubbleSort.sort([5,9,7,1,3,4,0,2,6,8])
		assert sortedArr == [0,1,2,3,4,5,6,7,8,9]
		print("Bubble Sort implementation tests passed.")    

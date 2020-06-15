import random

#hash table using universal hashing and linear probing
class HashTable:
	prime = 2147483647 #this is a random large prime. TODO use function to collect prime based on table size

	def __init__(self):
		self.array = [(None,None)] * 4
		self.randomA = random.randint(0,self.prime-1)
		self.randomB = random.randint(0,self.prime-1)
		self.numElements = 0

	def hash(self, key):
		#hash w universal hashing alg, Carter and Wegman 1977
		keyInt = int.from_bytes(str(key).encode("utf-8"), byteorder="big")
		hashed = (self.randomA * keyInt + self.randomB) % self.prime % len(self.array)
		return hashed

	def add(self, key, value):
		def insertKey(elem):
			arrIndex = self.hash(elem[0])
			while(self.array[arrIndex][0]!=None and
			      self.array[arrIndex][0]!="" and
			      self.array[arrIndex][0]!=elem[0]):
				arrIndex+=1
				if(arrIndex==len(self.array)):
					arrIndex=0
			self.array[arrIndex] = elem


		# - if key already exists, update value
		if(self.exists(key)==False):
			self.numElements += 1
		
		if(self.numElements >= len(self.array) / 3 * 2):
			#time to resize
			oldArr = self.array
			self.array = [(None,None)] * (len(self.array) * 2)
			for i in range(len(oldArr)):
				elem = oldArr[i]
				if(elem[0] == None or elem[0] == ""):
					continue
				insertKey(elem)

		insertKey((key,value))

	def exists(self, key):
		return self.get(key) != None

	#gets the internal array's index for a given key
	def getIndex(self, key):
		index = self.hash(key)

		for _ in range(len(self.array)):
			duple = self.array[index]
			if(duple==None):
				return None
			elif(duple[0]==key):
				return index
			else:
				index+=1
				if(index >= len(self.array)):
					index=0

		return None

	#gets the value for a given key
	def get(self, key):
		index = self.getIndex(key)
		if(index==None):
			return None
		return self.array[index][1]

	def remove(self, key):
		self.numElements -= 1
		index = self.getIndex(key)
		if(index==None):
			raise KeyError('Tried to remove a key from HashTable that does not exist.',key)
		self.array[index] = ("",None)
		
	@staticmethod
	def test():
		ht = HashTable()
		assert len(ht.array) == 4
		
		ht.add('tod',1)
		ht.add('bob',2)
		assert len(ht.array) == 4
		
		ht.add('stew',3)
		assert len(ht.array) == 8
		
		ht.add('arnold',4)
		assert ht.get('tod') == 1
		
		ht.add('tod',5)
		assert ht.get('tod') == 5
		
		assert ht.exists('bob') == True
		assert ht.exists('chris') == False
		
		ht.remove('stew')
		assert ht.get('stew') == None
		
		ht = HashTable()
		for i in range(0,1000):
			ht.add(i,'test')
		
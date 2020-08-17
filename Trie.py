class Trie:
	def __init__(self):
		self.charTree = {}
		
	def add(self, word):
		if(type(word) != str):
			return None
		
		word = word.lower()
		
		nodeDict = self.charTree		
		for char in word:
			if(char not in nodeDict):
				nodeDict[char] = {}
			nodeDict = nodeDict[char]
	
	def find(self, word):
		word = word.lower()
		
		nodeDict = self.charTree		
		for char in word:
			if(char in nodeDict):
				nodeDict = nodeDict[char]
			else:
				return False
		return True
	
	@staticmethod
	def test():
		trie = Trie()
		
		loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
		for word in loremIpsum.split(' '):
			trie.add(word)
			
		assert trie.find("laboris") == True
		assert trie.find("Google") == False
		assert trie.find("Laboris") == True
		
		print("Trie implementation tests passed.")
# Heap implementation

'''
def Heap:
	types = {'min': 1, 'max': 0}
	def __init__(self, type):
		if type not in(list(types.keys())):
			raise ValueError("Heap can be only 'min' or 'max'.")
		self.type = type
		self.values = []
		self.size = 0
'''

class Heap_min:
	def __init__(self):
		self.values = []
		self.size = 0

	def insert(self, x):
		self.values.append(x)
		self.size += 1
		self.sift_up(self.size-1)

	def sift_up(self, i):
		if (i!=0):
			j = (i-1)//2
		while (i!=0) and (self.values[i] < self.values[j]):
			self.values[i], self.values[j] = \
				self.values[j], self.values[i]
			i = j
			j = (i-1)//2

	def extract_min(self):
		if not self.size:
			return None
		tmp = self.values[0]
		self.values[0] = self.values[-1]
		self.values.pop()
		if not self.size:
			return None
		self.size -= 1
		self.sift_down(0)
		return tmp

	def sift_down(self, i):
		while (2*i+1 <= self.size):
			j = i
			if self.values[2*i+1] < self.values[i]:
				j = 2*i+1
			if (2*i+2 < self.size) and (self.values[2*i+2] < self.values[j]):
				j = 2*i+2
			if i==j:
				break
			self.values[i], self.values[j] = self.values[j], self.values[i]


class Heap_max:
	def __init__(self):
		self.values = []
		self.size = 0

	def insert(self, x):
		self.values.append(x)
		self.size += 1
		self.sift_up(self.size-1)

	def sift_up(self, i):
		if (i!=0):
			j = (i-1)//2
		while (i!=0) and (self.values[i] > self.values[j]):
			self.values[i], self.values[j] = \
				self.values[j], self.values[i]
			i = j
			j = (i-1)//2

	def extract_max(self):
		if not self.size:
			return None
		tmp = self.values[0]
		self.values[0] = self.values[-1]
		self.values.pop()
		if not self.size:
			return None
		self.size -= 1
		self.sift_down(0)
		return tmp

	def sift_down(self, i):
		while (2*i+1 <= self.size):
			j = i
			if self.values[2*i+1] > self.values[i]:
				j = 2*i+1
			if (2*i+2 < self.size) and (self.values[2*i+2] > self.values[j]):
				j = 2*i+2
			if i==j:
				break
			self.values[i], self.values[j] = self.values[j], self.values[i]

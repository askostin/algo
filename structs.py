# Heap implementation

def in_order(n1, n2, is_asc = True, strict = True):
	""" Check if the order of two given numbers is correct. """
	if strict:
		return ((n1 < n2) if is_asc else (n1 > n2))
	else:
		return ((n1 <= n2) if is_asc else (n1 >= n2))

class Heap:
	types = {'min': 1, 'max': 0}
	def __init__(self, type):
		if type not in(list(self.types.keys())):
			raise ValueError("Heap can be only 'min' or 'max'.")
		self.type = type
		self.values = []
		self.size = 0

	def parent(self, i):
		return (i-1)//2 if (i > 0) else None

	def child_left(self, i):
		return 2*i+1 if ((2*i+1) < self.size) else None

	def child_right(self, i):
		return 2*i+2 if ((2*i+2) < self.size) else None

	def insert(self, x):
		self.values.append(x)
		self.size += 1
		self.sift_up(self.size-1)

	def sift_up(self, i):
		if (i > 0):
			j = self.parent(i)
		while (
			(i > 0) and \
			in_order(
				self.values[i],
				self.values[j],
				is_asc = self.types[self.type]
				)
			):
			self.values[i], self.values[j] = \
				self.values[j], self.values[i]
			i = j
			j = self.parent(i)

	def extract_root(self):
		if self.size == 0:
			return None
		tmp = self.values[0]
		if self.size == 1:
			self.values.pop()
			return tmp
		self.values[0] = self.values[-1]
		self.values.pop()
		self.size -= 1
		self.sift_down(0)
		return tmp

	def sift_down(self, i):
		lc = self.child_left(i)
		is_min_heap = self.types[self.type]
		while lc:
			rc = self.child_right(i)
			j = i
			compare_lc = in_order(
				self.values[lc],
				self.values[i],
				is_asc = is_min_heap
				)
			if rc:
				compare_rc = in_order(
					self.values[rc],
					self.values[i],
					is_asc = is_min_heap
					)
				if compare_lc and compare_rc:
					if in_order(
						self.values[lc],
						self.values[rc],
						is_asc = is_min_heap
						):
						j = lc
					else:
						j = rc
				elif compare_lc:
					j = lc
				elif compare_rc:
					j = rc
			elif compare_lc:
				j = lc
			if i==j:
				break
#			print(f"parent (n[{i}] = {self.values[i]}) <-> " +
#				  f"child (n[{j}] = {self.values[j]})")
			self.values[i], self.values[j] = self.values[j], self.values[i]
			i = j
			lc = self.child_left(i)


class Heap_min:
	def __init__(self):
		self.values = []
		self.size = 0

	def parent(self, i):
		return (i-1)//2 if (i > 0) else None

	def child_left(self, i):
		return 2*i+1 if ((2*i+1) < self.size) else None

	def child_right(self, i):
		return 2*i+2 if ((2*i+2) < self.size) else None

	def insert(self, x):
		self.values.append(x)
		self.size += 1
		self.sift_up(self.size-1)

	def sift_up(self, i):
		if (i > 0):
			j = self.parent(i)
		while (i > 0) and in_order(self.values[i], self.values[j]):
			self.values[i], self.values[j] = \
				self.values[j], self.values[i]
			i = j
			j = self.parent(i)

	def extract_min(self):
		if self.size == 0:
			return None
		tmp = self.values[0]
		if self.size == 1:
			self.values.pop()
			return tmp
		self.values[0] = self.values[-1]
		self.values.pop()
		self.size -= 1
		self.sift_down(0)
		return tmp

	def sift_down(self, i):
		lc = self.child_left(i)
		while lc:
			rc = self.child_right(i)
			j = i
			more_than_left = in_order(self.values[lc], self.values[i])
			if rc:
				more_than_right = in_order(self.values[rc], self.values[i])
				if more_than_left and more_than_right:
					if (self.values[lc] < self.values[rc]):
						j = lc
					else:
						j = rc
				elif more_than_left:
					j = lc
				elif more_than_right:
					j = rc
			elif more_than_left:
				j = lc
			if i==j:
				break
			self.values[i], self.values[j] = self.values[j], self.values[i]
			i = j
			lc = self.child_left(i)


class Heap_max:
	def __init__(self):
		self.values = []
		self.size = 0

	def parent(self, i):
		return (i-1)//2 if (i > 0) else None

	def child_left(self, i):
		return 2*i+1 if ((2*i+1) < self.size) else None

	def child_right(self, i):
		return 2*i+2 if ((2*i+2) < self.size) else None

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
		lc = self.child_left(i)
		while lc:
			rc = self.child_right(i)
			j = i
			less_than_left = (self.values[lc] > self.values[i])
			if rc:
				less_than_right = (self.values[rc] > self.values[i])
				if less_than_left and less_than_right:
					if (self.values[lc] < self.values[rc]):
						j = rc
					else:
						j = lc
				elif less_than_left:
					j = lc
				elif less_than_right:
					j = rc
			elif less_than_left:
				j = lc
			if i==j:
				break
			self.values[i], self.values[j] = self.values[j], self.values[i]
			i = j
			lc = self.child_left(i)

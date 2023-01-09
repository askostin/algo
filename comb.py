def generate_numbers(N: int):
	"""
	Генерация всех чисел длины N.
	"""
	def aux(M: int, prefix = None):
		prefix = prefix or []
		if M == 0:
			print(prefix)
			return
		for i in range(N):
			prefix.append(i)
			aux(M-1, prefix)
			prefix.pop()

	aux(N)

def generate_permutations(N: int):
	def aux(M: int, prefix = None):
		prefix = prefix or []
		if M == 0:
			print(prefix)
			return
		for i in range(1, N+1):
			if i in prefix:
				continue
			prefix.append(i)
			aux(M-1, prefix)
			prefix.pop()

	aux(N)

# For given number @n generate list of all various numbers,
# which are results of permutatiuons of digits of @n.
def permutations(n: int):
	s = str(n)
	perms = []
	def aux(lod: list, prefix = ""):
		if not lod:
			perms.append(prefix)
		for i in range(len(lod)):
			aux(lod[:i]+lod[i+1:], prefix + lod[i])

	aux(s)
	return list(set([int(x) for x in perms]))
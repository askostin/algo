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
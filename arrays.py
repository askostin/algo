def circ_shift(A: list, direction = 'right', steps = 1):
	"""
		Shift all the elements of the array.
		A - array
		direction - 'left' or 'right' (default)
		steps - number of steps to move element
	"""

	if (direction == 'right'):
		m = 1
	elif (direction == 'left'):
		m = -1
	else :
		print("Direction should be 'left' or 'right")
		return -1

	if (steps <= 0):
		print("Need positive number of steps")
		return -1

	N = len(A)
	tmp = [0] * N
	for i in range(N):
		tmp[i] = a[(i + m * steps) % N]

	return tmp


def test_circ_shift():
	A = [1, 2, 3, 4]
	if circ_shift(A, 'right', 2) == [3, 4, 1, 2]:
		return "Test 1 passed"
	else :
		return "Test 1 failed"
	if circ_shift(A, 'left', 1) == [2, 3, 4, 1]:
		return "Test 2 passed"
	else :
		return "Test 2 failed"
	if circ_shift(A, 4) == A:
		return "Test 3 passed"
	else :
		return "Test 3 failed"


def sieve_erato(n: int):
	"""
		Create the list of prime numbers in the range [2, n] using the Sieve of Eratosthenes.
	"""
	A = [True] * n
	for k in range (2, n + 1):
		if A[k] :
			for j in range (2 * k, n, k):
				A[j] = False

	for k in range (n) :
		print(k, '-', "Prime" if A[k] else "Not prime")

def in_order(n1, n2, ascending = True):
	""" Check if the order of two given numbers is correct. """
	return ((n1 < n2) if ascending else (n1 > n2))


def insert_sort(A: list, ascending = True):
	""" Sorting array by insertion sort. """
	N = len(A)
	for i in range(1, N):
		tmp = A[i]
		j = i - 1
		while j >= 0 and in_order(tmp, A[j], ascending):
		#  ((A[j] > A[i]) == ascending)
			A[j+1] = A[j]
			j = j - 1
		A[j+1] = tmp


def choice_sort(A: list, ascending = True):
	""" Sorting array by choice sort. """
	N = len(A)
	for i in range(N):
		tmp_val = A[i]
		tmp_idx = i
		for j in range(i+1, N):
			if in_order(A[j], tmp_val, ascending):
				tmp_val = A[j]
				tmp_idx = j
		if (tmp_idx != i) :
			A[i], A[tmp_idx]  = A[tmp_idx], A[i]


def bubble_sort(A: list, ascending = True):
	""" Sorting array by bubble sort. """
	N = len(A)
	for i in range(N-1):
		for j in range(N-1, i, -1):
			if in_order(A[j], A[j-1], ascending):
				A[j], A[j-1] = A[j-1], A[j]


def count_sort(A: list, ascending = True):
	"""
	Using frequency analysis, Sort set of numbers for which we know the range of values.
	"""
	pass


def merge_sort(A: list, ascending = True):
	""" Sorting array by merge sort. """
	def merge(A1, A2: list):
		if not A1:
			return A2
		if not A2:
			return A1
		n1 = len(A1)
		n2 = len(A2)
		i, j = 0, 0
		A = []
		while (i < n1) and (j < n2):
			if A1[i] <= A2[j]:
				A.append(A1[i])
				i += 1
			else:
				A.append(A2[j])
				j += 1
		if (i < n1):
			return A + A1[i:]
		elif (j < n2):
			return A + A2[j:]
		else:
			return A
	
	if (len(A) <= 1):
		return A
	middle_index = len(A) // 2
	left_sorted = merge_sort(A[:middle_index])
	right_sorted = merge_sort(A[middle_index:])
	return merge(left_sorted, right_sorted)


def test_sort(sort_algorithm):
	print("Testing: ", sort_algorithm.__doc__)

	print("#testcase #1:", end = '')
	A = [4, 2, 5, 1, 3]
	A_sorted = [1, 2, 3, 4, 5]
	sort_algorithm(A)
	print("OK" if (A == A_sorted) else "Fail")

	print("#testcase #2:", end = '')
	A = list(range(10, 20)) + list(range(0, 10))
	A_sorted = list(range(0, 20))
	sort_algorithm(A)
	print("OK" if (A == A_sorted) else "Fail")

	print("#testcase #3:", end = '')
	A = [4, 2, 4, 2, 1]
	A_sorted = [1, 2, 2, 4, 4]
	sort_algorithm(A)
	print("OK" if (A == A_sorted) else "Fail")


if __name__ == '__main__':
	test_sort(insert_sort)
	test_sort(choice_sort)
	test_sort(bubble_sort)
	test_sort(merge_sort)
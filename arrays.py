# import operator

def circ_shift(A: list, direction = 'right', steps = 1):
	"""
		Shift all the elements of the array.
		* A - array
		* direction - 'left' or 'right' (default)
		* steps - number of steps to move element
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


def sieve_erato(n: int):
	"""
	Create the list of prime numbers in the range [2, n] using
	the Sieve of Eratosthenes.
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


def add_element(x, array, right = True):
	array.insert((len(array) if right else 0), x)
	return


def is_sorted(A: list):
	"""Checks if the array @A is sorted in the specified order.
	Execution time is O(n).
	"""
	N = len(A)
	if (N < 2):
		return (True, None)
	# Flag indicates if first two non-equal elements are in asc/desc order:
	is_asc = None
	i = 1
	while ((A[i] == A[i-1]) and (i < N)):
		i += 1
	if (i == N):
		return (True, None)
	is_asc = (A[i-1] < A[i])
	for j in range(i+1, N):
		if in_order(A[j-1], A[j], not is_asc):
			return (False, None)
	return (True, is_asc)


def insert_sort(A: list, ascending = True, inplace = True):
	""" Sorting array by insertion sort. """
	N = len(A)
	C = A if inplace else [x for x in A]
	for i in range(1, N):
		tmp = C[i]
		j = i - 1
		while j >= 0 and in_order(tmp, C[j], ascending):
			C[j+1] = C[j]
			j = j - 1
		C[j+1] = tmp
	if not inplace:
		return C


def choice_sort(A: list, ascending = True, inplace = True):
	""" Sorting array by choice sort. """
	N = len(A)
	C = A if inplace else [x for x in A]
	for i in range(N):
		tmp_val = C[i]
		tmp_idx = i
		for j in range(i+1, N):
			if in_order(C[j], tmp_val, ascending):
				tmp_val = C[j]
				tmp_idx = j
		if (tmp_idx != i) :
			C[i], C[tmp_idx] = C[tmp_idx], C[i]
	if not inplace:
		return C


def bubble_sort(A: list, ascending = True, inplace = True):
	""" Sorting array by bubble sort. """
	N = len(A)
	C = A if inplace else [x for x in A]
	for i in range(N-1):
		for j in range(N-1, i, -1):
			if in_order(C[j], C[j-1], ascending):
				C[j], C[j-1] = C[j-1], C[j]
	if not inplace:
		return C


def count_sort(A: list, ascending = True):
	"""Using frequency analysis, sort set of numbers
	for which we know the range of values.
	"""
	pass


def merge(A1, A2: list, ascending = True):
	if not A1:
		return A2
	if not A2:
		return A1
	n1, n2 = len(A1), len(A2)
	i, j = 0, 0
	A = []
	while (i < n1) and (j < n2):
		if in_order(A1[i], A2[j], ascending):
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


def merge_sort(A: list, ascending = True, inplace = True):
	""" Sorting array by merge sort. """
	if inplace:
		if (len(A) <= 1):
			return
		middle_idx = len(A) // 2
		L = A[:middle_idx]
		R = A[middle_idx:]
		merge_sort(L, ascending, inplace)
		merge_sort(R, ascending, inplace)
		tmp = merge(L, R, ascending)
		for i in range(len(A)):
			A[i] = tmp[i]
	else:
		if (len(A) <= 1):
			return A
		middle_idx = len(A) // 2
		L = merge_sort(A[:middle_idx], ascending, inplace)
		R = merge_sort(A[middle_idx:], ascending, inplace)
		return merge(L, R, ascending)


def hoar_sort(A, ascending = True, inplace = True):
	""" Sorting array by fast Hoar sort. """
	C = A if inplace else [x for x in A]
	if len(A) <= 1:
		if inplace:
			return # = return None
		else:
			return C
	barrier = C[0]
	L, M, R = [], [], []
	for x in C:
		if in_order(x, barrier, ascending):
			#add_element(x, L, ascending)
			L.append(x)
		elif x == barrier:
			#add_element(x, M, ascending)
			M.append(x)
		else:
			#add_element(x, R, ascending)
			R.append(x)
	hoar_sort(L, ascending)
	hoar_sort(R, ascending)
	i = 0
	for x in (L + M + R):
		C[i] = x
		i += 1
	if not inplace:
		return C


def search_binary(x, A, is_asc):
	"""
	In the sorted array find first and last occurences of elements
	@A[i] = @x and returns tuple (@left_bound, @right_bound),
	where @left_bound is the element preceeding to the first element,
	equal to @x, @right bound is the first element not equal to @x.
	"""
	def find_lbound(x, A):
		left = -1
		right = len(A)
		while (right - left > 1):
			middle = (left + right) // 2
			if is_asc:
				compare = (x <= A[middle])
			else:
				compare = (x >= A[middle])
			if compare:
				right = middle
			else:
				left = middle
		return left

	def find_rbound(x, A):
		left = -1
		right = len(A)
		while (right - left > 1):
			middle = (left + right) // 2
			if is_asc:
				compare = (x < A[middle])
			else:
				compare = (x > A[middle])
			if compare:
				right = middle
			else:
				left = middle
		return right

	return (find_lbound(x, A), find_rbound(x, A))


def subarray_max_mono(A: list, ascending = True, strict_mono = True):
	""" Find maximal monotonous ascending (or descending) subarray of @A.

	Paramenters:
	@ascending - if we look for ascending or descending subarray
	@strict_mono - if the subarray is strictly monotonous, i.e.
		if sequence [a_1, a_2, ..., a_n] is ascending:
		- a_{n} < a_{n+1} for any n in strictly monotonous seqence,
		- a_{n} <= a_{n+1} for any n in non-strictly monotonous sequence.
	"""
	pass


def subarray_max_common(A, B: list) -> list:
	""" For two given arrays find their maximal common subarray.
	"""
	F = [[0]*(len(B)+1) for i in range(len(A)+1)]
	for i in range(1, len(A)+1):
		for j in range(1, len(B)+1):
			if A[i-1] == B[j-1]:
				F[i][j] = 1 + F[i-1][j-1]
			else:
				F[i][j] = max(F[i-1][j], F[i][j-1])
	# search of subarray itself
		....
	return F[-1][-1]


def subarray_nsep_max_diff(A:list) -> list:
	"""For numeric sequence find nonseparate subsequence of elements
	(number) for which difference between last and first elements
	is maximal -- like our sequence is a row of daily prces,
	and we want to get maximal profit buying at one price
	and selling at another.
	"""
	pass

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

def add_element(x, array, right = True):
	array.insert((len(array) if right else 0), x)
	return


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
	"""
	Using frequency analysis, Sort set of numbers for which we know the range of values.
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


def is_sorted(A: list, ascending = True):
	"""
	Checks if the array @A is sorted in the specified order. Execution time is O(n).
	"""
	if not A:
		return True
	prev_elt = A[0]
	for elt in A[1:]:
		if in_order(prev_elt, elt, ascending) or (prev_elt == elt):
			prev_elt = elt
		else:
			return False
	return True


def search_binary(x, A):
	"""
	In the sorted array find first and last occurences of elements @A[i] = @x and returns tuple (@left_bound, @right_bound), where @left_bound is the first element equal to @x, @right bound is the first element not equal to @x, so @A[left_bound, right_bound] is the subarray of @A, where all the elements are equal to @x.
	"""
	pass


## Test sorting algorithms for correctness.

test_arrays = ([[4, 2, 5, 1, 3], list(range(10, 20)) + list(range(0, 10)), [4, 2, 4, 2, 1]])
test_arrays_sorted_asc = ([[1, 2, 3, 4, 5], list(range(0, 20)), [1, 2, 2, 4, 4]])
test_arrays_sorted_desc = ([[5, 4, 3, 2, 1], list(range(19, -1, -1)), [4, 4, 2, 2, 1]])

def test_sort(sort_algorithm, same_object = True):
	print("\nTesting:", sort_algorithm.__doc__[:-2], ' (inplace).' if same_object else '.', sep = '')

	for i in range(len(test_arrays)):
		print("#testcase #{}:".format(i+1), end = '\n')
		A = test_arrays[i]
		A_sorted_asc = test_arrays_sorted_asc[i]
		A_sorted_desc = test_arrays_sorted_desc[i]
		if same_object:
			# No declaration of 'inplace = True' since it is default value.
			sort_algorithm(A)
			print("sort in ascending order:",
				  "OK" if (A == A_sorted_asc) else "Fail")
			sort_algorithm(A, ascending = False)
			print("sort in descending order:",
				  "OK" if (A == A_sorted_desc) else "Fail")
		else:
			print("sort in ascending order:",
				  "OK" if (sort_algorithm(A, inplace = False) == A_sorted_asc) else "Fail")
			print("sort in descending order:",
				  "OK" if (sort_algorithm(A, ascending = False, inplace = False) == A_sorted_desc) else "Fail")


if __name__ == '__main__':
	test_sort(insert_sort)
	test_sort(insert_sort, same_object = False)
	test_sort(choice_sort)
	test_sort(choice_sort, same_object = False)
	test_sort(bubble_sort)
	test_sort(bubble_sort, same_object = False)
	test_sort(merge_sort)
	test_sort(merge_sort, same_object = False)
	test_sort(hoar_sort)
	test_sort(hoar_sort, same_object = False)

from arrays import *

## Test sorting algorithms for correctness.

test_arrays = \
	[[4, 2, 5, 1, 3],
	 list(range(10, 20)) + list(range(0, 10)),
	 [4, 2, 4, 2, 1]]
test_arrays_sorted_asc = \
	[[1, 2, 3, 4, 5],
	 list(range(0, 20)),
	 [1, 2, 2, 4, 4]]
test_arrays_sorted_desc = \
	[[5, 4, 3, 2, 1],
	 list(range(19, -1, -1)),
	 [4, 4, 2, 2, 1]]

def apply_sort_algo(sort_algorithm, A, A_sorted_correct, ascending, inplace):
	order = 'ascending' if ascending else 'descending'
	if inplace:
		sort_algorithm(A, ascending, inplace)
		A_sorted = A
	else:
		A_sorted = sort_algorithm(A, ascending, inplace)
	result = "OK" if (A_sorted == A_sorted_correct) else "Fail"
	print("sort in", order, "order:", result)

def test_sort(sort_algorithm, inplace = True):
	print("\nTesting:",
		  sort_algorithm.__doc__[:-2],
		  ' (inplace).' if inplace else '.',
		  sep = '')

	for i in range(len(test_arrays)):
		print("testcase #{}:".format(i+1), end = '\n')
		A = test_arrays[i]
		A_sorted_asc = test_arrays_sorted_asc[i]
		A_sorted_desc = test_arrays_sorted_desc[i]
		apply_sort_algo(
			sort_algorithm,
			A,
			A_sorted_asc,
			ascending = True,
			inplace = inplace
		)
		apply_sort_algo(
			sort_algorithm,
			A,
			A_sorted_desc,
			ascending = False,
			inplace = inplace
		)

'''
		if inplace:
			# No declaration of 'inplace = True' since it is default value.
			sort_algorithm(A)
			print("sort in ascending order:",
				  "OK" if (A == A_sorted_asc) else "Fail")
			sort_algorithm(A, ascending = False)
			print("sort in descending order:",
				  "OK" if (A == A_sorted_desc) else "Fail")
		else:
			if (sort_algorithm(A,
							   inplace = False) == A_sorted_asc):
				tmp = "OK"
			else:
				tmp = "Fail"
			print("sort in ascending order:", tmp)
			if (sort_algorithm(A,
							   ascending = False,
							   inplace = False)
				== A_sorted_desc):
				tmp = "OK"
			else:
				tmp = "Fail"
			print("sort in descending order:", tmp)
'''


def test_is_sorted():
	print("\nTesting is_sorted():")
	for i in range(len(test_arrays)):
		print("testcase #{}:".format(i+1), end = '\n')
		A = test_arrays[i]
		A_sorted_asc = test_arrays_sorted_asc[i]
		A_sorted_desc = test_arrays_sorted_desc[i]

		if (is_sorted(A) == (False, None)):
			print("OK")
		else:
			print("Fail")

		if (is_sorted(A_sorted_asc) == (True, True)):
			print("OK")
		else:
			print("Fail")

		if (is_sorted(A_sorted_desc) == (True, False)):
			print("OK")
		else:
			print("Fail")


if __name__ == '__main__':
	'''
	test_sort(insert_sort)
	test_sort(insert_sort, inplace = False)
	test_sort(choice_sort)
	test_sort(choice_sort, inplace = False)
	test_sort(bubble_sort)
	test_sort(bubble_sort, inplace = False)
	test_sort(merge_sort)
	test_sort(merge_sort, inplace = False)
	test_sort(hoar_sort)
	test_sort(hoar_sort, inplace = False)
	'''
	test_is_sorted()

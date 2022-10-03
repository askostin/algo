from algo.tests.test import general_test
from algo.arrays import *


def help():
	print("test_in_order()")
	print("# Sorting functions: #")
	print("test_is_sorted()")
	print("test_apply_sort_algo()")
	print("test_sort()")
	print("are applied to:")
	print("- insert sort,")
	print("- choice sort,")
	print("- bubble sort,")
	print("- merge sort,")
	print("- hoar sort,")
	print("- heap sort.")
	print("######################")
	print("test_circ_shift()")
	print("test_search_binary()")
	print("test_lms()")
	print("test_lcs()")
	print("test_smd()")


def test_in_order():
	general_test(
		in_order,
		[[-2, -1],
		 [2, 1],
		 [0, -1, True, False],
		 [0, 0, True, False],
		 [-1, -2, False],
		 [1, 2, False],
		 [1, 1, False, False],
		 [4, 6, False, False],
		 [4, 4, False, True]],
		[True, False, False, True, True, False, True, False, False]
	)


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


def test_is_sorted():
	general_test(
		is_sorted,
		[[input] for input in
		 test_arrays +
			test_arrays_sorted_asc +
			test_arrays_sorted_desc
		 ],
		[(0, None), (0, None), (0, None),
		 (1, 1), (1, 1), (1, 1),
		 (1, 0), (1, 0), (1, 0)]
		)

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
	print("\nTesting ",
		  sort_algorithm.__name__,
		  '() (inplace):' if inplace else '() (non-inplace):',
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


## Tests for non-sorting functions

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


def test_search_binary():
	general_test(
		search_binary,
		[[4, range(1, 10), True],
		 [4, range(9, 0, -1), False],
		 [4, range(0, 4), True],
		 [3, [1, 1, 2, 2, 3, 3], True]],
		[(2, 4),
		 (4, 6),
		 (3, 4),
		 (3, 6)]
	)

def test_lms():
	general_test(
		lms,
		[[[1, 2, 3, 0, 1]],
		 [[3, 2, 2, 3, 4, 1, 1], True, False],
		 [[-1, 0, 1, 1, 0, 3, -2], False],
		 [[-1, 0, 1, 1, 0, -2, -1], False, False]],
		[[1, 2, 3],
		 [2, 2, 3, 4],
		 [1, 0],
		 [1, 1, 0, -2]]
	)


def test_lcs():
	general_test(
		lcs,
		[[[1, 2, 3, 0, 1], [4, 2, 2, 5, 6]],
		 [[1, 2, 2, 3 ,4, 1, 1], [6, 2, 1, 5]],
		 [[-1, 0, 1, 0], [4, 3, -2, 0]]],
		[[2],
		 [2, 1],
		 [0]]
	)


def test_smd():
	general_test(
		smd,
		[[[100, 113, 110, 85, 105, 102, 86, 63,
		   81, 101, 94, 106, 101, 79, 94, 90, 97]],
		 [[1, 2]],
		 [[0, 5, -6, -4, 0, -3, -1]]],
		[[63, 81, 101, 94, 106],
		 [1, 2],
		 [-6, -4, 0]]
	)


if __name__ == '__main__':
	test_in_order()
	test_is_sorted()

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
	test_sort(heap_sort)
	test_sort(hoar_sort, inplace = False)

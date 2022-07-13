from algo.arrays import *


def help():
	print("# Sorting functions: #")
	print("test_is_sorted()")
	print("test_insert_sort()")
	print("test_choice_sort()")
	print("test_bubble_sort()")
	print("test_merge_sort()")
	print("test_hoar_sort()")
	print("######################")
	print("test_circ_shift()")
	print("test_search_binary()")
	print("test_subarray_mono_max()")
	print("test_subarray_common_max()")
	print("test_subarray_nsep_max_diff()")


def general_test(fun, input, output_cor):
	if (len(input) != len(output_cor)):
		raise ValueError('Input and ouput must have the same size.')
	if (isinstance(input[0], list)):
		output = [fun(*val) for val in input]
	else:
		output = [fun(val) for val in input]
	flag = True
	print("\nTesting {}():".format(fun.__name__))
	for i, o, o_c in zip(input, output, output_cor):
		if (o != o_c):
			flag = False
			print(
				"Fail: {}({}) = {}, must be {}"\
				.format(fun.__name__,i, o, o_c)
			)
	if flag:
		print("Test passed")


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


# Add test_search_binary()

# Add test_subarray_mono_max()

# Add test_subarray_common_max()

# Add test_subarray_nsep_max_diff()

if __name__ == '__main__':
	print("Testing is_sorted():")
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



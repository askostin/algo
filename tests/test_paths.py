# Tests for functions, making path search, select, count.
from algo.paths import *

def test_grasshoper_count_paths():
	args_sets = [
		[5, [1, 2], [], 8],
		[5, [1, 2, 3], [1, 2, 3], 0],
		[6, [1, 2, 3], [], 24],
		[6, [1, 2], [2, 4], 1],
		[6, [1, 2, 3], [3], 8]
		]

	def aux(i, *args):
		tmp = grasshoper_count_paths(args[0], args[1], args[2])
		s1 = 'passed' if (tmp == args[3]) else 'failed'
		s2 = "forbidden = {}, ".format(args[2]) if args[2] else ''
		s3 = '' if (tmp == args[3]) else ", have to be {}".format(args[3])
		s = "Test #{} {}:\n".format(i+1, s1) + \
			"for N = {}, steps = {}, {}".format(args[0], args[1], s2) + \
			"the answer is {}{}\n".format(tmp, s3)
		return s

	for i in range(len(args_sets)):
		print(aux(i, *args_sets[i]))


def test_grasshoper_best_path():
	def test_result(i, is_passed):
		if is_passed:
			print("Test #{} passed".format(i))
		else:
			print("Test #{} failed".format(i))

	test_result(1, grasshoper_best_path([1,1,1]) == ([2,3], 2) or \
		grasshoper_best_path([1,1,1]) == ([1,3], 2))
	test_result(2, grasshoper_best_path([1,1,1,1]) == ([2,4], 2))
	test_result(3, grasshoper_best_path([2,1,2,1]) == ([2,4], 2))


def test_king_count_paths():
	def size(num:int) -> int:
		return len(str(abs(num)))
	K = king_count_paths(8, 8, ret_all = True)
	max_size = size(K[7][7])
	for row in K:
		for num in row:
			print(
				' '*(max_size - size(num) + 1) + str(num),
				end = ' ')
		print("\n")


if __name__ == '__main__':
	print("\nTesting grasshoper_count_paths():")
	test_grasshoper_count_paths()

	print("\nTesting grasshoper_best_path():")
	test_grasshoper_best_path()

	print("\nTesing king_count_paths():")
	test_king_count_paths()

from algo.spelling import *

def help():
	print("test_match()")
	print("test_check_paren()")
	print("test_levenstein()")


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
				.format(fun.__name__, i, o, o_c)
			)
	if flag:
		print("Test passed")


def test_match():
	general_test(
		match,
		[['abc', 'a?c'], ['abc', 'a??c'], ['abc', '***a***c***']],
		[True, False, True]
	)


def test_check_paren():
	general_test(
		check_paren,
		[['()()', False],
		 ['(([()()])){}[()({})]', False],
		 [')', False],
		 ['(', False],
		 ['((])', False],
		 ['[()}]', False]],
		[True,
		 True,
		 False,
		 False,
		 False,
		 False]
	)


def test_levenstein():
	general_test(
		levenstein,
		[['aaa', 'aaa'],
		 ['333-a1', '333-a'],
		 ['kitten', 'sitting'],
		 ['Saturday', 'Sunday'],
		 ['exponential', 'polynomial']],
		[0,
		 1,
		 3,
		 3,
		 6]
	)

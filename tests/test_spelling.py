from algo.tests.test import general_test
import algo.spelling as s

def help():
	print("test_match()")
	print("test_check_paren()")
	print("test_levenstein()")
	print("test_prefix()")
	print("test_kmp()")


def test_match():
	general_test(
		s.match,
		[['abc', 'a?c'], ['abc', 'a??c'], ['abc', '***a***c***']],
		[True, False, True]
	)


def test_check_paren():
	general_test(
		s.check_paren,
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
		s.levenstein,
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


def test_prefix():
	general_test(
		s.prefix,
		[['aabaa'],
		 ['aabaab'],
		 ['aabaabaaaabaaba'],
		 ['aabaabaaaabaabaaab', True]],
		[2,
		 3,
		 7,
		 [0, 1, 0, 1, 2, 3, 4, 5, 2, 2, 3, 4, 5, 6, 7, 8, 9, 3]]
)


def test_kmp():
	general_test(
		s.kmp,
		[['ab', 'ababab'],
		 ['','34r'],
		 ['mm1', '1mm2'],
		 ['ac', 'aacababbac']],
		[[0, 2, 4],
		 [],
		 [],
		 [1, 8]]
	)

if __name__ == "__main__":
	test_match()
	test_check_paren()
	test_levenstein()
	test_prefix()
	test_kmp()

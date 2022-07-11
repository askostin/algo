# Tests for functions, making path search, select, count.
from .paths import *

def test_grasshoper_count_paths():
	pass

def test_grasshoper_best_path():
	pass

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

# Functions to work with various dats structures (lists, arrays, trees etc.)
# to find some elements, set of elements, substructures; build optimal paths;
# count number of possible paths.
# Here we implement some algorithms of 'dynamic programming'.


def grasshoper_count_paths(N: int, steps = [1, 2, 3], forbidden = []):
	"""Find number of possible path variants in the 1D road with @N+1 points
	(start has index "0", end -- "@N"), where we can make jumps with lenghts
	stated in @steps list (max step is @N//10).
	There also can be 'forbidden' points, which are given as the list of
	indexes @i, 0 < @i < @N.
	"""
	if N < 2:
		raise ValueError("Should be 2 or more points to jump to.")
	if (not forbidden):
		forbidden = list(set(sorted(forbidden)))
	for p in forbidden:
		if (p < 1) or (p >= N):
			raise ValueError(
				"Forbidden points have to be in range [1, {})".format(N)
			)
	steps = list(set(sorted(steps)))
	for s in steps:
		if (s <= 0):
			raise ValueError("All step sizes have to be positive integers.")
	pths_to_first = 0 if (1 in forbidden) else 1
	K = [1, pths_to_first] + [0]*(N-1)
	for i in range(2, N+1):
		for s in [s for s in steps if (i-s >= 0)]:
			if not ((i-s) in forbidden):
				K[i] += K[i-s]
	K[0] = 0
	return K[N]


def grasshoper_best_path(prices: list, steps = [1, 2]):
	"""Find path from point 0 to point N with minimal cost,
	so we have start point and N other points [1,...,N].
	Parameters:
		prices - list of prices of jump from (i-1)-th point to i-th, i = [1...N]
		steps - list of jump values
	"""
	N = len(prices)
	for s in steps:
		if (s <= 0):
			raise ValueError("All step sizes have to be positive integers.")
		if (max(steps) > N // 2):
			raise ValueError("Step size ({}) too big.".format(max(steps)))

	C = [float("-inf"), prices[0], prices[0] + prices[1]] + [None]*(N-2)
	for i in range(3, N+1):
		steps_possible = [s for s in steps if (i-s > 0)]
		C[i] += price[i] + min([C[i-s] for s in steps_possible])
	return C[N]


def king_count_paths(M, N: int, *, ret_all = False):
	"""Count the number of ways how the king, starting from one corner
	of the chess plate with size N*M (e.g. a1 or (0,0)) will reach diagonnaly
	opposite corner (h8 or (7,7) for classic plate 8x8).
	The King can go only in 2 directions: if a1 is top left corner place,
	the King can go only one filed down or right, and it have to reach
	low right corner h8.
	"""
	K = [[0]*(N+1) for i in range(M+1)]
	K[1][1] = 1
	for i in range(2, M+1):
		K[i][1] = 1
	for j in range(2, N+1):
		K[1][j] = 1
	for i in range(2, M+1):
		for j in range(2, N+1):
			K[i][j] = K[i-1][j] + K[i][j-1]
	if ret_all:
		return [row[1:] for row in K[1:]]
	else:
		return K[M][N]

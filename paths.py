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
		prices - list of prices of jump from (i-1)-th point to i-th
		steps - list of jump values
	"""
	N = len(prices)
	prices = [0] + prices
	steps = list(set(sorted(steps)))
	for s in steps:
		if (s <= 0):
			raise ValueError("All step sizes have to be positive integers.")
		if (max(steps) > (N // 2 + 1)):
			raise ValueError("Step size ({}) too big.".format(max(steps)))

	C = [0, prices[1]] + [None]*(N-1)
	for i in range(2, N+1):
		steps_possible = [s for s in steps if (i-s >= 0)]
		C[i] = prices[i] + min([C[i-s] for s in steps_possible])

	def find_path(point, points):
		if point == 0:
			return points
		best_prev_point = point - steps[0]
		for s in steps[1:]:
			prev_point = point - s
			if (C[prev_point] < C[best_prev_point]):
				best_prev_point = prev_point
		return(
			find_path(
				best_prev_point,
				[best_prev_point] + points
			)
		)

	return (find_path(N, [N])[1:], C[N])


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


def backpack(M: int, names, m, v: list, test_output = False) -> list:
	"""
	Find optimal selection of goods, described by lists of
	names @names[i], masses (volumes) @m[i], values (prices) @ v[i],
	for backpack (inventory) with maximal payload (volume) M.
	"""
	N = len(names)
	assert (N == len(list(set(names)))) and \
		((N == len(m)) and (N == len(v)))
	m = [0] + [m[i] for i in range(N)]
	v = [0] + [v[i] for i in range(N)]
	F = [[0]*(N + 1) for i in range(M + 1)]
	for i in range(1, N + 1):
		for j in range(1, M + 1):
			if m[i] <= j:
				F[i][j] = max(F[i-1][j], v[i] + F[i-1][j - m[i]])
			else:
				F[i][j] = F[i-1][j]
	if test_output:
		return [[F[i][j] for j in range (1, M+1)] for i in range(1, N+1)]
	else:
		return F[N][M]

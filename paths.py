# Functions to work with various dats structures (lists, arrays, trees etc.)
# to find some elements, set of elements, substructures; build optimal paths;
# count number of possible paths.
# Here we implement some algorithms of 'dynamic programming'.

# Добавить функцию # прыжки кузнечика - количество способов
def grasshoper_paths_quantity(N: int, steps = [1, 2, 3], forbidden = [])
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
	K = [0, 1] + [0]*(N-1)
	for i in range(2, N+1):
		K[i] = 0
		for s in [s for s in steps if (i-s > 0)]:
			if not ((i-s) in forbidden):
				K[i] += K[i-s]
		K[i] = K[i] or 0
	return K[N]

# Добавить функцию # прыжки кузнечика - наиболее выгодная тракетория
def grasshoper_best_path(prices: list, steps = [1, 2]):
	"""Find path from point 0 to point N with minimal cost,
	so we have start point and N other points.
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

# Добавить функцию # траектория короля

# Добавит

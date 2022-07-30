def cols_word(n_cols: int) :
    if (n_cols % 100 > 10) and (n_cols % 100 < 20) :
        return ('колонок')
    elif (n_cols % 10 == 1) :
        return('колонка')
    elif (n_cols % 10 in [2, 3, 4]) :
        return('колонки')
    else :
        return('колонок')

def rows_word(n_rows: int) :
    if (n_rows % 100 > 10) and (n_rows % 100 < 20) :
        return ('колонок')
    elif (n_rows % 10 == 1) :
        return('строка')
    elif (n_rows % 10 in [2, 3, 4]) :
        return('строки')
    else :
        return('строк')

def match(str, pat: str)-> bool:
	"""
	Compare string with pattern and return True if there is any match.
	It finds only first match.
	Pattern scheme:
		- [a-zA-Z0-9] - one alphabet symbol or digit
		- '*' : any symbols, occur zero or more times
		- '.' : any symbols, occur one or more times
	"""
	def match_aux(str, pat: str, str_pos, pat_pos: int) -> bool:
		while 1:
			if (pat_pos >= len(pat)):
				return (str_pos >= len(str))
			if (pat[pat_pos] == '*') and (str_pos >= len(str)):
				return match_aux(str, pat, str_pos, pat_pos+1)
			if (pat[pat_pos] == '*'):
				for i in range(0, len(str)-str_pos):
					if match_aux(str, pat, str_pos+i, pat_pos+1):
						return True
				return False
			if ((str_pos >= len(str)) or
				((str[str_pos] != pat[pat_pos]) and (pat[pat_pos] != '?'))):
				return False
			str_pos += 1
			pat_pos += 1

	return match_aux(str, pat, 0, 0)


def check_paren(s: str, print_output = True) -> int:
	""" Check the expresson which have parentheses for pair matching.
	"""
	stack = []
	openers = ['(', '{', '[']
	pairs = {')': '(', '}': '{', ']': '['}
	for i in range(len(s)):
		if s[i] in openers:
			stack.append(s[i])
		elif not stack:
			if print_output:
				print(f"Inconsistent bracket at position {i}: '{s[i]}'")
			return False
		else:
			if (pairs[s[i]] != stack.pop()):
				if print_output:
					print(f"Inconsistent bracket at position {i}: '{s[i]}'")
				return False
	if not stack:
		return True
	else:
		if print_output:
			print(f"Inconsistent bracket at position {i}: '{s[i]}'")
		return False


def levenstein(s1, s2: str) -> bool:
	""" Compute Levenstein distance between two strings
	"""
	if not s1:
		return len(s2)
	elif not s2:
		return len(s1)
	L = [[(i + j) if (i*j == 0) else 0 for j in range(len(s2) + 1)]
		 for i in range(len(s1) + 1)]
	for i in range(1, len(s1) + 1):
		for j in range(1, len(s2) + 1):
			if (s1[i-1] == s2[j-1]):
				L[i][j] = L[i-1][j-1]
			else:
				L[i][j] = 1 + min(L[i][j-1], L[i-1][j], L[i-1][j-1])
	return L[-1][-1]


def prefix(s: str, full_array = False):
	""" Prefix-function.
	"""
	if not s:
		if full_array:
			return []
		else:
			return 0
	pref = [0 for i in range(len(s))]
	for i in range(1, len(s)):
		p = pref[i-1]
		while p > 0 and s[i] != s[p]:
			p = pref[p-1]
		if s[i] == s[p]:
			p += 1
		pref[i] = p
	if full_array:
		return pref
	else:
		return pref[-1]

str1 = 'aabaabaaabaaba'
str2 = 'aabaabaaaabaabaaab'


def kmp(sub, s):
	""" Knuth-Morris-Pratt algo realisation.
	Find substring @sub in the string @s and return list of indexes
	where each index corresponds to the symbol, from which symbols in
	@s match all symbols in @sub.
	"""
	if len(sub)*len(s) < 1:
		return []
	F = prefix(sub+'#'+s, True)[len(sub)+1:]
	matches = [
		(i - len(sub))
		for i in range(2*len(sub)+1,len(F))
		if (F[i] == len(sub))
		]
	return matches

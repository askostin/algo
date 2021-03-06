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


# def check_paren(...)
# check the expressin which have parentheses for pair matching

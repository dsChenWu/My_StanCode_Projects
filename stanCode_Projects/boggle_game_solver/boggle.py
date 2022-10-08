"""
File: boggle.py
Name: Jason  Wu
----------------------------------------
TODO: In this python file, user can enter the 4x4 capital,
	  and function will help user to find out all possibility words in dictionary.
	  There is the rule that words can only be found in between.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
N_ROW = 4


def main():
	"""
	Input: Enter the capitals and it forms like 4x4 matrix.
	Output: Print all possibility words in the console and sum up all how many words.
	"""
	lst = []
	for i in range(N_ROW):
		rows = input(str(i+1) + ' row of letters: ').lower()
		if len(rows) != 7:  # Check if user type wrong format.
			print('Illegal input')
			break
		type_word = rows[0] + rows[2] + rows[4] + rows[6]  # Only store the
		lst.append(type_word)
	start = time.time()
	dict_lst = read_dictionary()  # Return a list store all vocabulary in the dictionary.
	find_func(lst, dict_lst)  # Run the recursion function to check the word
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return the list(all_word) which store all vocabulary.
	"""
	with open(FILE, 'r') as f:
		all_word = []
		for line in f:
			all_word.append(line[:-1])
		return all_word


def find_func(boggle_lst, dictionary):
	"""
	:param boggle_lst: 4x4 capital
	:param dictionary: all vocabulary
	"""
	ans = ''
	store_lst = []
	for i in range(len(boggle_lst)):
		for j in range(len(boggle_lst[i])):
			find_func_helper(boggle_lst, dictionary, ans, i, j, [], store_lst)  # Call a helper function for convenient coding.
	print(f"There are {len(store_lst)} words in total.")


def find_func_helper(boggle_lst, dictionary, ans, i, j, current_lst, store_lst):
	'''
	:param boggle_lst: 4x4 capital matrix
	:param dictionary: all vocabulary
	:param ans: compose the word.
	:param i : the index value
	:param j : the index value
	:param current_lst: convenient to store the value.
	:param store_lst: store the finding word in a list.
	Output: print each finding word
	'''

	# Base case
	if len(ans) >= 4:
		if ans not in store_lst:
			if ans in dictionary:
				store_lst.append(ans)
				print(f"Found: {ans}")
				for x in range(-1, 2, 1):  # From line 88 to line 101 just double check the words which it may be missing.
					for y in range(-1, 2, 1):
						if 0 <= (i + x) <= len(boggle_lst) - 1:
							if 0 <= (j + y) <= len(boggle_lst[i]) - 1:
								if (i + x, j + y) not in current_lst:
									current_lst.append((i + x, j + y))
									ans += boggle_lst[i + x][j + y]
									test_word = has_prefix(ans, dictionary)
									if test_word:
										# Explore
										find_func_helper(boggle_lst, dictionary, ans, i + x, j + y, current_lst,store_lst)
									# Un-choose
									current_lst.pop()
									ans = ans[:-1]
	else:
		# Choose
		for x in range(-1, 2, 1):
			for y in range(-1, 2, 1):
				if 0 <= (i + x) <= len(boggle_lst) - 1:
					if 0 <= (j + y) <= len(boggle_lst[i]) - 1:
						if (i+x, j+y) not in current_lst:  # To check if we have found the index.
							current_lst.append((i+x, j+y))
							ans += boggle_lst[i+x][j+y]  # compose the string into ans
							test_word = has_prefix(ans, dictionary)
							if test_word:
								# Explore
								find_func_helper(boggle_lst, dictionary, ans, i+x, j+y, current_lst, store_lst)
							# Un-choose
							current_lst.pop()
							ans = ans[:-1]


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: store all vocabulary in a list.
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

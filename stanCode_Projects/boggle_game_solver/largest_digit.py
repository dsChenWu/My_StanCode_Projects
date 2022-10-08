"""
File: largest_digit.py
Name: Jason Wu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: Input val
	:return: return the maximum value, based on the function, find_largest_digit_help(abs_n, max)
	"""
	abs_n = abs(n)
	max = abs_n % 10  # First val
	numeric = find_largest_digit_help(abs_n, max)  # Call a help function
	if max > numeric:
		return max
	else:
		return numeric


def find_largest_digit_help(abs_n, max):
	next_data = abs_n % 10
	# Base Case
	if abs_n // 10 == 0:
		if max < next_data:
			return next_data
		else:
			return max
	# Recursion
	else:
		return find_largest_digit_help(abs_n // 10, next_data)


if __name__ == '__main__':
	main()

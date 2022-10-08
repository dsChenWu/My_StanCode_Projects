"""
File: anagram.py
Name: Jason Wu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    Input: Introduction the function and let user type the word.
    Output: search the possibility word for all capital possibility combination.
    """
    print("Welcome to stanCode \" Anagram Generator\" (or -1 to quit)")
    while True:
        enter_word = input('Find anagrams for: ')
        if enter_word == EXIT: # Guardian val.
            break
        else:
            start = time.time()
            all_words = read_dictionary()
            find_anagrams(enter_word, all_words)
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    Input: open a txt. file
    Output: Store all words from dictionary into a list, called: dict_all.
    """
    dict_all = []
    with open(FILE, 'r') as f:
        for line in f:
            dict_all.append(line[:-1])  # To store all words from dictionary into a python list.
    return dict_all


def find_anagrams(s, dict_all):
    """
    :param s : The word that user enter
    :param dict_all: The list store all words.
     Creat a helper function to solve the problem
    """
    current_lst =[]
    lst = []
    for ch in s:
        lst.append(ch)  # To split each capital from a word.
    counter = []  # Convenient to calculate.
    find_anagrams_help(s, "", current_lst, lst, dict_all, counter)  # Create a helper function to input more info to solve the problem.
    print(str(len(current_lst)), 'anagrams:', current_lst)  # print all finding words from dictionary.


def find_anagrams_help(enter_string, current_string, current_lst, default_lst, data_base, counter):
    """
    :param enter_string:  == s
    :param current_string: == ""
    :param current_lst: == []
    :param default_lst:  == lst . For example: s = 'stop', so lst = ['s', 't', 'o', 'p']
    :param data_base:  == store all words in a list.
    Output: print a list.
    """
    # Base case
    if len(current_string) == len(enter_string):
        if current_string in data_base:
            print('Searching...')  # To let user know it is still under searching.
            if current_string not in current_lst:
                current_lst.append(current_string)
                print('Found', current_string)
            return current_lst
    # Back-tracking
    else:
        for i in range(len(default_lst)):
            # Choose
            if i not in counter:
                counter.append(i)
                current_string += default_lst[i]
                test_word = has_prefix(current_string, data_base)
                if test_word:
                    # Explore
                    find_anagrams_help(enter_string, current_string, current_lst, default_lst, data_base, counter)
                    # Un-choose
                current_string = current_string[:-1]
                counter.pop()


def has_prefix(sub_s, data_base):
    """
    Input:  To check the sub_s which is in the dictionary or not.
    Output: TO return True or False and convenient to run recursion.
    """
    for word in data_base:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

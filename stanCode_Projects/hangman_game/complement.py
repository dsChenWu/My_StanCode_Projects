"""
File: complement.py
Name: Jason Wu
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Hypothesis: user can only type "A/a", "T/t", "C/c", "G/g"
    """
    Gene = input("Please give me a DNA standard and I'll find the complement: ")
    Gene = build_complement(Gene) # The function will return the corresponding Gene code name.
    print(Gene)


def build_complement(Gene):
    """
    Check user's typing and turn back the corresponding Gene code name.
    """
    Gene_series = ""
    for i in range(len(Gene)):
        code_name = Gene[i]
        if code_name.islower():
            code_name= code_name.upper()
        if code_name == 'A':
            Gene_series += 'T'
        if code_name == 'C':
            Gene_series += 'G'
        if code_name == 'T':
            Gene_series += 'A'
        if code_name == 'G':
            Gene_series += 'C'
    return Gene_series




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

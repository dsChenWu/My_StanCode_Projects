"""
File: similarity.py (extension)
Name: Jason Wu
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    User can only type "A/a", "T/t", "C/c", "G/g".
    The nested for loop can help user to find the best similarity result.
    """
    lon_DNA = input('Please give me a DNA sequence to search: ').upper()
    short_DNA = input('What DNA sequence would you like to match? ').upper()
    len_long_DNA = len(lon_DNA)
    len_short_DNA = len(short_DNA)
    match = 0
    for i in range(len_long_DNA+1 - len_short_DNA):
        in_long_DNA = lon_DNA[i:i + len_short_DNA]  # To pick up the character and length is depended on the length of short DNA.
        a = 0
        for j in range(len(in_long_DNA)):
            if in_long_DNA[j] == short_DNA[j]: # To check if the character which pick up in long_DNA is the same as short_DNA
                a += 1
        if a > match:       # To compare one by one and memorize the best one as match.
            match = a
            x = in_long_DNA
    print('The best match is ' + x)




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

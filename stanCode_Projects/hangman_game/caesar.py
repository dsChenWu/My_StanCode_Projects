"""
File: caesar.py
Name: Jason Wu
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    First: Create new string.(New_ALPHABET)
    Second: to type the secret words.
    Third: use the function (decode) to decipher.
    Last: Print the behind meaning.
    """
    move = int(input("Secret number: ")) # to enter how many times to move the A~Z sting.
    new_alp = replace(ALPHABET, move)   # create new sting (new_alp) for the new sequence of A~Z.
    type = input("What's the ciphered string? ").upper()    # Type the character or sentence and make sure all be upper.
    decipher = decode(type, new_alp, ALPHABET)  # decipher the true meaning.
    print(decipher)


def replace(old_alp, times):
    """
    To create new string.
    """
    new_alp = ""
    for i in range(times):
        new_alp = old_alp[len(old_alp)-1-i] + new_alp  # It will be like "XYZ____".
    new_alp = new_alp + old_alp[0:len(old_alp)-times]   # To add original normally sequence, like: "XYZABC......"
    return new_alp


def decode(type, new_alpha, old_alp):
    """
    To check the place of user's word in new string and check the corresponding character in normal A-Z string.
    """
    ans = ''
    for i in range(len(type)):
        ch = new_alpha.find(type[i])
        true = old_alp[ch]
        if type[i] != new_alpha[ch]:
            ans += type[i]
        else:
            ans += true
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

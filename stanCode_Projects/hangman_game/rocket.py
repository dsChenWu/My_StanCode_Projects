"""
File: rocket.py
Name: Jason Wu
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
    """
    The main function can print the rocket figure.
    Follow the function:
    head()
    belt()
    upper()
    lower()
    belt()
    head()
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()

def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ", end="")
        for j in range(i+1):
            print('/', end="")
        for j in range(i+1):
            print('\\', end="")
        for j in range(SIZE-i):
            print(" ", end="")
        print()
    return


def belt():
    for i in range(1):
        print('+', end="")
        for j in range(2*SIZE):
            print('=',end="")
        print('+', end="")
    print()
    return


def upper():
    for i in range(SIZE):
        for j in range(1):
            print('|', end="")
        for j in range(SIZE-1-i):
            print('.', end="")
        for j in range(i+1):
            print('/',end="")
            print('\\', end="")
        for j in range(SIZE-1-i):
            print('.', end="")
        for j in range(1):
            print('|', end="")
        print()
    return


def lower():
    for i in range(SIZE):
        for j in range(1):
            print('|', end="")
        for j in range(i):
            print('.', end="")
        for j in range(SIZE-i):
            print('\\'+'/', end="")
        for j in range(i):
            print('.', end="")
        for j in range(1):
            print('|', end="")
        print()
    return


def belt():
    for i in range(1):
        print('+', end="")
        for j in range(2*SIZE):
            print('=',end="")
        print('+', end="")
    print()
    return


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ", end="")
        for j in range(i+1):
            print('/', end="")
        for j in range(i+1):
            print('\\', end="")
        for j in range(SIZE-i):
            print(" ", end="")
        print()
    return







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()

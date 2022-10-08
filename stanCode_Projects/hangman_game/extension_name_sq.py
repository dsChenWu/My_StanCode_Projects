"""
File: name_sq.py (extension)
Name: Jason Wu
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    To print a square and each side print the "name".
    """
    print("This program prints a name in a square pattern!")
    name = input('Name: ')
    print(name) #Upper side
    square = produce(name)
    buttom = last(name)


def produce(name):      # Print the right-hand side and left-hand side and do not include the name[0] & name[len(name)-1].
    for i in range(len(name)-2):
        a = ''
        a = name[i + 1] + a
        for j in range(len(name) -2):
            a = a + " "
        a = a +name[len(name)-2-i]
        print(a)
    return


def last(name): # Print the buttom side.
    a = ''
    for i in range(len(name)):
        a = name[i]+a
    print(a)
    return


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

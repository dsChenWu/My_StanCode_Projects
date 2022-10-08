"""
File: hangman.py
Name: Jason Wu
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    It is a hangman game or you can say it is like "Wordle"!!
    You have total 7 chance to guess the word.
    If there is the character in the word, the machine will prompt the place.
    If it is not in the word, the chance will minus 1.
    Enjoy the game ~~~
    """
    x = N_TURNS # Convenient to program
    num = random_word()
    y = num     # Convenient to program
    dashed = first_func(num)    # this function can create the dashed when user start the game.
    ans = dashed    # Convenient to program
    print('The word looks like ' + dashed)
    print('You have ' + str(x) + ' wrong guesses left.')
    guess = input("Your guess: ").upper()  # make it be upper and first time for user to guess
    while x > 0:    # Criteria: When user has the chance >0, user have the chance to guess.
        if guess.isalpha() == False:    # Wrong type of guess, ex: 2
            print('Illegal format')
            guess = input("Your guess: ").upper()  # Make it be upper.
        elif len(guess) != 1:   # Wrong type of guess, ex: cg
            print('Illegal format')
            guess = input("Your guess: ").upper()  # Make it be upper.
        elif num.find(guess) != -1:     # When guess_word is in the the "Word"
            ans = replace(y, ans, '-', guess)   # Create a new string called "ans" and it looks like: --c--- (Example)
            y = change_fun(y,'-', guess)    # This function is to check if the character is more than one times in the "Word".
            print('You are correct!')
            if ans != num:      # If haven't finished find out the "Word", keep guessing.
                print('The word looks like ' + ans)
                print('You have ' + str(x) + ' wrong guesses left.')
                guess = input("Your guess: ").upper()  # make it be upper.
            elif ans == num:    # If finding out the answer, print the "Word" and stop the game.
                print('You win!!')
                print('The word was:' + num)
                break
        else:   # If guess_word is not in the "Word"
            print('There is no ' + guess +"\'s" + ' in the word.')  # Prompt that the guess_word is not in the "Word".
            x -= 1  # Chance -1
            if x != 0:  # If there is still the chance, keep guessing.
                print('The word looks like ' + ans)
                print('You have ' + str(x) + ' wrong guesses left.')
                guess = input("Your guess: ").upper()  # make it be upper.
            else:   # If no chance to guess, stop the game.
                print('You are completely hung : (')
                print('The word was: ' + num)
                break



def first_func(num):
    """
    This fucntion is to create the dashed when user starts the game.
    """
    ans =''
    for i in range(len(num)):
        ans = ans +'-'
    return ans


def replace(num, old_string, old_word, guess):
    """
    In this function: When the guess_word is in "Word"
    create new string to show the place of guess_word in "Word"
    """
    ans = ''
    i = num.find(guess) # GG this step should be modified since there are more than one "O"
    ans = ans +old_string[:i]
    ans = ans +guess
    ans = ans + old_string[i+1:]
    return ans


def change_fun(old_que, change_word, guess):
    """
    This function is to check if the guess_word is more than one times in "Word"
    Make sure when guess_word showing again, it can print right result.
    """
    ans = ''
    a = 0
    for j in range(len(old_que)):
        if guess == old_que[j]:
            a += 1
    if a >1:
        i = old_que.find(guess)
        ans = ans + old_que[:i]
        ans += change_word
        ans += old_que[i+1:]
        return ans
    else:
        return old_que


def random_word():
    """
    This function is randomly assign the num in rang: 0,1,2,3,4,5,6,7,8 and it will base on the criteria to return a "Word"
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

import argparse
from random import randint

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Guess number")
    parser.add_argument('-f', '--floor', metavar='FLOOR', dest='floor', action='store', default=0, type=int)
    parser.add_argument('-t', '--top', metavar='TOP', dest='top', action='store', default=100, type=int)
    parser.add_argument('-g', '--guess', metavar='GUESS', dest='guess', action='store', default=5, type=int)
    args = parser.parse_args()
    floor = args.floor
    top = args.top
    number_of_guess = args.guess
    number = randint(floor, top)
    guess = int(input("What do you guess that number is: "))
    for _ in range(number_of_guess - 1):
        if guess == number:
            print("Wow your are right, you WIN THE GAME")
            break
        elif guess > number:
            print('enter lower number')
            print(f"you have {number_of_guess - 1 - _} chance to guess")
            guess = int(input("What do you guess that number is: "))
        else:
            print('enter higher number')
            print(f"you have {number_of_guess - 1 - _} chance to guess")
            guess = int(input("What do you guess that number is: "))
    else:
        print("Sorry, you lose the game")
        print(f"the number is {number}")

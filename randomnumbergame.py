from random import randint
from sys import argv
def random_number():
    while True:
        try:
            rnd_num = randint(int(argv[1]), int(argv[2]))
            print(f"Okay I am ready. A thought a number from {argv[1]} to {argv[2]}.")
            return rnd_num
        except ValueError:
            print("I accept only numbers, sorry bro restart me.")


def guessing(num):
    guess_time = 0
    while True:
        try:
            guess = int(input("Tell you your guess!: "))
            if guess == num:
                guess_time += 1
                return guess_time
            elif num > guess:
                guess_time += 1
                print(f"Your number: {guess} is smaller than mine. Try again.")
            else:
                guess_time += 1
                print(f"Your number: {guess}  is bigger than mine. Try again.")
        except ValueError:
            print("Try with a number please")
            guess_time += 1


def restart(yesno):
    if yesno.upper() == "Y":
        return True
    return False

def random_number_game():
    while True:
        my_number = random_number()
        guesses = guessing(my_number)
        print(f"You win, my number was {my_number}. You tried {guesses} times.")
        regame = input("Do you want to start over? (Y/N): ")
        if not restart(regame):
            break
if __name__ == '__main__':
    random_number_game()
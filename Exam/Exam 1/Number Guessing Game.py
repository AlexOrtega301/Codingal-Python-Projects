from random import randint
import sys 
number = randint(1, 50)
guess = None
hearts = 10
while guess != number and hearts > 0:
    guess = int(input("Guess a number between 1 and 50: "))
    hearts -= 1
    if guess < number:
        print("Guess too low!!! Try Again! you have " + str(hearts) + " hearts left.")
        if abs(guess - number) >= 20:
            print("🧊 ice cold!")
        elif abs(guess - number) >= 10:
            print("🥶 Still Cold!")
        elif abs(guess - number) >= 5:
            print("🌡️ Getting Warmer!")
        elif abs(guess - number) < 5:
            print("🔥 Hot! You're very close!")
    elif guess > number:
        print("Guess too high!!! Try Again! You have " + str(hearts) + " hearts left.")
        if abs(guess - number) >= 20:
            print("🧊 ice cold!")
        elif abs(guess - number) >= 10:
            print("🥶 Still Cold!")
        elif abs(guess - number) >= 5:
            print("🌡️ Getting Warmer!")
        elif abs(guess - number) < 5:
            print("🔥 Hot! You're very close!")
    elif guess == number:
        print(f"Congratulations! You've guessed the number {number} correctly!")
        sys.exit()
    if hearts == 0:
        print(f"You've run out of hearts! The number was {number}. Better luck next time!")
        sys.exit()

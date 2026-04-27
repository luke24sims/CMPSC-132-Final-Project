import random

def play_game():
    attempts = 0
    number = random.randint(0, 100)

    print("Welcome to the number guessing game! Try to guess a number 1-100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue
 
        attempts += 1

        if guess == number:
            print("Congratulations! You guessed the number in "+str(attempts)+" attempt(s)!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

play_game()

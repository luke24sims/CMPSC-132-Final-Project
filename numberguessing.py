import random

def get_temperature(difference):
    """Return a temperature based on how close the guess is"""
    if difference <= 10:
         return "HOT!"
    elif difference <= 20:
        return "Warmer..."
    elif difference <= 30:
        return "Cold."
    else:
        return "ICE COLD!"
    
def play_game():
    attempts = 0
    number = random.randint(0, 100)

    print("Welcome to the number guessing game! Try to guess a number 1-100.")
    print("After each guess, I'll tell you:")
    print("HOT — within 10")
    print("Warmer — within 20")
    print("Cold — within 30")
    print("ICE COLD — more than 30 away")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue
 
        attempts += 1
        difference = abs(guess - number)

        if guess == number:
            print("Congratulations! You guessed the number in "+str(attempts)+" attempt(s)!")
            break
        else:
            direction = "Too High! Go lower." if guess > number else "Too Low! Go higher."
            temperature = get_temperature(difference)
            print(f"{direction} | {temperature}\n")

play_game()
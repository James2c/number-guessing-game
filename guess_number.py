import random

# Number guessing game and keeping track and number of attempts
def main():
    attempts = 0
    number_to_guess = random.randint(1, 100)

    while True:
        guess = int(input("Enter your guess beteen 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low, try again.")
        elif guess > number_to_guess:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries")
            break


main()
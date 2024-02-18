import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")

    low, high = 1, 100
    user_feedback = None

    while user_feedback != 'c':
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        
        user_feedback = input("Is my guess too high (h), too low (l), or correct (c)? ").lower()

        if user_feedback == 'h':
            high = guess - 1
        elif user_feedback == 'l':
            low = guess + 1
        elif user_feedback != 'c':
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

    print(f"Hooray! I guessed your number {guess} correctly!")

if __name__ == "__main__":
    guess_number()

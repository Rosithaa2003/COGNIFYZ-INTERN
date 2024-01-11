import random

def number_guessing_game(min_range, max_range):
    
    secret_number = random.randint(min_range, max_range)
    
    print(f"Welcome to the Number Guessing Game! I've selected a number between {min_range} and {max_range}. Try to guess it!")
    
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    min_range = int(input("Enter the minimum range: "))
    max_range = int(input("Enter the maximum range: "))
    
    number_guessing_game(min_range, max_range)

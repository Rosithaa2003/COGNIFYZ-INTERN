import random
random_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("I have selected a random number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == random_number:
        print(f"Congratulations! You guessed the correct number {random_number} in {attempts} attempts.")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

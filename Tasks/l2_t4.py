def generate_fibonacci_sequence(n):
   
    fibonacci_sequence = [0, 1]

   
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence


n = int(input("Enter the number of Fibonacci terms you want to generate: "))


if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci_sequence(n)
    print(f"Fibonacci sequence up to {n} terms:")
    print(fibonacci_sequence)

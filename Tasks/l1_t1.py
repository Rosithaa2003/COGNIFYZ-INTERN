def reverse_string(input_string):
    # Use slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string

# Test the function
input_string = "hello"
reversed_result = reverse_string(input_string)
print(reversed_result)

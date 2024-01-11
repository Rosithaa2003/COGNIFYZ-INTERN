def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")

if unit.upper() == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} degrees Celsius is equal to {converted_temperature} degrees Fahrenheit.")
elif unit.upper() == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature} degrees Celsius.")
else:
    print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

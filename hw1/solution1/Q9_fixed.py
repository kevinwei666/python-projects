"""
Converts a temperature in celsius to a temperature in fahrenheit.
Asks the user for a temperature in celsius and prints it in fahrenheit.

"""

#Get user input of temp in C
C = float(input('What is the temperature in celsius? '))

#Convert to F
F = 9/5 * C + 32
print("The temperature in fahrenheit is", F)


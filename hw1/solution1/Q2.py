"""
Gets user input of x and y and prints a concatenated string with the values.
No arithemetic is performed with the x operand since its treated as a str value.
y is cast to an int so arithmetic with the y operand will return a number.

The str value of x is printed as is.
The int value of y is multiplied by 2, printing it as such.

Examples:
x = 2
y = 3
Prints: 262

x = two
y = 3
Prints: two6two

"""

#Get user input
x = input('give me an input please' )
y = input('give me another ')

#Cast y to int
y = int(y)

#Print concatenated string
print(x + str(2 * y) + x)

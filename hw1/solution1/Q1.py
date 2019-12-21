"""
Gets user input of x and y and prints a concatenated string with the values.
No arithemetic is performed since operands are treated as str values.

The str value of x is printed as is.
The str value of y is multiplied by 2, printing it twice.

Examples:
x = 2
y = 3
Prints: 2332

x = 2
y = three
Prints: 2threethree2

"""

#Get user input
x = input('give me an input ')
y = input('give me another input ')

#Print concatenated string
print(x + (2 * y) + x)


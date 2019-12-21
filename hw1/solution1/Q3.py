"""
Asks a user to input an integer.  The program checks if the user entered an integer,
then checks to see if the integer is even or odd.
Prints the word 'Even' if even and the word 'Odd' if odd.

"""

#Get user input
num = input("Input an integer: ")

try:
    num = int(num)

    #Test for even
    if (num % 2 == 0):
        print("Even")
    #Test for odd
    else:
        print("Odd")
except ValueError as e:
    print(num +  " is not an integer")
    

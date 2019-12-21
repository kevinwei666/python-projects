"""
Asks the user to input a positive integer.  The program checks if the user entered an integer.

If the number is divisible by 3, prints ’Fizz’. If the number is divisible by 5, prints ’Buzz’.
If the number is divisible by 3 and 5, prints ’Fizz Buzz’.
If none of these conditions are satisfied, prints the number itself.

Examples:
6 prints 'Fizz'
25 prints 'Buzz'
15 prints 'Fizz Buzz'
4 prints '4'

"""

#Get input from user
pos_int = input("Enter a positive integer: ")

#Tests for int
if (pos_int.isnumeric()):

    #Casts to int
    pos_int = int(pos_int)
    
    #Tests for positive int
    if (pos_int > 0):
        #Divisible by 3 and 5
        if ((pos_int % 3 == 0) and (pos_int % 5 == 0)):
            print('Fizz Buzz')
        #Divisible by 3 
        elif (pos_int % 3 == 0):
            print('Fizz')
        #Divisible by 5
        elif (pos_int % 5 == 0):
            print('Buzz')
        #None of the above
        else:
            print(pos_int)

    

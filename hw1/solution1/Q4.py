"""
Asks the user to input an integer.  The program checks if the user entered an integer,
then checks to see if the integer is within 10 (10 is included) of 100 or 200.
If that is the case, prints ‘Yes’, else prints ‘No’.

Examples:
90 should print 'Yes'
209 should also print 'Yes'
189 should print 'No'

"""

#Get user input
num = input("Enter an integer: ")

try:
    num = int(num)
    
    #Checks to see if int is within 10 of 100 or 200
    if ((90 <= x <= 110) or (190 <= x <= 210)):
        print('Yes')
    else:
        print('No')
except ValueError as e:
    print(num + " is not an integer")
    print(e)
    



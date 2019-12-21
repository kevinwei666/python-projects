"""
Asks the user for two integers.  If both values are in the range 30 to 40 (inclusive)
or if both values are in the range 40 to 50 (inclusive), print "Yay" else print "Nay"

"""

#Get user input
val1 = (input("Input value 1: "))
val2 = (input("Input value 2: "))

try:
    val1 = int(val1)
    val2 = int(val2)

    #If both within the range of 30 - 40 or 40 - 50
    if (((30 <= val1 <= 40) and (30 <= val2 <= 40)) or
        ((40 <= val1 <= 50) and (40 <= val2 <= 50))):
        print("Yay")
    else:
        print("Nay")
except:
    print("Input is not valid")
    
    

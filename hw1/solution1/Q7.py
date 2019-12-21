"""
Calculates a dog’s age from a human age.
Asks the user for their age and allows for float values.
For the first 2 years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years.
Print the result in the format: "The human's age in dog years is ..." 

If the user enters a negative age,
prints "Age must be a positive number." instead of the dog's age.

"""

#Get human age
h_age = input("Input human years: ")

try:
    h_age = float(h_age)

    #If user enters negative number
    if h_age < 0:
        msg = "Age must be a positive number."
    #Calculates dog's age
    else: 
        #If human is 2 years old or younger
        if h_age <= 2: 
            d_age = h_age * 10.5
        #If human is 3 years old or older
        else:
            #Subtract 2 from human age, add 21 dog years to account for the 2
            #Multiply the rest by 4
            d_age = 21 + (h_age - 2) * 4
            
        msg = "The human's age in dog years is {}".format(d_age)

    print(msg)
    
except:
    print(h_age, "is not a valid age") 
    

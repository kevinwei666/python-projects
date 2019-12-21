"""
CIT 590: Fall 2018 Homework 2

This homework deals with the following topics:

- loops
- functions

This HW deals primarily with loops and functions.
It will introduce you to some interesting number theory as well.
You have probably heard of prime numbers and composite numbers before,
but have you ever heard of abundant numbers, or narcissistic numbers?

This assignment will teach you how to write code to identify different kinds number properties.
We also want you to learn how to reuse code in this assignment.
This is a basic strategy for reducing complexity in a program.
Why?  Because things change, and if you have the same thing in several places,
when you change one, you have to change all the others.
And you can’t always find them all!

In order to reuse code, you must take common pieces of code and put them into functions.
Failure to do so will result in loss of points.
You will submit just one file for this assignment called numberProperties.py.
We also want you to add comments to your code and docstrings to your functions.

You can assume that all inputs in this assignment will be positive integers.

"""

def getFactors(x):
    """Returns all factors of given number x.

    """
    factors = []

    #find the possible factors, check for division by numbers 1 to x
    #find the numbers between 1 and x that divide x evenly
    for i in range(1, x + 1):
        if (x % i == 0):
            factors.append(i)

    #another easier way to return a list of factors of x
    #factors = (i for i in range(1, x + 1) if x % i == 0)
       
    return factors


def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    """
    if x > 1:
        
        for n in range(2, x):
            if x % n == 0:
                return False

        return True
    
    return False


def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    """
    if x > 1:
        #If it's not prime, it's composite
        return not isPrime(x)

    return False


def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.

    """
    if x > 0:
        #get all factors
        factors = getFactors(x)

        #remove x itself from list of factors
        if (x in factors): factors.remove(x)

        #get sum of all factors
        factors_sum = 0
        for factor in factors: factors_sum += factor

        #If x is the sum of all factors, it's perfect
        return x == factors_sum

    return False


def isPerfect_v2(x):
    """Returns whether or not the given number x is perfect.

    V2: Gets the sum of the list of factors of x.

    """
    if x > 0:

        #add to a new list, for each i in 1 to x (not including x),
        #if i evenly divides x
        #get the sum of all values in the list
        new_list = (i for i in range(1, x) if x % i == 0)

        #If x is the sum of all factors, it's perfect
        return x == sum(new_list)
            
    return False

    
def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.

    """
    #get all factors
    factors = getFactors(x)
    
    #remove x itself from list of factors
    if (x in factors): factors.remove(x)

    #get sum of all factors
    factors_sum = 0
    for factor in factors: factors_sum += factor

    #If x is less than the sum of all factors, it's abundant
    return x < factors_sum


def isAbundant_v2(x):
    """Returns whether or not the given number x is abundant.

    V2: Gets the sum of the list of factors of x,

    """
    #add to a new list, for each i in 1 to x (not including x),
    #if i evenly divides x
    #get the sum of all values in the list
    new_list = (i for i in range(1, x) if x % i == 0)

    #If x is less than the sum of all factors, it's abundant
    return x < sum(new_list)

def isTriangular(x):
    """Returns whether or not a given number x is triangular.

    Calls getTriangular.

    """
    if x > 0:

        tri, pos = getTriangular(x)
        return tri
    
    return False


def getTriangular(x):
    """Returns whether or not a given number x is triangular and the position of the triangular number. (As a tuple)

    If it's not triangular, it returns 0 for position.

    The triangular number Tn is a number that can be represented in the form of a triangular grid of
    points where the first row contains a single element and
    each subsequent row contains one more element than the
    previous one.

    We can just use the fact that the nth triangular
    number can be found by using a formula: Tn = n(n + 1) / 2.

    Example: 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)

    """
    i = 1
    while (i * (i + 1) / 2 <= x):
        if (i * (i + 1) / 2 == x):
            return True, i

        i = i + 1
            
    return False, 0


def isTriangular_v2(x):
    """Returns whether or not a given number x is triangular.

    V2: An integer x is triangular if and only if 8x + 1 is a perfect square.

    """
    if x > 0:

        #An integer x is triangular if and only if 8x + 1 is a square
        y = (8 * x) + 1
        
        #Calculate sqrt, this will return float
        z = y ** 0.5
        
        #Round values, then mutiply by itself to test for perfect sqr
        z_sqrd_rounded = (round(z) * round(z))
        
        return y == z_sqrd_rounded
    
    return False
    

def isTriangular_v3(x):
    """Returns whether or not a given number x is triangular.

    V3: Triangular numbers are equal to the sum of the n natural numbers from 1 to n.

    """
    if x > 0:

        #triangular numbers are equal to the sum of the n natural numbers from 1 to n
        sum_numbers = 0
        i = 1
        while (sum_numbers <= x):
            sum_numbers += i
            
            if (sum_numbers == x):
                return True

            i = i + 1
            
    return False

def isPentagonal(x):
    """Returns whether or not a given number x is pentagonal.  Also
    checks the position of the triangular numbers and compares it to the position
    of the pentagonal number.

    Every pentagonal number is 1/3 of a triangular number.  More specifically,
    the nth pentagonal number is one-third of the 3n−1th triangular number.
    
    Example Pentagonal Numbers: 1, 5, 12, 22, 35, 51, 70 ...
    Example: 5 --> 2nd position: (3 * 2 - 1 = 5th position) --> 15

    Tests potential triangular number, gets potential position, gets factors and
    possible values of n, then compares to pentagonal position.
        
    """

    #calculate potential triangular number
    pot_triangular_num = (3 * x)

    #determine if it's potentially triangular
    if isTriangular(pot_triangular_num):
    
        #The position of a triangular number: Tn = n(n*1) / 2
        #Example, for triangular number 15, 15 = n(n*1) / 2
        #Or, 30 = n(n*1)
        location = pot_triangular_num * 2
        location_factors = getFactors(location)
        
        for i in range(0, len(location_factors) - 2):
            if (location_factors[i] * location_factors[i + 1] == location
                and location_factors[i + 1] == location_factors[i] + 1):

                #The triangular position, n, is the first factor, location_factors[i]
                pot_triangular_pos = location_factors[i]
                
                #Use the triangular position to get the potential pentagonal position
                pot_pentagonal_pos = (pot_triangular_pos + 1) / 3

                #Compare the the triangular position to the pentagonal position
                return (3 * round(pot_pentagonal_pos)) - 1 == pot_triangular_pos
            
    return False

def isPentagonal_v2(x):
    """Returns whether or not a given number x is pentagonal.  Also
    checks the position of the triangular numbers and compares it to the position
    of the pentagonal number.

    Every pentagonal number is 1/3 of a triangular number.  More specifically,
    the nth pentagonal number is one-third of the 3n−1th triangular number.
    
    Example Pentagonal Numbers: 1, 5, 12, 22, 35, 51, 70 ...
    Example: 5 --> 2nd position: (3 * 2 - 1 = 5th position) --> 15

    Tests potential triangular number and gets triangular number positon.
    Compares to pentagonal position.
    
    """
    #calculate potential triangular number
    pot_triangular_num = (3 * x)

    #determine if it's trinagular, and it's triangular position
    tri, pos = getTriangular(pot_triangular_num)

    #if triangular
    if (tri == True):
        #compare the position to the pentagonal number position
        pot_pentagonal_pos = (pos + 1) / 3

        return (3 * round(pot_pentagonal_pos)) - 1 == pos

    return False

def isHexagonal(x):                       
    """Returns whether or not a given number is hexagonal.

    A hexagonal number can be expressed in the
    form 2n^2 − n. The nth hexagonal number will be the number of points
    in a hexagon with n regularly spaced points on a side.

    Examples: 1, 6, 15, 28, 45, 66
    Example: 2 * (1 ^ 2) - 1 = 1
    Example: 2 * (2 ^ 2) - 2 = 6
    Example: 2 * (3 ^ 2) - 3 = 15

    """
    i = 1
    while (2 * (i ** 2) - i <= x):
        if (2 * (i ** 2) - i == x):
            return True

        i = i + 1
            
    return False


def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.

    """
    if x > 0:

        #convert number to string
        x_str = str(x)

        #power is number of 'digits'
        power = len(x_str)
        
        digit = 0
        sum_digits = 0
        for n in x_str:

            #convert to number
            digit = int(n)

            #raise to power and add to overall sum
            sum_digits += (digit ** power)

        return sum_digits == x

    return False
    
def main():

    playing = True
    while playing == True:
    
        num_input = input('Give me a number from 1 to 10000.  Type -1 to exit. ')

        try:
            num = int(num_input)
            
            if (num == -1):
                playing = False
                continue

            if isPrime(num):
                print(str(num) + ' is prime')
            if isComposite(num):
                print(str(num) + ' is composite')
            if isPerfect(num):
                print(str(num) + ' is perfect')
            if isPerfect_v2(num):
                print(str(num) + ' is perfect (v2)')
            if isAbundant(num):
                print(str(num) + ' is abundant')
            if isAbundant_v2(num):
                print(str(num) + ' is abundant (v2)')
            if isTriangular(num):
                print(str(num) + ' is triangular')
            if isTriangular_v2(num):
                print(str(num) + ' is triangular (v2)')
            if isTriangular_v3(num):
                print(str(num) + ' is triangular (v3)')
            if isPentagonal(num):
                print(str(num) + ' is pentagonal')
            if isHexagonal(num):
                print(str(num) + ' is hexagonal')
            if isNarcissistic(num):
                print(str(num) + ' is narcissistic')
                    
        except:
            print('Sorry, the input is not an int.  Please try again.')
        
if __name__ == '__main__':
    main()

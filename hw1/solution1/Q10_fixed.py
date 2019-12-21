"""
Given the following coefficients: 1, 3, 1
Solves the quadratic equation: ax^2 + bx + c
Rounds to 6 decimal places.

#Overview of quadratic formula
#https://en.wikipedia.org/wiki/Quadratic_formula

#Solutions can be checked here:
https://www.calculatorsoup.com/calculators/algebra/quadratic-formula-calculator.php

"""

#Define coefficients
a, b, c = 1, 3, 1

#Solve for d
d = (b ** 2) - (4 * a * c)

#Is negative
if d < 0:
    print('no solution')
#Is  0
elif d == 0:
    print(-b / (2 * a))
#Otherwise, calculate solutions
else:
    solution1 = (-b + (d ** 0.5)) / (2 * a)
    solution2 = (-b - (d ** 0.5)) / (2 * a)
    print(round(solution1, 6))
    print(round(solution2, 6))


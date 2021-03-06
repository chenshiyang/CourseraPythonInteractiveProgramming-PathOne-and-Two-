## Question 1
# An if statement can have how many elif parts?
# Solution : Unlimited

## Question 2
# Consider the Boolean expression not (p or not q). 
# Give the four following values in order, separated
# only by spaces:
# the value of the expression when p is True, and q is True,
# the value of the expression when p is True, and q is False,
# the value of the expression when p is False, and q is True,
# the value of the expression when p is False, and q is False,

# Solution : False False True False

## Question 3
# def do_stuff():
#    print "Hello world"
#    return "Is it over yet?"
#    print "Goodbye cruel world!"
#    
# print do_stuff()

# Solution : 
# Hello world
# Is it over yet?

## Question 4
# Given a non-negative integer n, which of the 
# following expressions computes the ten's digit of n? 
# For example, if n is 123, then we want the expression 
# to evaluate to 2.
# Solution : ((n - n % 10) % 100) / 10
# (n % 100 - n % 10) / 10

## Question 5
# The function calls random.randint(0, 10) and random.
# randrange(0, 10) generate random numbers in different 
# ranges. What number can be generated by one of these 
# functions, but not the other? 
# Solution :10 (refer to the python docs)

## Question 6
def function1(x):
    y = -5 * x**5 + 69 * x ** 2 - 47
    return y
print(function1(0))
print(function1(1))
print(function1(2))
print(function1(3))


## Question 7
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    future_value = present_value * (1 + rate_per_period) ** periods
    return future_value
print "$1000 at 2% compounded daily for 3 years yields $",future_value(1000, .02, 365, 3)


## Question 8
import math
def polygon_area(sides_number, sides_length):
    area = 0.25 * sides_number * sides_length ** 2 / (math.tan(math.pi / sides_number))
    return area
print polygon_area(7, 3)

## Question 9
# Running the following program results in the error 
# SyntaxError: bad input on line 8 ('return'). Which 
# of the following describes the problem?

# Solution : incorrect indentation

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

## Question 10
# The following code has a number of syntactic errors 
# in it. The intended math calculations are correct, so 
# the only errors are syntactic. Fix the syntactic 
# errors.
# Solution �� The right code is as follows:
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)
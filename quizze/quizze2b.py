## Question 1
# Solution :¡¡width of the button

## Question 2
# How many control objects are allowed in a frame?
# Solution : Unlimited.

## Question 3
# 
#import simplegui
#simplegui.create_frame("my frame", 200, 200)
#simplegui.add_label("My label")
# Solution : 
import simplegui
f = simplegui.create_frame(...)
label = f.add_label("My label")
label.set_text("My new label")

import simplegui
f = simplegui.create_frame(...)
f.add_label("My label")

## Question 4
# When you enter text into an input field and press enter, the text is passed to the 
# input field's event handler. What is the data type of the text?
#Solution : a string

## Question 5
# Consider the following conditional statement.
# Solution : return p and q

## Question 6
# Which of the following describes the mistake in the following code?
# Solution : The function should return, not print, its result.

## Question 7
# What kind of errors can happen if you are missing a needed global 
# declaration in one of your function definitions? For this question, 
# you need only consider the case where the problem is in the 
# function that is missing the global declaration.
# Solution : Error: local variable '¡­' referenced before assignment   
# An incorrect computation that generates no error message

## Question 8
# Which of the following function definitions are in the recommended code style?
# Solution : 
def my_function(x, y):
    """ Add the two inputs. """
    return x + y

## Question 9 
# Solution : Add an assignment to count in the event handler for the input 
# field. Also add a global count declaration there.

# Question 10
# In the game ¡°Guess the number¡±, what is the minimum number of guesses necessary 
# to guarantee that the guesser can always win if the secret number is chosen in range(0, 400)? 
# Solution : 9 guesses.

## Question 1
#What typically calls an event handler?
# Solution : Some code that you didn't write which generates the event


## Question 2
# In CodeSkulptor, how many event handlers can be running at the same time?
# Solution : unlimited

## Question 3
#　What are the three parts of a frame?
# Solution: Control area, status area, canvas

## Question 4
# For the SimpleGUI-based programs in this course, we recommended breaking down an interactive Python program into seven parts. Below, these parts are listed alphabetically.
# Solution : 4523167

## Question 5
# Solution : function a c d nedds global declaration

## Question 6
# Solution : 4

count = 0

def square(x):
    global count
    count += 1
    print "count in square :", count
    return x**2

print square(square(square(square(3))))
print count

## Question 7
# which names occur in the global scope
# Solution : a b f 
#a = 3
#b = 6

#def f(a):
#    c = a + b
#    return c

## Question 8
# Which names occur in a local scope
# Solution : a c
a = 3
b = 6

def f(a):
    c = a + b
    return c
f(7)

## Question 9
# Which of the following are valid calls to create_frame?
# Solution : frame = simplegui.create_frame("Testing", 200, 200, 300)
# f = simplegui.create_frame("My Frame", 100, 100)

## Question 10
# If the following is our entire program, what one line of code should replace the question marks for it to show a frame?
# Solution : import simplegui

import simplegui
frame = simplegui.create_frame("My Frame", 100, 100)
frame.set_canvas_background("#FF")
frame.start()
## Question 1 
# What Python operator takes two strings (e.g., "sun" and "rise") and forms the combination of these two strings, one followed by the other (e.g., "sunrise")?
# Solution : +

## Question 2
# What does the draw handler parameter represent?
# Solution : The canvas

## Question 3
# What happens if you draw text outside the canvas coordinates?
# Solution : Some or none of the text is shown. Conceptually, the text is drawn at whatever coordinates are given, but only whatever text fits within the canvas coordinates is shown.

## Question 4
# Assume we have a canvas that is 200 pixels wide and 300 pixels high. We want to draw a green line between the upper left corner and the lower right corner. Which of the following calls will accomplish this?
# Solution £º canvas.draw_line((199, 299), (0, 0), 10, "Green")

## Question 5
# 
def date(month, day):
    """
    Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day.
    """
    return month + "/" + day

print date(2, 12)

# Solution : str(month) + "/" + str(day)

## Question 6
# Assume we have a variable word that contains a string, such as "Mississippi" or "indivisible". We would like to determine how many "i"'s are in the string word. What code should replace the question marks in the following function definition?

def number_of_i(word):
    """Returns the number of lower-case i's in the word."""
    return ???
    
# Solution : word.count("i")

## Question 7
# Where should your draw_text, draw_line, and similar drawing calls be?
# Solution : In a draw handler, or a helper function called from it

## Question 8
# Which of the following function calls are valid, i.e., don't lead to an error?
# Solution £º float("5.4") int("5")

## Question 9
# Turn the following description into a CodeSkulptor program, and run it.

#Create a 300-by-300 canvas.
#Draw two circles with radius 20 and white lines of width 10. One is centered at (90,200) and one at (210,200).
#Draw a red line of width 40 from (50,180) to (250,180).
#Draw two red lines of width 5 from (55,170) to (90,120) and from (90,120) to (130,120).
#Draw a red line of width 140 from (180,108) to (180,160).

# Solution : a automobile
import simplegui

def draw_handler(canvas):
    canvas.draw_circle([90, 200], 20, 10, "White")
    canvas.draw_circle([210, 200], 20, 10, "White")
    canvas.draw_line([50, 180], [250, 180], 40, "Red")
    canvas.draw_line([55, 170], [90, 120], 5, "Red")
    canvas.draw_line([90, 120], [130, 120], 5, "Red")
    canvas.draw_line([180, 108], [180, 160], 140, "Red")
    

frame = simplegui.create_frame("my_frame", 300, 300)
frame.set_draw_handler(draw_handler)
frame.start()

## Question 10
# The following is a diagram of an archery target.
## Solution : Largest first
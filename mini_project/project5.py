# implementation of card game - Memory

import simplegui
import random

#global variables
cards = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
exposed = [False] * 16
last_three_click = [-1, -1, -1]
status = turns = 0

# helper function to initialize globals
def new_game():
    global status, turns, exposed, last_three_click
    random.shuffle(cards)
    status = turns = 0
    label.set_text("Turns = " + str(turns))
    exposed = [False] * 16
    last_three_click = [-1, -1, -1]
     
# define event handlers
def mouseclick(pos):
    global status, turns
    # add game state logic here
    index = pos[0] / 50
    if exposed[index]:
        return
    last_three_click[0] = last_three_click[1]
    last_three_click[1] = last_three_click[2]
    last_three_click[2] = index
    if index == last_three_click[1]:#if this click is the same as last click, unvalid click
        return
    if status == 0:
        exposed[index] = True
        status = 1
    elif status == 1:
        exposed[index] = True
        status = 2
        turns += 1
        label.set_text("Turns = " + str(turns))
        print turns        
    elif status == 2:
        if cards[last_three_click[0]] != cards[last_three_click[1]]:
            exposed[last_three_click[0]] = exposed[last_three_click[1]] = False
        exposed[index] = True
        status = 1  
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        canvas.draw_polygon([[i * 50, 0], [i * 50, 100], [(i + 1) * 50, 100], [(i + 1) * 50, 0]], 2, 'Yellow', 'Green')
        if exposed[i]:
            canvas.draw_polygon([[i * 50, 0], [i * 50, 100], [(i + 1) * 50, 100], [(i + 1) * 50, 0]], 2, 'Yellow', 'Silver')
            canvas.draw_text(str(cards[i]), [i * 50 + 19, 65], 30, "Black")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

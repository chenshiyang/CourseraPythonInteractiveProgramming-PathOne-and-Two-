import random
import simplegui
import math

#global variables
secret_number = 7
# the low bound
min = 0
# the up bound
max = 100
# chance remains
chance = 5
# difficuly level
# 1 indicates easy
# 2 indicates normal
# 3 indicates hard
level = 1
# helper function to start and restart the game
def new_game():
    ''' start a new game and reset the secret number'''
    global secret_number, chance
    secret_number = random.randrange(min, max)
    chance = int(math.log(max - min, 2) - level + 2)
    if chance <= 0 :
        chance = 1
    print ''
    print '*******************************\n*\tNew game start!       *\n*******************************' 
    print 'Please guess from ' + str(min) +' to ' + str(max)
    print 'You have ' + str(chance) + ' chances remain.'
    print ''
    
# define event handlers for control panel
def range100():
    '''button that changes the range to [0,100) and starts a new game '''
    global min, max
    min = 0
    max = 100

    #print 'Game start. The range is now 0-100'
    new_game()

def range1000():
    '''button that changes the range to [0,1000) and starts a new game '''
    global min, max
    min = 0
    max = 1000

    #print 'Game start. The range is now 0-1000'
    new_game()

def set_up_bound(num):
    '''Set the up bound'''
    number = int(num)
    if number <= min :
        print 'Up bound must larger than current low bound ' + str(min)
    else :
        global max
        max = number

        #print 'The range is now ' + str(min) + ' to ' + str(max)
        #print ''
        new_game()
        
def set_low_bound(num):
    '''Set the low bound '''
    number = int(num)
    if number >= max :
        print 'Low bound must smaller than current up bound ' + str(max)
    else :
        global min
        min = number

        #print 'The range is now ' + str(min) + ' to ' + str(max)
        #print ''
        new_game()
        
def set_difficulty(diffString):
    '''Set the difficulty of the game.
    1 as easy
    2 as normal
    3 as hard'''
    global level
    level = int(diffString)
    if level == 1 :
        print 'The level is current easy'
    elif level == 2 :
        print 'The level is current normal'
    elif level == 3 :
        print 'The level is current hard'
    else :
        level = 1 # invalid difficulty set, use default value
        print 'invalid difficulty input, use default level : easy'
    new_game()
    
def input_guess(guess):
    '''compare the guess number with the secret number and output the result
    information'''
    global chance
    chance = chance - 1
    guess_number = int(guess)
    win = 0
    print 'You guess ' + guess + ', You have ' + str(chance) + ' chances left'
    if secret_number > guess_number :
        print 'Higher'
    elif secret_number < guess_number :
        print 'Lower'
    else :
        print 'Bingo, you win!'
        win = 1
        new_game()
    if win == 0 and chance <= 0 :
        print 'You lose.'
        new_game()
        
# create frame
my_frame = simplegui.create_frame('Game', 200, 300)
my_frame.add_button('Range 0-100', range100, 200)
my_frame.add_button('Range 0-1000', range1000, 200)
my_frame.add_button('Restart', range100, 200)
my_frame.add_input('Set new up bound', set_up_bound, 200)
my_frame.add_input('Set new low bound', set_low_bound, 200)
my_frame.add_input('Choose difficulty from 1-3', set_difficulty, 200)
my_frame.add_input('Input guess here', input_guess, 200)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
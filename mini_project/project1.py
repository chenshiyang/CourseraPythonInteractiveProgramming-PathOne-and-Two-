# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    value = -1
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        value = 0
    elif name == 'Spock':
        value = 1
    elif name == 'paper':
        value = 2
    elif name == 'lizard':
        value = 3
    elif name == 'scissors':
        value = 4
    else:
        print 'name invalid'
    return value

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    name = 'unknow'
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print 'number invalid'
    return name

def rpsls(player_choice): 
    
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print 'Player chooses  ' + player_choice 
    
    # convert the player's choice to player_number 
    #using the function name_to_number()
    player_number = name_to_number(player_choice)
    if player_number <0 or player_number > 4:
        print 'player number invalid'
        return
    
    # compute random guess for comp_number using 
    #random.randrange()
    comp_number = random.randrange(0, 5)
    
    # convert comp_number to comp_choice using 
    #the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice
    
    # compute difference of comp_number and 
    #player_number modulo five
    result = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, 
    #print winner message
    if result == 0:
        print 'Tie!'
    elif result <= 2:
        print 'Player wins!'
    else:
        print 'Computer wins'

# test for name_to_number
def test4name2number():
    print name_to_number('rock') == 0
    print name_to_number('Spock') == 1
    print name_to_number('paper') == 2
    print name_to_number('lizard') == 3
    print name_to_number('scissors') == 4
    print name_to_number('milk') == 1
test4name2number()

# test for number_to_name
def test4number2name():
    print number_to_name(0) == 'rock'
    print number_to_name(1) == 'Spock'
    print number_to_name(2) == 'paper'
    print number_to_name(3) == 'lizard'
    print number_to_name(4) == 'scissors'
    print number_to_name(-1) == 'rock'
test4number2name()
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("Milk")

# always remember to check your completed program against the grading rubric



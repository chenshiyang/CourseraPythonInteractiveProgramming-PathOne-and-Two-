# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
last_outcome = ""
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def draw_back(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        res = 'Hand contains '
        if len(self.cards) == 0:
            return res + 'no card.'
        for card in self.cards:
            res += str(card) + ' '
        return res

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        has_ace = False
        self.value = 0
        for card in self.cards:
            self.value += VALUES.get(card.rank)
            if card.rank == 'A':
                has_ace = True
        if not has_ace:
            return self.value
        elif self.value + 10 <= 21:
            self.value += 10
            return self.value
        else:
            return self.value
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.cards:
            card.draw(canvas, (i * CARD_SIZE[0] + pos[0], pos[1]))
            i += 1
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(suit, rank))  

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        res = 'The deck has '
        for card in self.cards:
            res += str(card) + ','
        return res

#define event handlers for buttons
def deal():
    global outcome, in_play, score, player, dealer, deck, last_outcome
    if in_play:
        score -= 1
        last_outcome = 'You lost. New deal starts'
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    print 'Player' + str(player)
    print 'Dealer' + str(dealer)
    outcome = 'Hit or stand?'
    in_play = True

def hit():
    global in_play, score, player, dealer, deck, outcome, last_outcome
    if not in_play:
        return
    
    if player.get_value() < 21:
        player.add_card(deck.deal_card())
        print 'Player ' + str(player)
    else:
        print 'You have busted. Dealer win.'
        last_outcome = 'Player has busted. Dealer win'
        outcome = 'New deal?'
        score -= 1
        in_play = False
       
def stand():
    global in_play, score, player, dealer, deck, outcome, last_outcome
    if not in_play:
        return
    
    if player.get_value() > 21:
        print 'You have busted'
        last_outcome = 'Player has busted. Dealer win.'
        outcome = 'New deal?'
        score -= 1
        in_play = False
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            score += 1
            print 'Dealer ' + str(dealer)
            print 'Dealer busted, player win.'
            last_outcome = 'Dealer busted. Player win.'
            outcome = 'New deal?'
        elif dealer.get_value() >= player.get_value():
            score -= 1
            print 'dealer is ' + str(dealer.get_value()) + 'player is ' + str(player.get_value()) + ' dealer win'
            last_outcome = 'dealer:' + str(dealer.get_value()) + ',player:' + str(player.get_value()) + ' ,dealer win'
            outcome = 'New deal?'
        else:
            score += 1
            last_outcome = 'dealer:' + str(dealer.get_value()) + ',player:' + str(player.get_value()) + ' ,player win'
            outcome = 'New deal?'
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        in_play = False
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):   
    player.draw(canvas, (10, 350))
    dealer.draw(canvas, (10, 150))
    if in_play:
        dealer.cards[0].draw_back(canvas, (10, 150))
    #draw title
    canvas.draw_text('Black', (200, 70), 40, 'Black', 'sans-serif')
    canvas.draw_text('Jack', (320, 70), 40, 'Red', 'sans-serif')
    #draw message
    canvas.draw_text(last_outcome, (10, 470), 20, 'Black', 'sans-serif')
    canvas.draw_text(outcome, (10, 500), 20, 'Black', 'sans-serif')
    #draw score
    canvas.draw_text('score:' + str(score), (430, 70), 40, 'Yellow', 'sans-serif')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

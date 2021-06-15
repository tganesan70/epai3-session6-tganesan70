#'''
#Python script for solving Part-I problems
#'''
import random
import itertools
import functools
import operator

## Globals
# Card values
vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'king', 'queen' , 'ace' ]
vals_dict = {'2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 , '10':10 , 'jack':11 , 'king': 12, 'queen':13 , 'ace':14}
# card suits
suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

#royal_flush_vals = ['ace','king','queen','jack','10']
royal_flush_vals = ['10', 'jack', 'king', 'queen', 'ace']
quad_vals = royal_flush_vals
flush_vals_set0 = ['2','3','4','5','6']
flush_vals_set1 = ['3','4','5','6','7']
flush_vals_set2 = ['4','5','6','7','8']
flush_vals_set3 = ['5','6','7','8','9']
flush_vals_set4 = ['6','7','8','9','10']
flush_vals_set5 = ['7','8','9','10','jack']
flush_vals_set6 = ['8','9','10','jack','king']
flush_vals_set7 = ['9','10','jack','king','queen']

def deal_cards_normal(numCards: 'No. of cards to be dealt')-> 'Tuple corresponding to the cards':
   '''
   Deal cards from the deck suits and values randomly
   :param numCards: No. of cards dealt per hand
   :return: List of tuples (suit, vals) for each of the cards
   '''
   card_vals = random.choices(vals, k=numCards)
   card_suits = random.choices(suits, k=numCards)
   return [card_vals, card_suits]

def deal_cards(deck: 'List of Tuples for card deck', numcards : 'No. of cards to be dealt')->'Tuples for the cards dealt':
    '''
    Deal cards from the deck randomly
    :param deck: Card deck with 52 card Tuples
    :param numcards: No. of cards per hand
    :return: Tuples for the dealt cards
    '''
    hand1 = random.choices(deck, k=numcards)
    return hand1

def get_vals(x: 'list of tuples with suits and values on the cards')->'list of values on the cards':
    '''
    Get the values from the Tuples with suits and values
    :param x: list of Tuples with suits and values
    :return: list of values
    '''
    val = [z[0:] for z in x]
    return val[1][:]

def get_suits(x):
   '''
   Get the suits from the Tuples with suits and values
   :param x: list of Tuples with suits and values
   :return: list of suits
   '''
   val = [z[0:] for z in x]
   return val[0][:]

def create_card_deck_normal()->'List of tuples representing  a card deck':
   '''
   Create a card deck without using the zip/map functions
   :return: A list of tuples with suits and values
   '''
   card_deck = list()
   for i in range(len(suits)):
      for j in range(len(vals)):
         card_deck.append((suits[i], vals[j]))
   return card_deck

def repeat_element(x: 'Element to be repeated', n=13)->'List of repeated elements':
   '''
   Repeats the given element n -times
   :param x: Element to repeated
   :param n: No. of times to be repeated (default=13)
   :return: Repeated elements list
   '''
   return [x for i in range(n)]

def create_card_deck()->'List of tuples representing a 52 card deck':
   '''
   Create a card deck using the zip/map functions
   :return: A list of tuples with suits and values
   '''
   repeat_vals = [*vals, *vals, *vals, *vals]
   repeat_suits = map(repeat_element, [x for x in suits])
   repeat_suits = list(itertools.chain(*repeat_suits))
   deck = list(zip(repeat_suits, repeat_vals))
   return deck

def majority_suit(x:'list of suits')->'count of each suit in the list':
   '''
   Returns the count of number of suits from each class in the given card list
   :param x: List of suit names in a card deck
   :return: Count of each suit in the given list
   '''
   i = 0
   temp = [i for i in range(len(suits))]
   for mysuit in suits:
      temp[i] = sum(map(lambda y: (y == mysuit), x))
      i += 1
   return temp

def majority_vals(x:'list of vals')->'count of each val in the list':
   '''
   Returns the count of number of suits from each class in the given card list
   :param x: List of val names in a card deck
   :return: Count of each vals in the given list
   '''
   i = 0
   temp = [i for i in range(len(vals))]
   for myvals in vals:
      temp[i] = sum(map(lambda y: (y == myvals), x))
      i += 1
   return temp

def max_vals(x:'list of values of a card deck')->'Returns the card with highest value':
    '''
    Returns the value with the highest value in the card deck
    :param x: list of card values
    :return: the card with highest value
    '''
    return functools.reduce(max, list([vals_dict[y] for y in x]))

def check_poker_straight(vals:'List of values')->'Returns true if it matches one of the sets':
    '''
    Check whether one of the straight conditions are met in the values of the poker cards
    :param vals: Values of cards as strings
    :return:  True if one of the straight conditions is met
    '''
    return (functools.reduce(operator.and_, map(lambda x: x in flush_vals_set0, vals)) or
            functools.reduce(operator.and_, map(lambda x: x in flush_vals_set1, vals)) or
            functools.reduce(operator.and_, map(lambda x: x in flush_vals_set2, vals)) or
            functools.reduce(operator.and_, map(lambda x: x in flush_vals_set3, vals)) or
            functools.reduce(operator.and_, map(lambda x: x in flush_vals_set4, vals)) or
            functools.reduce(operator.and_, map(lambda x: x in flush_vals_set5, vals)) or
            functools.reduce(operator.and_, map(lambda x: x in flush_vals_set6, vals)) or
            functools.reduce(operator.and_, map(lambda x: x in flush_vals_set7, vals)))

def check_poker_straight_value(val: 'List of values')->'Returns the set number which matches fpr straight':
    '''
    Check whether one of the straight conditions are met in the values of the poker cards
    :param vals: Values of cards as strings
    :return:  Compute which set has the matching
    '''
    set_value = [i+1 for i in range(8)]
    set0 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set0, val))
    set1 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set1, val))
    set2 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set2, val))
    set3 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set3, val))
    set4 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set4, val))
    set5 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set5, val))
    set6 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set6, val))
    set7 = functools.reduce(operator.and_, map(lambda x: x in flush_vals_set7, val))
    set = [set0, set1, set2, set3, set4, set5, set6, set7]
    value = 0
    for i in range(len(set)):
        value += set[i] * set_value[i]
    return value

def poker_winner(hand1:'List of tuples for the cards of hand1',hand2:'List of tuples for the cards of hand2')->'Winning hand number 1 or 2':
   '''
   Function to decide on the winner in the game of Poker for the two hands given
   :param hand1: list of tuples for hand1
   :param hand2: list of tuples for hand2
   :return: Declares the winner as 1 or 2
   '''
   hand1_suits = list(map(get_suits, hand1))
   hand1_vals = list(map(get_vals, hand1))
   hand2_suits = list(map(get_suits, hand2))
   hand2_vals = list(map(get_vals, hand2))
   hand1_suit_counts = majority_suit(hand1_suits)  # Find the majority number for the suits
   hand2_suit_counts = majority_suit(hand2_suits)  # Find the majority number for the suits
   hand1_vals_counts = majority_vals(hand1_vals)  # Find the majority number for the vals
   hand2_vals_counts = majority_vals(hand2_vals)  # Find the majority number for the vals

   # For debug only
   #print(hand1_suit_counts, hand1_vals_counts)
   #print(hand2_suit_counts, hand2_vals_counts)

   # Check for all winning conditions
   if max(hand1_suit_counts) == 5 and max(hand2_suit_counts) < 5:
       #test1 = ('ace' in hand1_vals) and ('king' in hand1_vals) and ('queen' in hand1_vals) and ('jack' in hand1_vals) and ('10' in hand1_vals)
       if functools.reduce(operator.and_, map(lambda x: x in royal_flush_vals, hand1_vals)):
           print("Royal Flush for Hand 1")
           return 1 # "Royal Flush"
           #elif ('3' in hand1_vals) and ('4' in hand1_vals) and ('5' in hand1_vals) and ('6' in hand1_vals) and ('7' in hand1_vals):
       elif check_poker_straight(hand1_vals):
           set1_value = check_poker_straight_value(hand1_vals)
           set2_value = check_poker_straight_value(hand2_vals)
           print(set1_value, set2_value)
           if set1_value > set2_value:
               print("Straight Flush in Hand1")
               return 1    # same suit cards in sequence - "straight flush"
           else:
               print("Straight Flush in Hand2")
               return 2    # same suit cards in sequence - "straight flush"
       else:
           print("Flush in Hand1")
           return 1
   elif max(hand2_suit_counts) == 5 and max(hand1_suit_counts) < 5:  # Second hand also have Flush
       if functools.reduce(operator.and_, map(lambda x: x in royal_flush_vals, hand2_vals)):
           print("Royal flush for Hand 2")
           return 2   # One of them got to be a winner - ideally None in this case
       elif check_poker_straight(hand2_vals):
           set1_value = check_poker_straight_value(hand1_vals)
           set2_value = check_poker_straight_value(hand2_vals)
           if set1_value > set2_value:
               print("Straight Flush in Hand1")
               return 1  # same suit cards in sequence - "straight flush"
           else:
               print("Straight Flush in Hand2")
               return 2  # same suit cards in sequence - "straight flush"
       else:
           print("Flush in Hand1")
           return 1
   elif max(hand2_suit_counts) == 5 and max(hand1_suit_counts) == 5:  # Second hand also have Flush
       print("Got lucky with Royal flush for Hand 1")
       return 1  # One of them got to be a winner - ideally None in this case
   elif max(hand1_vals_counts) == 4 and max(hand2_vals_counts) < 4:
       print("The Quad for hand 1")
       return 1
   elif  max(hand1_vals_counts) == 4 and max(hand2_vals_counts) == 4:  # Tie on Quads
       if max_vals(hand1_vals) > max_vals(hand2_vals):
            print("The Quad for hand 1- upper hand")
            return 1   # Quad for hand 1 - wins with higher value
       else:
            print("The Quad for hand 2- upper hand")
            return 2   # Quad for hand 2 = wins with higher value
   elif max(hand1_vals_counts) < 4 and max(hand2_vals_counts) == 4:
        print("The Quad for hand 2")
        return 2  # The quad for hand2
   elif max(hand1_vals_counts) == 3 and (2 in hand1_vals_counts):  # the other cards are also same
      print("Full house for hand 1")
      return 1
   elif max(hand2_vals_counts) == 3 and (2 in hand2_vals_counts):  # the other cards are also same
      print("Full house for hand 2")
      return 2
   elif check_poker_straight_value(hand1_vals) > check_poker_straight_value(hand2_vals):
      print("Straight for hand1")
      return 1
   elif check_poker_straight_value(hand1_vals) < check_poker_straight_value(hand2_vals):
      print("Straight for hand2")
      return 2
   elif max(hand1_vals_counts) == 3 and max(hand2_vals_counts) < 3:
       print("Three of a kind for hand1")
       return 1
   elif max(hand2_vals_counts) == 3 and max(hand1_vals_counts) < 3:
       print("Three of a kind for hand2")
       return 2
   elif (max(hand1_vals_counts) == 2) and (sum(map(lambda x: x == 2, hand1_vals_counts)) == 2):
       print("Two pairs for hand1")
       return 1
   elif (max(hand2_vals_counts) == 2) and (sum(map(lambda x: x == 2, hand2_vals_counts)) == 2):
       print("Two pairs for hand2")
       return 2
   elif max(hand1_vals_counts) == 2 and max(hand2_vals_counts) < 2:
       print("One pair for Hand 1")
       return 1
   elif max(hand2_vals_counts) == 2 and max(hand1_vals_counts) < 2:
       print("One pair for Hand 2")
       return 2
   elif max_vals(hand1_vals) > max_vals(hand2_vals):
       print("High Value in Hand 1")
       return 1
   elif max_vals(hand2_vals) > max_vals(hand1_vals):
       print("High Value in Hand 2")
       return 2
   else:
       return 0  # Some thing broken in the code - No winner

## Main test code for python notebook starts here
# Question 1: Create the complete deck of 52 cards using map, filter and/or zip
#deck_new= create_card_deck()
#print("Deck created by using map, filter, zip: \n ",deck_new)  #--> it is working correctly

# Question 2: Create the complete deck of 52 cards without using map, filter or zip
#deck_normal = create_card_deck_normal()
#print("Deck created by wo using map, filter, zip: \n ",deck_normal)  #--> it is working correctly

# Question 3: From the complete deck of 52 cards, create two hands with 5 cards each
#hand1 = deal_cards(deck_normal, 5)
#hand2 = deal_cards(deck_normal, 5)

####  Tests for the Poker Game
# Test 1: Royal Flush for hand1
#print("############# test 1 ############")
#hand1 = [('hearts', 'ace'), ('hearts', 'king'), ('hearts', 'queen'), ('hearts', 'jack'), ('hearts', '10')]
#hand2 = [('spades', 'ace'), ('hearts', '10'), ('diamonds', 'queen'), ('hearts', '3'), ('diamonds', '2')]
#winner = poker_winner(hand1, hand2)
#print('The winning hand is : ',winner)

#print("############# test 2 ############")
# Test 2: Royal Flush for hand2
#hand2 = [('spades', 'ace'), ('spades', 'king'), ('spades', 'queen'), ('spades', 'jack'), ('spades', '10')]
#hand1 = [('spades', 'ace'), ('hearts', '10'), ('diamonds', 'queen'), ('hearts', '3'), ('diamonds', '2')]
#winner = poker_winner(hand1, hand2)
#print('The winning hand is : ',winner)

#print("############# test 3 ############")
## Test 3: Straight Flush for hand2
#hand1 = [('clubs', '9'), ('spades', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
#hand2 = [('hearts', '9'), ('hearts', 'king'), ('hearts', '8'), ('hearts', 'jack'), ('hearts', '10')]
#winner = poker_winner(hand1, hand2)
#print('The winning hand is : ',winner)


#print("############# test 4 ############")
## Test 4: Straight Flush for hand1
#hand1 = [('diamonds', '9'), ('diamonds', 'king'), ('diamonds', 'queen'), ('diamonds', 'jack'), ('diamonds', '10')]
#hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
#winner = poker_winner(hand1, hand2)
#print('The winning hand is : ',winner)


#print("############# test 5 ############")
## Test 5: The Quad hand1
#hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
#hand1 = [('clubs', 'king'), ('diamonds', 'king'), ('spades', 'king'), ('hearts', 'king'), ('diamonds', '10')]
#winner = poker_winner(hand1, hand2)
#print('The winning hand is : ',winner)

#print("############# test 6 ############")
## Test 6: The Quad hand2
#hand1 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
#hand2 = [('clubs', 'queen'), ('diamonds', 'queen'), ('spades', 'queen'), ('hearts', 'queen'), ('spades', '10')]
#winner = poker_winner(hand1, hand2)
#print('The winning hand is : ',winner)


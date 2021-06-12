#'''
#Python script for solving Part-I problems
#'''
import random
import itertools

## Globals
# Card values
vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
# card suits
suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

'''
Create an entry of dictionary elements from inputs
:param x: Key
:param y: Entry
:return: (Key, Entry) pair
'''
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

'''
Deal cards from the deck randomly using map, filter, and zip
'''
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

def poker_winner(hand1:'List of tuples for the cards of hand1',hand2:'List of tuples for the cards of hand2')->'Winning hand number 1 or 2':
   '''
   Finction to decide on the winner in the game of Poker for the two hands given
   :param hand1: list of tuples for hand1
   :param hand2: list of tuples for hand2
   :return: Declares the winner as 1 or 2
   '''
   hand1_suits = list(map(get_suits, hand1))
   hand1_vals = list(map(get_vals, hand1))
   hand2_suits = list(map(get_suits, hand2))
   hand2_vals = list(map(get_vals, hand2))
   #print(hand1_suits, hand1_vals)
   #print(hand2_suits, hand2_vals)
   hand1_suit_counts = majority_suit(hand1_suits)  # Find the majority number for the suits
   hand2_suit_counts = majority_suit(hand2_suits)  # Find the majority number for the suits
   hand1_vals_count = majority_suit(hand1_vals)  # Find the majority number for the vals
   hand2_vals_count = majority_suit(hand2_vals)  # Find the majority number for the vals

   # Check for all winning conditions
   if max(hand1_suit_counts) == 5:
       if ('ace' in hand1_vals) and ('king' in hand1_vals) and ('queen' in hand1_vals) and ('jack' in hand1_vals) and ('10' in hand1_vals):
          return 1     # Royal flush
       elif ('3' in hand1_vals) and ('4' in hand1_vals) and ('5' in hand1_vals) and ('6' in hand1_vals) and ('7' in hand1_vals):
          return 1    # same suit cards in sequence
       elif max(hand2_suit_counts) < 5:   # all cards in same suit, but not in order
          return 1   # flush
   elif max(hand2_suit_counts) == 5:
       if ('ace' in hand2_vals) and ('king' in hand2_vals) and ('queen' in hand2_vals) and ('jack' in hand2_vals) and ('10' in hand2_vals):
             return 2  # Royal flush
       elif ('3' in hand2_vals) and ('4' in hand2_vals) and ('5' in hand2_vals) and ('6' in hand2_vals) and ('7' in hand2_vals):
             return 2  # same suit cards in sequence
       elif max(hand2_suit_counts) < 5:  # all cards in same suit, but not in order
             return 1   # flush
   elif max(hand1_suit_counts) == 4:
       if ('ace' in hand1_vals) and ('king' in hand1_vals) and ('queen' in hand1_vals) and ('jack' in hand1_vals) and ('10' in hand1_vals):
           return 1     # full house
   elif max(hand2_suit_counts) == 4:
       if ('ace' in hand2_vals) and ('king' in hand2_vals) and ('queen' in hand2_vals) and ('jack' in hand2_vals) and ('10' in hand2_vals):
           return 2     # full house
   elif (max(hand1_vals_count) > max(hand2_vals_count)) and max(hand1_vals_count) == 4:
       if ('king' in hand1_vals) or ('queen' in hand1_vals) or ('jack' in hand1_vals) or ('ace' in hand1_vals) or ('9' in hand1_vals) or ('8' in hand1_vals) or ('7' in hand1_vals) or ('6' in hand1_vals) or ('5' in hand1_vals) or ('4' in hand1_vals) or ('3' in hand1_vals) or ('1' in hand1_vals) or ('10' in hand1_vals):
            return 1    # The Quads
   elif (max(hand1_vals_count) < max(hand2_vals_count)) and max(hand2_vals_count) == 4:
        if ('king' in hand2_vals) or ('queen' in hand2_vals) or ('jack' in hand2_vals) or ('ace' in hand2_vals) or ('9' in hand2_vals) or ('8' in hand2_vals) or ('7' in hand2_vals) or ('6' in hand2_vals) or ('5' in hand2_vals) or ('4' in hand2_vals) or ('3' in hand2_vals) or ('1' in hand2_vals) or ('10' in hand2_vals):
            return 2    # The Quads
   elif (max(hand1_vals_count) > max(hand2_vals_count)) and max(hand1_vals_count) == 3:
      if ('king' in hand1_vals) or ('queen' in hand1_vals) or ('jack' in hand1_vals) or ('ace' in hand1_vals) or ('9' in hand1_vals) or ('8' in hand1_vals) or ('7' in hand1_vals) or ('6' in hand1_vals) or ('5' in hand1_vals) or ('4' in hand1_vals) or ('3' in hand1_vals) or ('1' in hand1_vals) or ('10' in hand1_vals):
            return 1    # The full house
   elif (max(hand1_vals_count) < max(hand2_vals_count)) and max(hand2_vals_count) == 3:
        if ('king' in hand2_vals) or ('queen' in hand2_vals) or ('jack' in hand2_vals) or ('ace' in hand2_vals) or ('9' in hand2_vals) or ('8' in hand2_vals) or ('7' in hand2_vals) or ('6' in hand2_vals) or ('5' in hand2_vals) or ('4' in hand2_vals) or ('3' in hand2_vals) or ('1' in hand2_vals) or ('10' in hand2_vals):
            return 2    # The full house
        #add  other test conditions here before declaring hand1 as winner
   else:
      return None

#def poker_winner(hand1: 'List of tuples for the cards of hand1',
#                hand2: 'List of tuples for the cards of hand2') -> 'Winning hand number 1 or 2':
#      '''
#      Finction to decide on the winner in the game of Poker for the two hands given
#      :param hand1: list of tuples for hand1
#      :param hand2: list of tuples for hand2
#      :return: Declares the winner as 1 or 2
#      '''
#      hand1_suits = list(map(get_suits, hand1))
#      hand1_vals = list(map(get_vals, hand1))
#      hand2_suits = list(map(get_suits, hand2))
#      hand2_vals = list(map(get_vals, hand2))
#      # print(hand1_suits, hand1_vals)
#      # print(hand2_suits, hand2_vals)
#      hand1_suit_counts = majority_suit(hand1_suits)  # Find the majority number for the suits
#      hand2_suit_counts = majority_suit(hand2_suits)  # Find the majority number for the suits
#      # print(hand1_suit_counts, hand2_suit_counts)
#      # If 4 cards or more from the same suit
#      if (max(hand1_suit_counts) > max(hand2_suit_counts)) and (max(hand1_suit_counts) >= 4):
#         return 1
#         # add  other test conditions here before declaring hand1 as winner
#      elif (max(hand2_suit_counts) > max(hand1_suit_counts)) and (max(hand2_suit_counts) >= 4):
#         return 2
#      else:
#         return None

## Main test code for python notebook starts here
# Question 1: Create the complete deck of 52 cards using map, filter and/or zip
deck_new= create_card_deck()
#print("Deck created by using map, filter, zip: \n ",deck_new)  #--> it is working correctly

# Question 2: Create the complete deck of 52 cards without using map, filter or zip
deck_normal = create_card_deck_normal()
#print("Deck created by wo using map, filter, zip: \n ",deck_normal)  #--> it is working correctly

# Question 3: From the complete deck of 52 cards, create two hands with 5 cards each
hand1 = deal_cards(deck_normal, 5)
hand2 = deal_cards(deck_normal, 5)
winner = poker_winner(hand1, hand2)
print('Hand1 : ',hand1)
print('Hand2 : ',hand2)
print('The winning hand is : ',winner)

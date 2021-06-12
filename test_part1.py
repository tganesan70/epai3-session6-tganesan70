'''
Python code for poker game
'''
import random
import itertools
import part1



## Globals
# Card values
vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]
# card suits
suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

# Question 1: Create the complete deck of 52 cards using map, filter and/or zip
def test_session6_part1_create_card_deck():
    deck_new= part1.create_card_deck()
    deck_normal = part1.create_card_deck_normal()
    assert sorted(deck_new) == sorted(deck_normal), "Error card deck generation - Normal method and map method do not match"
    assert len(deck_new) == 52, "Error card deck generation - number of cards in new method is less than 52"
    assert len(deck_normal) == 52, "Error card deck generation - number of cards in normal method is less than 52"

# Question 2: Create the complete deck of 52 cards without using map, filter or zip
#print("Deck created by wo using map, filter, zip: \n ",deck_normal)  #--> it is working correctly

# Question 3: From the complete deck of 52 cards, create two hands with 5 cards each
def test_session6_part1_create_poker_hand():
    deck_normal = part1.create_card_deck_normal()
    hand1 = part1.deal_cards(deck_normal, 5)
    hand2 = part1.deal_cards(deck_normal, 3)
    assert len(hand1) == 5, "Error in poker hand generation - number of cards is incorrect"
    assert len(hand2) == 3, "Error in poker hand generation - number of cards is incorrect"

# Question 4: check for the winner of the game
def test_session6_part1_poker_game():
    deck_normal = part1.create_card_deck_normal()
    #hand1 = part1.deal_cards(deck_normal, 5)  # hard code the hand for selecting winner
    #hand2 = part1.deal_cards(deck_normal, 3)  # hard code the hand for selection winner
    hand1 = [('hearts','ace'),('hearts','king'),('hearts','queen'),('hearts','jack'),('hearts','2')]
    hand2 = [('spade','ace'),('hearts','10'),('diamond','queen'),('hearts','3'),('diamond','2')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "
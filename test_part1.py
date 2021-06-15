#'''
#Python code for poker game
#'''
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
def test_session6_part1_poker_game1():
    # Test 1: Flush for hand1
    hand1 = [('hearts','ace'),('hearts','king'),('hearts','queen'),('hearts','jack'),('hearts','2')]
    hand2 = [('spade','ace'),('hearts','10'),('diamond','queen'),('hearts','3'),('diamond','2')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "


def test_session6_part1_poker_game2():
    # Test 2: Royal Flush for hand1
    print("############# test 1 ############")
    hand1 = [('hearts', 'ace'), ('hearts', 'king'), ('hearts', 'queen'), ('hearts', 'jack'), ('hearts', '10')]
    hand2 = [('spades', 'ace'), ('hearts', '10'), ('diamonds', 'queen'), ('hearts', '3'), ('diamonds', '2')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game3():
    # Test 3: Royal Flush for hand2
    hand2 = [('spades', 'ace'), ('spades', 'king'), ('spades', 'queen'), ('spades', 'jack'), ('spades', '10')]
    hand1 = [('spades', 'ace'), ('hearts', '10'), ('diamonds', 'queen'), ('hearts', '3'), ('diamonds', '2')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game4():
    # Test 4: Straight Flush for hand2
    hand1 = [('clubs', '9'), ('spades', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand2 = [('hearts', '9'), ('hearts', 'king'), ('hearts', '8'), ('hearts', 'jack'), ('hearts', '10')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game5():
    # Test 5: Straight Flush for hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('diamonds', '9'), ('diamonds', 'king'), ('diamonds', 'queen'), ('diamonds', 'jack'), ('diamonds', '10')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game6():
    # Test 6: The Quad hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('clubs', 'king'), ('diamonds', 'king'), ('spades', 'king'), ('hearts', 'king'), ('diamonds', '10')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game7():
    # Test 7: The Quad hand2
    hand1 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand2 = [('clubs', 'queen'), ('diamonds', 'queen'), ('spades', 'queen'), ('hearts', 'queen'), ('spades', '10')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game8():
    # Test 8: The Quad hand2
    hand1 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand2 = [('clubs', 'queen'), ('diamonds', 'queen'), ('spades', 'queen'), ('hearts', 'queen'), ('spades', '10')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game9():
    # Test 9: The full house in hand2
    hand1 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand2 = [('clubs', 'queen'), ('diamonds', 'queen'), ('spades', 'queen'), ('hearts', 'ace'), ('spades', 'ace')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game10():
    # Test 10: The full house in hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('clubs', 'king'), ('diamonds', 'king'), ('spades', 'king'), ('hearts', 'jack'), ('spades', 'jack')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game11():
    # Test 11: The flush in hand1
    hand1 = [('hearts', '2'), ('clubs', '3'), ('diamonds', 'ace'), ('spades', '5'), ('spades', '8')]
    hand2 = [('diamonds', '3'), ('diamonds', '5'), ('diamonds', '7'), ('diamonds', '9'), ('diamonds', 'queen')]
    #hand2 = [('spades', '2'), ('spades', '4'), ('spades', '6'), ('spades', '8'), ('spades', 'king')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game12():
    # Test 12: The flush in hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('diamonds', '3'), ('diamonds', '5'), ('diamonds', '7'), ('diamonds', '9'), ('diamonds', 'queen')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game13():
    # Test 13: The straight in hand2
    hand1 = [('hearts', '2'), ('clubs', '3'), ('diamonds', 'ace'), ('spades', '5'), ('spades', '8')]
    hand2 = [('diamonds', '3'), ('clubs', '4'), ('spades', '5'), ('hearts', '6'), ('diamonds', '7')]
    #hand2 = [('spades', '2'), ('spades', '4'), ('spades', '6'), ('spades', '8'), ('spades', 'king')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game14():
    # Test 14: The straight in hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('diamonds', '6'), ('clubs', '7'), ('spades', '8'), ('hearts', '9'), ('diamonds', '10')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game15():
    # Test 15: The triplets in hand2
    hand1 = [('hearts', '2'), ('clubs', '3'), ('diamonds', 'ace'), ('spades', '5'), ('spades', '8')]
    hand2 = [('diamonds', 'queen'), ('clubs', 'queen'), ('spades', 'queen'), ('hearts', '6'), ('diamonds', '7')]
    #hand2 = [('spades', '2'), ('spades', '4'), ('spades', '6'), ('spades', '8'), ('spades', 'king')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game16():
    # Test 16: The triplets in hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('diamonds', 'king'), ('clubs', 'king'), ('spades', 'king'), ('hearts', 'ace'), ('diamonds', '9')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game17():
    # Test 15: The pairs in hand2
    hand1 = [('hearts', '2'), ('clubs', '3'), ('diamonds', 'ace'), ('spades', '5'), ('spades', '8')]
    hand2 = [('diamonds', 'queen'), ('clubs', 'queen'), ('spades', 'king'), ('hearts', '6'), ('diamonds', '7')]
    #hand2 = [('spades', '2'), ('spades', '4'), ('spades', '6'), ('spades', '8'), ('spades', 'king')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game18():
    # Test 16: The pairs in hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('diamonds', 'king'), ('clubs', 'king'), ('spades', '2'), ('hearts', 'ace'), ('diamonds', '9')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game19():
    # Test 17: One pairs in hand2
    hand1 = [('hearts', '2'), ('clubs', '3'), ('diamonds', 'ace'), ('spades', '5'), ('spades', '8')]
    hand2 = [('diamonds', 'queen'), ('clubs', 'queen'), ('spades', 'king'), ('hearts', '6'), ('diamonds', '7')]
    #hand2 = [('spades', '2'), ('spades', '4'), ('spades', '6'), ('spades', '8'), ('spades', 'king')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game20():
    # Test 18: One pairs in hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('diamonds', 'king'), ('clubs', 'king'), ('spades', '2'), ('hearts', 'ace'), ('diamonds', '9')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game21():
    # Test 17: two pairs in hand2
    hand1 = [('hearts', '2'), ('clubs', '3'), ('diamonds', 'ace'), ('spades', '5'), ('spades', '8')]
    hand2 = [('diamonds', 'queen'), ('clubs', 'queen'), ('spades', 'king'), ('hearts', 'king'), ('diamonds', '7')]
    #hand2 = [('spades', '2'), ('spades', '4'), ('spades', '6'), ('spades', '8'), ('spades', 'king')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 2, "Game is over!!! You lost "

def test_session6_part1_poker_game22():
    # Test 18: two pairs in hand1
    hand2 = [('spades', '9'), ('clubs', '10'), ('spades', 'queen'), ('spades', '3'), ('spades', '2')]
    hand1 = [('diamonds', 'king'), ('clubs', 'king'), ('spades', '2'), ('hearts', '2'), ('diamonds', '9')]
    winner = part1.poker_winner(hand1, hand2)
    assert winner == 1, "Game is over!!! You lost "

def test_session6_part1_poker_game23():
    # Test 17: Random hands - test 1
    deck_new = part1.create_card_deck()
    hand1 = part1.deal_cards(deck_new, 5)
    hand2 = part1.deal_cards(deck_new, 5)
    winner = part1.poker_winner(hand1, hand2)
    assert winner != 0, "Game is over!!! You lost "

def test_session6_part1_poker_game24():
    # Test 18: Random hands - test 2
    deck_new = part1.create_card_deck()
    hand2 = part1.deal_cards(deck_new, 5)
    hand1 = part1.deal_cards(deck_new, 5)
    winner = part1.poker_winner(hand1, hand2)
    assert winner != 0, "Game is over!!! You lost "


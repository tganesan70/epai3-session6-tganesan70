# session6-tganesan70
#
# This assignment describes solutions to the following problems
#
# 1. Poker Game:
#   * To generate a function to simulate a deck of playing cards and to draw i
#     2 sets of 5 cards randomly. The card set with the following combinations
#     is declared as winner when compared to the other set. 
#     
   *  Poker Gama Winning Rules:
     The winning set is one of the following (from lowest to highest options)
     
     (i) High card - This is where the player has not made any pair of his/her 
     cards with the cards on the board. Here, the person with the highest card wins.
     
     (ii) One pair - In this hand, either two cards on the board, or one card on the 
     board and one in the hole (player’s cards), or both hole cards make a pair.
     
     (iii) Two pair - Two different cards are paired in this hand. For example, 
     you have a 3 and 5, and the board also brings a 3 and 5.
     
     (iv) Three of a kind - Also known as ‘trips’, in this hand, the player 
     gets 3 cards of the same value. For example, you have a K and 9, and the 
     board brings 2 more 9’s.
     (v) Straight - In this hand, the player makes a sequence 5 of cards. 
     For example, 3,4,5,6,7 is a straight. A person with a higher straight always wins.
     
     (vi) Flush - Here, the player gets 5 cards of the same suit, but not in a 
     sequence. For example, you have 3 and 7 of Hearts, and the board 
     has 9,2, and Q of Hearts, then you have a flush. If all cards on the board 
     are of the same suit, the person with the highest card wins.
     
     (vii) Full house - In this hand, the player has a pair of one card and 
     trips of the other. For example, you have 8,K and the board is 4,8,K,9,K; 
     here, you have a full house of K,K,K,8,8.
     
     (viii) Four of a kind - This hand is also called ‘quads’. Here, you get 
     all 4 cards of the same value. For example, 4 Kings, 4 Queens, etc.
     
     (ix) Straight flush - This hand is a combination of the straight and flush. 
     For example, you have a straight flush if you get 3,4,5,6,7 ALL of the same suit.
     
     (x) Royal flush - This is the biggest, and rarest, hand in all of poker. i
     The royal flush is when you get 10, J, Q, K, Ace - ALL of the same suit
     
# Implementaion Details:
#     * The card suits are repeated 10 times using map function and the vals are repeated 4 times and 
#     they are paired using the zip function to create a deck.
     
     * From a deck, two hands are dealt by using random choice of the 52 tuples
     
     * The Winner is selected by checking for the above 10 rules of winning
     
     
# 2. Fibanocci number test 
#    A filter function which tells whether a number which is less than 10000, 
#    is a Fibanocci number or not
#    * For this the Fibanocci sequence is precomputed and stored and used
#      filter function to check whether the given number is in the sequence.
   
# 3 . List comprehension test
    (a) Add two iterable a and b such that a is even and b is odd
       - For this two lambda functions are added to check odd and even numbers 
         and filter is used to select the odd and even numbers. Thus filtered numbers 
         are added using a list comprehension and myadd lambda function
    (b) Strip all vowels from a supplier string
       - For this use the fitler to check whether the given letter in a string is a
         vowel or not.
    (c) Acts like a list comprehension for a sigmoid function
        - A list comprehension is added as a simple function implementing
          y(x) = 1/(1+exp(-x))
    (d) Shift the letters in a string by a number translation
        i.e., takes a small character string and shifts all characters by 5 
        (handle boundary conditions) tsai>>yxfn
         - For this a map is created using the alphabets array, and modulo 
         addition is performed in a list comprehension
    (e) Filter out swearing words from the available list
        - For that a shitty comment is added here to test on this very file.
          A list comprehension is added to do the same by matching the words

# 4. Reduce function tests
    (a) Add only even numbers in a list 
    - Used a combination of reduce function along with filter to check for even numbers
    (b) Find the biggest ASCII character in a string
    - Used a combination of reduce function along with filter to check for maximum of ord() values
    (c) Adds every 3rd number in a list
    - Used reduce() with add operator and filter() with modulo operator on the index of the data

# 5. List Comprehension - Random Car number plate generation 
     For this list of random number plates ware created using list comprehension and
     another partial function for the same
     
    
    
    
     
     
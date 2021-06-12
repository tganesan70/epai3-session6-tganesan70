'''
Python script for solving Part-II problems
'''
import random
import math
import itertools
#import matplotlib.pyplot as plt
import functools
import operator

# Define space for Fibanocci sequence
fib_seq = [0 for i in range(25)]  # allocate memory (list) for the global array

# Define the English alphabets and vowels separately
alphabets = [chr(i + 97) for i in range(25)]
alphabets.append(chr(32))  # add space also to create artificial words
cap_letters = [chr(i + 65) for i in range(25)] # add space also to create artificial words
alphabets.append(cap_letters)
alphabets = list(itertools.chain(*alphabets))
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def gen_fibanocci(n: 'Max. number in the Fibanocci seqquence ') -> 'Returns no. of generated sequence':
    '''
    Generate Fibanocci sequence upto given integer n and saves it in a global array fib_seq
    :param n: Integer - Maximum number upto which sequence will be generated
    :return: Number of Fibanocci sequence numbers generated
    '''
    if not 0 < n < 10001:
        raise ValueError('Input number must be between 1 and 10001')
    new = 1
    old = 0
    index = 0
    fib_seq[index] = old
    index += 1
    fib_seq[index] = new
    while (new + old <= n):
        index += 1
        if index > len(fib_seq):
            raise IndexError('Insufficient space to save fib_seq')
        fib_seq[index] = new + old
        old, new = new, fib_seq[index]
    return index


def test_fib_seq_num(n: 'Integer number') -> ' Returns True or False':
    '''
    Test whether the given number is a Fibanocci number
    :param n: Integer less than 10000
    :return: True if the number is a Fibanocci sequence else False
    '''
    temp = list(filter(lambda x: x == n, fib_seq))
    print(temp)
    if len(temp) > 0:
        return True
    else:
        return False


isvowel = lambda x: True if (x in vowels) else False
isnot_vowel = lambda x: False if (x in vowels) else True
iseven = lambda x: True if (x % 2 == 0) else False
isodd = lambda x: True if (x % 2 == 1) else False
myadd = lambda x, y: x + y

def add_2_iterables(x1: 'List of numbers', y1:'List of numbers')->'List of numbers':
    '''
    Add two iterables if first one is even and second one is odd
    :param x1: List of numbers from which even will be picked
    :param y1: List of numbers from which odd numbers will be picked
    :returns: List of sum of numbers if the above condition matches for the same index
    '''
    temp_y = list(filter(isodd, y1))
    temp_x = list(filter(iseven, x1))
    temp_z = [myadd(x, y) for (x, y) in zip(temp_x, temp_y)]
    return temp_z
    # return list(map x,y: x+y, for (x,y) in (tempx,temp_y))

def vowel_free_word(s: 'Input string') ->'Returns the string without vowels':
    '''
    Function to strip the vowels from the given string
    :param s:
    :return:
    '''
    letters = [c for c in s]
    new_word = "".join(list(filter(isnot_vowel, letters)))
    return new_word

def sigmoid_func(x: 'list of number ') -> 'Returns the sigmoid function of input' :
    '''
    Apply Sigmoid function of the input y(x) = 1/(1+exp(-x))
    :param x: list of numbers
    :return: Sigmoid(x) as list
    '''
    return [1/(1+math.exp(-z)) for z in x]

def mod(x,y):
    if x < 0:
        x = x + y
    return x if x < y else x-y

def shift_alphabets(word: 'Input string', n: 'No.of shifts', dir: 'direction of shift') -> 'returns the modified string':
    '''
    Shift the alphabets by a fixed number and wrap around for encryption and decryption
    :param word: Input string
    :param n:  No. of shifts
    :param dir: +/- 1 for forward and reverse direction
    :return: Direction of shift (1 for forward and -1 for backward)
    '''
    alphabets = [chr(i + 97) for i in range(26)]
    return "".join([alphabets[mod(ord(x) - 97 + dir * n, 26)] for x in word])

## Main code starts here to test without pytest -> This will be converted to pytest testcase
def filter_swearing_words(line: 'A text paragraph')->'Cleaned paragraph without swaering words':
    '''
    Remove the swearing words in the given file list.txt
    :param line: a set of words from a file
    :return: Words without swearing words are returned
    '''
    wrong_words_file = open("list.txt","r")
    wrong_words = wrong_words_file.read().split()
    return " ".join(list(filter(lambda x: True if x not in wrong_words else False,line)))

def multiply_all_even_numbers(x: 'list of numbers')->'product of all even numbers from the inout list':
    '''
    Reduce function to multiply only even numbers in a list
    :param x: list of numbers
    :return: product of all even numbers
    '''
    return functools.reduce(operator.mul, filter(iseven, x))

def find_max_char(line):
    '''
    Reduce function to pick the largest character in a line (as per the ASCII value)
    :param line: a string
    :return: the character with the maximum ASCII value
    '''
    return chr(functools.reduce(lambda x,y: x if x> y else y, [ord(x) for x in line]))

def add_every_3rd_number(data: 'List of numbers')->'Sum of data(1:3:end)':
    '''
    Reduce function to add every 3rd number in a list of numbers
    :param data: list of numbers
    :return: Sum of every 3rd number in the input list
    '''
    z = [i for i in range(len(data))]
    return functools.reduce(operator.add, filter(lambda x: data[x] if (x % 3 == 0) else False, z))

def random_number_plates(state: 'State string in 2 letters', number:'Number of plates needed')->'List of number plates':
    '''
    Generate a random set of number plates in the format SSRRAADDDD, where
    SS - State letters
    RR - Region numbers between 0 to 99
    AA - Series letters from AA to ZZ
    DDDD - Number from 0000 to 9999
    :param state: State 'SS' string
    :param number: No,. of random number plates to be generated
    :return: list of random number plates for the given state
    '''
    region_numbers = [i for i in range(10,100)]
    regist_numbers = [i for i in range(1000,10000)]
    alpha_numbers = [chr(i + 65) for i in range(26)]
    number_plates = [state +
                 str(random.choice(region_numbers))+
                 random.choice(alpha_numbers)+
                 random.choice(alpha_numbers)+
                 str(random.choice(regist_numbers)) for i in range(number)]
    return number_plates

def random_number_plates_new(state: 'State string in 2 letters', r1: 'start of DDDD', r2:'end of DDDD',number:'Number of plates needed')->'List of number plates':
    '''
    Generate a random set of number plates in the format SSRRAADDDD, where
    SS - State letters
    RR - Region numbers between 0 to 99
    AA - Series letters from AA to ZZ
    DDDD - Number from 0000 to 9999
    :param state: State 'SS' string
    :param number: No,. of random number plates to be generated
    :return: list of random number plates for the given state
    '''
    region_numbers = [i for i in range(10,100)]
    regist_numbers = [i for i in range(r1,r2)]
    alpha_numbers = [chr(i + 65) for i in range(26)]
    number_plates = [state +
                     str(random.choice(region_numbers))+
                     random.choice(alpha_numbers)+
                     random.choice(alpha_numbers)+
                     str(random.choice(regist_numbers)) for i in range(number)]
    return number_plates
## Main code starts here to test without pytest -> This will be converted to pytest testcase
## Test cases for the pynotebook
# numSeq = gen_fibanocci(-1)  # works
# numSeq = gen_fibanocci(0)   # works
# numSeq = gen_fibanocci(1)   # works
# numSeq = gen_fibanocci(2)   # works
# numSeq = gen_fibanocci(3)   # works
numSeq = gen_fibanocci(10000)  # works
# numSeq = gen_fibanocci(100001)   # works

## Validate a number of Fibanocci number or not
# test_num = int(random.random()*10000)   # works
# print(test_num)
# print(test_fib_seq_num(test_num))       #works
# print(test_fib_seq_num(-1))             #works
# print(test_fib_seq_num(2584))           #works for valid Fibanocci number

## Test for add two iterables
# x = [0 for i in range(10)]
# y = [0 for i in range(10)]
# for i in range(10):
#    x[i] = math.floor(random.random()*100)
#    y[i] = math.floor(random.random()*100)
# print(x,y,add_2_iterables(x,y))

## Test for vowel stripper in strings
#random_word = "".join(random.choices(alphabets, k=20))
#new_word = vowel_free_word(random_word)
#print(random_word, new_word)

#Test for a Sigmoid function application
#x = [0 for i in range(10)]
#for i in range(10):
#   x[i] = (random.random()-0.5)
#y = sigmoid_func(x)
#print(x)
#print(y)
#plt.bar(x,y)

#Test for checking profanity in text
#readme_file = open("README.md","r")
#readme_file_words = readme_file.read().split()
#y = filter_swearing_words(readme_file_words)
#print(y)

# Test for product of even numbers using reduce function
#x = [i for i in range(10)]
#for i in range(10):
#   x[i] = (random.random()-0.5)
#y = functools.reduce(lambda x,y: x*y, filter(iseven, x[2:]))
#y = functools.reduce(operator.mul, filter(iseven, x[2:]))
#y = multiply_all_even_numbers(x[2:])
#print(y)

# Test for picking the maximum ASCII value character in a string
#alphanums = alphabets
#numerals = [str(i) for i in range(10)]
#alphanums.append(numerals)
#alphanums = list(itertools.chain(*alphanums))
##print(alphanums)
#random_line = "".join(random.choices(alphanums,k=20))
##print(random_line)
#y = find_max_char(random_line)
#print(chr(y))

# Test for adding every 3rd number is a list
#data = [i for i in range(20)]
#z = [i for i in range(len(data))]
#print(list(filter(lambda x: data[x] if (x % 3 == 0) else False, z)))
#y = functools.reduce(operator.add, filter(lambda x: data[x] if (x % 3 == 0) else False, z))
#y = add_every_3rd_number(data)
#print(y)

#Test for number plate generation
#region_numbers = [i for i in range(100)]
#regist_numbers = [i for i in range(10000)]
#alpha_numbers = [chr(i+65) for i in range(26)]
#state = "KA"
#num_plates = random_number_plates(state,15)
#print(num_plates)
#state = "DL"
#num_plates = random_number_plates(state,15)
#print(num_plates)

# Generate using partial function
#f = functools.partial(random_number_plates_new,'DL',1000,10000)
#num_plates = f(10)
#print(num_plates)

#
# Python script for solving problem 2
#

import random
import part2
import pytest
import os
import inspect
import re
import math
import functools

## Main code starts here to test with pytest -> This will be converted to pytest testcase
def test_session6_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session6_readme_500_words():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session6_readme_file_for_more_than_10_hashes():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10 , "More detailed \# comments needed"

def test_session6_function_name_had_cap_letter():
    functions = inspect.getmembers(part2, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

## Test cases for the pynotebook
def test_session6_part2_fibanocci1():
    with pytest.raises(ValueError, match=r".*Input number must be between 1 and 10001*"):
        part2.gen_fibanocci(-1)

def test_session6_part2_fibanocci2():
    with pytest.raises(ValueError, match=r".*Input number must be between 1 and 10001*"):
        part2.gen_fibanocci(0)

def test_session6_part2_fibanocci3():
    assert part2.gen_fibanocci(1) == 2, "Fibanocci output not correct"
    assert part2.gen_fibanocci(2) == 3, "Fibanocci output not correct"
    assert part2.gen_fibanocci(3) == 4, "Fibanocci output not correct"
    assert part2.gen_fibanocci(10000) == 20, "Fibanocci output not correct"

def test_session6_part2_fibanocci4():
    assert part2.test_fib_seq_num(1234) == False, "Fibanocci test is not correct"
    assert part2.test_fib_seq_num(-1) == False, "Fibanocci test is not correct"
    assert part2.test_fib_seq_num(2584) == True, "Fibanocci test is not correct"

# Test for adding two iterables
def test_session6_part2_add_iterables():
    ## Test for add two iterables
    x = [i for i in range(1,10)]
    y = [i for i in range(2,11)]
    assert part2.add_2_iterables(x,y) == [5,9,13,17], "add two iterables output not matching"

## Test for vowel stripper in strings
def test_session6_part2_vowel_free_word():
    random_word = "The quick brown fox jumps over the lazy dog"
    assert part2.vowel_free_word(random_word) == "Th qck brwn fx jmps vr th lzy dg", "Still vowels are out there..."

#Test for a Sigmoid function application
def test_session6_part2_sigmoid_func():
    assert part2.sigmoid_func([0]) == [0.5], "Error in Sigmoid function computation"
    assert part2.sigmoid_func([1]) == [0.7310585786300049], "Error in Sigmoid function computation"
    assert part2.sigmoid_func([-1]) == [0.2689414213699951], "Error in Sigmoid function computation"
    assert part2.sigmoid_func([1,0,-1]) == [0.7310585786300049,0.5,0.2689414213699951], "Error in Sigmoid function computation"

#Test for shifting the letters in a string
def test_session6_part2_letter_shift():
    random_word = "thequickbrownfoxjumpsoverthelazydog"
    shift_text = part2.shift_alphabets(random_word,5,1)
    assert shift_text == "ymjvznhpgwtbsktcozruxtajwymjqfeditl", "encoding not correct"
    assert part2.shift_alphabets(shift_text,5,-1)==random_word, "decoding not correct"

#Test for checking profanity in text
def test_session6_part2_profanity_check():
    readme_file = open("README.md","r")
    readme_file_words = readme_file.read().split()
    output_words = part2.filter_swearing_words(readme_file_words)
    flag = 0
    for word in output_words:
        if word == "shitty":
            flag = 1
    assert flag == 0, "Profanity check failed"

# Test for product of even numbers using reduce function
def test_session6_part2_even_number_reduce():
    x = [i for i in range(10)]
    assert part2.multiply_all_even_numbers(x[2:]) == 384, "Error in even number product output"

# Test for picking the maximum ASCII value character in a string
def test_session6_part2_max_aascii_reduce():
    random_word = "thequickbrownfoxjumpsoverthelazydog"
    assert part2.find_max_char(random_word) == 'z', "Error in the max ASCII value"

# Test for adding every 3rd number is a list
def test_session6_part2_add_every_3rd_reduce():
    data = [i for i in range(20)]
    assert part2.add_every_3rd_number(data) == 63, "Error in adding every 3rd number"

#Test for number plate generation
def test_session6_part2_number_plate_gen():
    state = "KA"
    num_plates = part2.random_number_plates(state,15)
    assert len(num_plates) == 15, "No. of generated number plates is wrong"

# Generate using partial function
def test_session6_part2_number_plate_partial_func():
    state = "KA"
    f = functools.partial(part2.random_number_plates_new,'DL',1000,10000)
    num_plates = f(10)
    assert len(num_plates) == 10, "No. of generated number plates is wrong"
    for x in num_plates:
        if x == state:
            assert False, "State is not correct"

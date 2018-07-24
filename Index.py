#!usr/bin/env  python3
"""
Index.py

Problem Statement
--------------------------------------------------------
1. Write logic that takes a blob of text as a parameter and tokenizes this blob into words.
   Words are delimited by any character other than a-z, A-Z, or 0-9.
2. Write logic to track all unique words encountered and the number of times each was encountered.
   Words should be matched in a case-insensitive manner. This should return the top 10 words (and their counts).
3. Provide some documentation for the code you wrote in each of the previous steps.
4. You must test your code. Make sure you include some brief documentation on how to run the tests.
   Any collection of plain text files can be used as input, and we suggest you try out some free plain text books
   from http://www.gutenberg.org/

Functions
--------------------------------------------------------
tokenize_into_words
    Tokenizes a blob of text into words.
count_unique_words
    this counts the total number of words in a list.
display_top_n_words
    this returns the most used words and with their counts.
"""

from textblob import TextBlob
import re  # Importing  package for Regular Expression


def tokenize_into_words(myblob):
    """ This function tokenizes the input string into words.
        Words are delimited by any character other than a-z, A-Z, or 0-9.
        Input parameter is a string value named myBlob
        Return value for the function is a list named words having various individual words
    """
    set_constraint = re.compile(r'[^a-zA-Z0-9]')
    tokenize_to_text = set_constraint.split(myblob) # The blob is spilt into words and the given constraints are applied
    words = [word for word in tokenize_to_text if word]
    return words


def count_unique_words(words):
    """ This function counts the total number of unique words in a list of words.
        Input parameter is  a list of strings named words.
        Return value for the function is a dictionary named total_count__of_words
    """
    total_count__of_words = {}    # Defining a Dictionary
    for word in words:
        if word.lower() in total_count__of_words:  # As mentioned in the requirements checking for case insensitive matching
            total_count__of_words[word.lower()] += 1
        else:
            total_count__of_words[word.lower()] = 1
    return total_count__of_words


def display_top_n_words(total_count__of_words, n):   # Considering n=10 here as specified in the requirements
    """This function returns  the most frequent words from the dictionary and sorts them by decreasing value of their counts
       Input parameters are a dictionary named total_count__of_words and n (Integer value)
       Return value is a list comprising of (word of string type, total count of integer type)
    """
    return sorted(total_count__of_words.items(), key=lambda i: i[1], reverse=True)[:n]


if __name__ == '__main__':    # Starting point of the program
     n = 10  # As specified in the requirement that top 10 words are required
     with open('the_camp_fire_girls_at_half_moon_lake.txt', encoding='utf8') as text_file:
        myBlob = text_file.read()
     words = tokenize_into_words(str(myBlob))    # Function called to tokenize into words
     total_count__of_words = count_unique_words(words)
     print(display_top_n_words(total_count__of_words, n))

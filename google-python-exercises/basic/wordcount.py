#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
from collections import Counter


# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

# Define a helper function to read the file and build a word/count dictionary.
def build_word_count_dict(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = text.split()
        word_count = Counter(words)
    return word_count



# Define print_words(filename) to print word counts sorted by word.
def print_words(filename):
    word_count = build_word_count_dict(filename)
    for word in sorted(word_count.keys()):
        print(f'{word} {word_count[word]}')

# Define print_top(filename) to print the top 20 most common words.
def print_top(filename):
    word_count = build_word_count_dict(filename)
    top_words = word_count.most_common(20)
    for word, count in top_words:
        print(f'{word} {count}')

# Function to be called within the notebook
def wordcount(option, filename):
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


def main():
    option = '--count'  #or '--topcount'
    filename = r'D:\Isha\ME\studies\assignments\advanced programming\google-python-exercises\basic\story.txt'
    wordcount(option, file_path)

if __name__ == '__main__':
    main()
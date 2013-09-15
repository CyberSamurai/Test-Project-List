"""
-=Mega Project List=-
5. Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a
summary.
"""

import os.path

def count_words(string):
    words = string.split()
    return len(words)


def main(file):
    filename = os.path.abspath(file)
    with open(filename, 'r') as f:
        count = [count_words(line) for line in f]
        for i, v in enumerate(count):
            print "Line %d has %d words in it." % (i+1, v)

if __name__ == '__main__':
    main('footext.txt')

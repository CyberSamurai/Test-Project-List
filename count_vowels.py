"""
-=Mega Project List=-
3. Count Vowels - Enter a string and the program counts the number of vowels in
the text.  For added complexity have it report a sum of each vowel found.
"""


def count_vowels(string):
    # Need to break the string into a list and count all the vowels
    letters = list(string.lower())
    vowels = "aeiou"
    vcount = 0
    for letter in string:
        if letter in vowels:
           vcount += 1

    # Need a list of all the vowels in the string to count them individually
    summary  = [i for i in letters if i in vowels]

    # Report our vowel count and details of the count
    print "There are %s vowels in your string." % vcount
    print "A's:", summary.count('a')
    print "E's:", summary.count('e')
    print "I's:", summary.count('i')
    print "O's:", summary.count('o')
    print "U's:", summary.count('u')
        

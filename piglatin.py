"""
-=Mega Project List=-
2. Pig Latin
"""

def translator(string):
    word = string.lower()
    if word[0] in ('a', 'e', 'i', 'o', 'u'):
         print string + "-ay"
    else:
        first_letter = word[0]
        rest = word[1:]
        print "%s-%say" % (rest, first_letter)

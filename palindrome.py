"""
-=Mega Project List=-
4. Check if Palindrome - Checks if the string entered by the user is a
palindrome. That is that it reads the same forwards as backwards like "racecar"
"""

def palindrome(string):
    #compare the first and last letters for equality then check the middle
    if string[0] == string[-1]:
        middle = string[1:-1]
        if middle == middle[::-1]:
            return True
    return False

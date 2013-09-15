"""
-=Mega Project List=-
1. Reverse a string:
    Enter a string and the program will reverse it and print it out.
"""

def reverse_string(string):
    first = string[0]
    mid = string[1:-1]
    last = string[-1]
    print last + mid + first

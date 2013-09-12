"""
Mega Projects List

99 Bottles of Beer - Display lyrics of 99 bottles without typing numbers in
the lyric lines.
"""

bottles = 99

while bottles > 0:
    chorus = """%d bottles of beer on the wall, %d bottles of beer! 
    Take one down, pass it around...""" % (bottles, bottles)
    if bottles == 1:
        chorus = """%d bottle of beer on the wall, %d bottle of beer!
        Take one down, pass it around...
        No more bottles of beer on the wall!!""" % (bottles, bottles)
    print chorus
    print
    bottles -= 1

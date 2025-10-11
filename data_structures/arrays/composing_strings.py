"""
Assume that we have a large string named document, and our goal
is to produce a new string, letters, that contains only the
alphabetic characters of the original string. 
"""

# WARNING: do not do this
# Strings are immutable and so this would create a new instance
# and reassign identifer, letters, to the result.
# runs in O(n^2) !!!
letters = '' # start with empty string
for c in document:
    if c.isalpha():
        letters += c # concatenate alphabetic characters

# O(n) approach
# use a temporary list to store individual pieces
# rely on the join method to compose the final result
temp = []   # start with empty list
for c in document:
    if c.isalpha():
        temp.append(c)  # append alphabetic character
    letters = ' '.join(temp) # compose overall result

# Further improve by using LIST COMPREHENSION! 
# build up the temp list, rather than by repeated calls to append
letters = ' '.join([c for c in document if c.isalpha()])

# Even better, can entirely avoid the temp list w/ a GENERATOR COMPREHENSION!
letters = ' '.join(c for c in document if c.isalpha())
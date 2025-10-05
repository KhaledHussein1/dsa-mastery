# O(n)
def reverse(S, start, stop):
    """Reverse elements in implicit since S[start:stop]"""
    if start < stop -1: # if at least 2 elements:
        S[start], S[stop-1] = S[stop-1],S[start] # swap first and last
        reverse(S, start+1, stop-1) # recur on rest

if __name__ == "__main__":
    S = [1,2,3,4,5,6,7,8,9]
    print(S)
    reverse(S, 0, 9)
    print(S)
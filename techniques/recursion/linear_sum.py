# O(n)
def linear_sum(S,n):
    """Return the sum of the first n numbers of a sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(S)
    print(linear_sum(S, 4))
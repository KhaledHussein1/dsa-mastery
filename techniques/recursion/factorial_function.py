import time
#import sys

#sys.setrecursionlimit(2000)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    start = time.perf_counter()
    result = factorial(20)
    end = time.perf_counter()

    print(f"Result: {result}")
    print(f"Execution time: {end - start:.6f} seconds")
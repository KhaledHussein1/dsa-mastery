def binary_search_recursive(data, target, low, high):
    """ Return True if target is found in indicated portion of Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high: 
        return False    #interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True #found match
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search_recursive(data, target, low, mid -1)
        else:
            # recur on the portion right of the middle
            return binary_search_recursive(data, target, mid + 1, high)

if __name__ == "__main__":
    data = [1, 4, 7, 9, 45, 55, 878, 7765]

    result = binary_search_recursive(data, 7765, 0, 8)

    print(result)
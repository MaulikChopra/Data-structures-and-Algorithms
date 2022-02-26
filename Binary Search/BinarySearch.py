# Binary Search recursive.
# O(log(n)) - time complexity.

def recursive(array, value):
    return bs(array, value, 0, len(array))


def bs(array, value, left_iterator, right_iterator):
    start = left_iterator
    end = right_iterator
    middle = (start + end) // 2
    if start == end:
        return False
    elif value > array[middle]:  # right
        print(start, middle, end)
        return bs(array, value, middle + 1, end)
    elif value < array[middle]:  # left
        print(start, middle, end)
        return bs(array, value, start, middle)
    return True, middle


def iterative():
    pass


# DRIVER CODE
if __name__ == "__main__":
    arr = [i for i in range(1, 51)]
    find = 8
    print("(bool, index)")
    print(recursive(arr, find))

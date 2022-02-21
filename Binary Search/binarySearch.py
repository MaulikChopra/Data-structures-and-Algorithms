# Binary Search recursive.
# O(log(n)) - time complexity.

def recursive(array, value):
    return bs(array, value, 0, len(array))


def bs(array, value, start, end):
    middle = (start + end) // 2
    if start == end:
        return False
    elif value > array[middle]:  # right
        return bs(array, value, middle + 1, len(array))
    elif value < array[middle]:  # left
        return bs(array, value, start, middle)
    return True, middle


def iterative():
    pass


# DRIVER CODE
if __name__ == "__main__":
    arr = [i for i in range(0, 10)]
    find = 8
    print(recursive(arr, find))

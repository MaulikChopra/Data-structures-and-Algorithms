# Binary Search recursive.
# O(log(n)) - time complexity.
# Do not manipluate the array as it causes more space complexity.
# Use iterators to easily divide the array and update them at each step.
# For me iterative was much easier to remember/ implement than recursive search.

"""
PseudoCode:
function():
    assign value of left iterator as start
    assign value of right iterator as end
    run until the list ends:
        calculate middle index [formula: (start + end) //2]
        check if value not find: 
            return False
        check if value greater than middle index: ie right
            update start to middle +1
            update end value to new end
        check if value smaller than middle indes: ie left
            update end value to middle
            update start value to new start
        check else:
            return True, middle (middle is the index of value)
"""


def recursive(array, value):
    return bs(array, value, 0, len(array))


def bs(array, value, left_iterator, right_iterator):
    start = left_iterator
    end = right_iterator
    middle = (start + end) // 2
    if start == end:
        return False
    elif value > array[middle]:  # right
        # print(start, middle, end)
        return bs(array, value, middle + 1, end)
    elif value < array[middle]:  # left
        # print(start, middle, end)
        return bs(array, value, start, middle)
    return True, middle


def iterative(array, value):
    start = 0
    end = len(array)
    while True:
        middle = (start + end)//2
        if start == end:
            return False
        elif value > array[middle]:  # Right side
            # print(start, middle, end)
            # update the new values like in the recurssion
            start = middle + 1
            end = end
        elif value < array[middle]:  # Left side
            # print(start, middle, end)
            start = start
            end = middle
        else:
            return True, middle


# DRIVER CODE
if __name__ == "__main__":
    arr = [i for i in range(1, 51)]
    # arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    find = 6
    print("(bool, index)")
    print(recursive(arr, find))
    print("-------------------")
    print(iterative(arr, find))

import time


def binary_search(array, value):
    length = len(array)

    def bs(array, length, value):
        if length != 0 and value <= array[length-1] and value >= array[0]:
            if value == array[length//2]:
                return True
            elif value > array[length//2]:
                # print(array[length//2:])
                return binary_search(array[length//2:], value)
            elif value < array[length//2]:
                # print(array[:length//2])
                return binary_search(array[:length//2], value)
        else:
            return False
    return bs(array, length, value)


def binary_search_length(array, length, value):
    if length != 0 and value <= array[length-1] and value >= array[0]:
        if value == array[length//2]:
            return True
        elif value > array[length//2]:
            print(array[length//2:])
            return binary_search_length(array[length//2:], length//2, value)
        elif value < array[length//2]:
            print(array[:length//2])
            return binary_search_length(array[:length//2], length//2, value)
    else:
        return False


def linear_search(array, value):
    for i in array:
        if i == value:
            return True
    return False


# DRIVER CODE
arr = [1, 2, 3, 4, 6, 7, 8, 9]
val = 50
# BINARY SEARCH NO LENGTH BEST ONE
start = time.perf_counter()
if binary_search_length(arr, len(arr), val):
    print("found it")
else:
    print("not found")
end = time.perf_counter()
print(f"code ran in {end-start:0.4f} seconds.")

# BINARY SEARCH GIVE LENGTH
start = time.perf_counter()
if binary_search(arr, val):
    print("found it")
else:
    print("not found")
end = time.perf_counter()
print(f"code ran in {end-start:0.4f} seconds.")


# LINEAR NOOB SEARCH
start = time.perf_counter()
if linear_search(arr, val):
    print("found it")
else:
    print("not found")
end = time.perf_counter()
print(f"code ran in {end-start:0.4f} seconds.")

#!/usr/bin/python
# Filename: binary_search.py
# Solution to Exercise 2.3-5

def binary_search_offset(haystack, needle, base_index, finded):
    """ version one, idea: base index + offset"""
    if len(haystack) < 1:
        return base_index if finded else None

    midpoint = int(len(haystack) / 2)
    middle = haystack[midpoint]

    if needle == middle:
        finded = True
        return base_index + midpoint
    elif needle < middle:
        haystack = haystack[0:midpoint]
        return binary_search_offset(haystack, needle, base_index, finded)
    elif needle > middle:
        haystack = haystack[(midpoint + 1):]
        base_index = base_index + midpoint + 1
        return binary_search_offset(haystack, needle, base_index, finded)

def binary_search_indices_recursive(haystack, needle, low, high):
    if low > high:
        return None

    mid = int((low + high) / 2)
    if needle == haystack[mid]:
        return mid
    elif needle > haystack[mid]:
        return binary_search_indices_recursive(haystack, needle, mid + 1, high)
    else:
        return binary_search_indices_recursive(haystack, needle, low, mid - 1)

def binary_search_indices_iterative(haystack, needle, low, high):
    while low <= high:
        mid = int((low + high) / 2)
        if needle == haystack[mid]:
            return mid
        elif needle > haystack[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None

def binary_search(haystack, needle, low, high):
    if low > high:
        return low

    mid = int((low + high) / 2)
    if needle == haystack[mid]:
        return mid
    elif needle > haystack[mid]:
        return binary_search(haystack, needle, mid + 1, high)
    else:
        return binary_search(haystack, needle, low, mid - 1)

if __name__ == '__main__':
    haystack = [10, 26, 30, 31, 41, 42, 43, 58, 59]
    needle = 30
    # index = binary_search(haystack, needle, 0, len(haystack) - 1)
    # haystack.insert(index, needle)
    # print haystack

    # index = binary_search_indices_iterative(haystack, needle, 0, len(haystack) - 1)

    index = binary_search_indices_recursive(haystack, needle, 0, len(haystack) - 1)

    # finded = False
    # base_index = 0
    # index = binary_search_offset(haystack, needle, base_index, finded)
    print index


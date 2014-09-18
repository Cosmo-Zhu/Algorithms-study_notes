#!/usr/bin/python
# Filename: merge_sort_pythonic.py


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged = []
        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            merged.append(left.pop(0))
        while right:
            merged.append(right.pop(0))
        return merged


    middle = int(len(lst) / 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

if __name__ == '__main__':
    A = [41, 52, 26, 38, 57, 9, 49]
    print A
    A_sorted = merge_sort(A)
    print A_sorted
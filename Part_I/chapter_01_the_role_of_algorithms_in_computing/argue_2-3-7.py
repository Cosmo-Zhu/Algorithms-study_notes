#!usr/bin/python
# -*- coding: utf-8 -*-
# Filename: argue proposition for Exercises 2.3-7 (page 39)


import merge_sort_pythonic

def argue_existence(testedList, target):
    """Let x − S = {x − y | y ∈ S}. We sort sets S and x − S and scan them to check, 
        if some element a appears in both sets. In that case, S contains both a and x − a. 
        Sorting takes O(n log n) time, while scanning takes O(n) time."""
    sorted_list = merge_sort_pythonic.merge_sort(testedList)

    i, j = 0, len(sorted_list) - 1

    while i < j:
        # check if the sum of elements at index i and j equals target, if yes we are done.
        if sorted_list[i] + sorted_list[j] == target:
            return True
        # else if the sum more than target, decrease the sum.
        elif sorted_list[i] + sorted_list[j] > target:
            j = j - 1
        # else if the sum is less than target, increase the sum.
        else:
            i = i + 1

    # failed to find any such pair..return false. 
    return False

if __name__ == '__main__':
    testedList = [41, 52, 26, 38, 12, 57, 9, 49]
    target = 38
    result = argue_existence(testedList, target)
    print result

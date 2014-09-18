#!/usr/bin/python
# Filename: insert_sorting.py

def insert_sort(is_desc=False):
    input_list = [31, 41, 59, 26, 41, 58]  # [5, 2, 4, 6, 1, 3]
    list_length = len(input_list)
    j = 1
    print input_list
    print '\n'

    if is_desc:
        while j < list_length:
            key = input_list[j]
            i = j - 1  # Insert inut_list[j] into the sorted sequence input_list[0..j - 1].
            while (i > -1) and (input_list[i] < key):
                input_list[i + 1] = input_list[i]
                i = i - 1
            input_list[i + 1] = key
            j = j + 1
            print input_list
    else:
        while j < list_length:
            key = input_list[j]
            i = j - 1   # Insert inut_list[j] into the sorted sequence input_list[0..j - 1].
            while (i > -1) and (input_list[i] > key):
                input_list[i + 1] = input_list[i]
                i = i - 1
            input_list[i + 1] = key
            j = j + 1
            print input_list

if __name__ == '__main__':
    # insert_sort()
    insert_sort()

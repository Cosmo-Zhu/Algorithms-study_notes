#!/usr/bin/python
#Filename: selection_sort.py


def select_sort():
    A = [12, 3, 7, 9, 83, 0, 23]
    bound = len(A)
    print A

    for i in xrange(0, bound - 1):
        smallest = A[i]
        index = i
        for j in xrange(i + 1, bound):
            if smallest > A[j]:
                smallest = A[j]
                index = j
        A[index] = A[i]
        A[i] = smallest
    print A

if __name__ == '__main__':
    select_sort()

# i = 0
# while i < bound - 1:
#     smallest = A[i]
#     index = i
#     j = i + 1
#     while j < bound:
#         if smallest > A[j]:
#             smallest = A[j]
#             index = j
#         j = j + 1
#     A[index] = A[i]
#     A[i] = smallest
#     i = i + 1

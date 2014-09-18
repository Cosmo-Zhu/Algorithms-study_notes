#!/usr/bin/python
# Filename: merge_sort.py


def merge(A, p, q, r):
    left_list_len = q - p + 1
    right_list_len = r - q

    # L = []
    # R = []
    # for i in xrange(0, left_list_len):
    #     L.append(A[p + i])
    # for j in xrange(0, right_list_len):
    #     R.append(A[q + j + 1])

    # Let L[0..left_list_len - 1] and R[0..right_list_len - 1] be new lists
    L = A[p:(q + 1)]
    R = A[(q + 1):(r + 1)]

    i = 0
    j = 0
    k = p

    while i < left_list_len and j < right_list_len:
        if L[i] <= R[j]:
            A[k] = L[i]
            k += 1
            i += 1
        else:
            A[k] = R[j]
            k += 1
            j += 1

    while i < left_list_len:
        A[k] = L[i]
        k += 1
        i += 1

    while j < right_list_len:
        A[k] = R[j]
        k += 1
        j += 1


def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == '__main__':
    A = [41, 52, 26, 38, 57, 9, 49]
    print A
    merge_sort(A, 0, len(A) - 1)
    print A

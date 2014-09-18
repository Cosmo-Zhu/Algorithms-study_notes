#!/usr/bin/python
# Filename: binary_adding.py which is the excercise of chapter 2.1-4

A = [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0]
B = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1]
length = len(A)
C = []
i = 1
carry = 0

while i <= length:    
    if A[length - i] + B[length - i] + carry == 2:
        C.insert(0, 0)
        # print '2  ', carry, C
        carry = 1
    elif A[length - i] + B[length - i] + carry == 3:
        C.insert(0, 1)
        # print '3  ', carry, C
        carry = 1
    else:
        result = A[length - i] + B[length - i] + carry
        C.insert(0, result)
        # print carry, C
        carry = 0
    i = i + 1

if carry != 0:
    C.insert(0, 1)

# print carry
print C
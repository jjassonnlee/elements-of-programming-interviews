"""
Write a program which takes as input an array of digits encoding a nonnegative
decimal integer D and updates the array to represent the integers D+1.
For example, if the input is [1, 2, 9], then you should update the array to
[1, 3, 0]
"""

def plus_one(A):
    carry = 1
    for i in range(len(A)-1, -1, -1):
        A[i] = A[i] + carry
        carry = A[i] // 10
        A[i] = A[i] % 10
    if carry == 1:
        A.insert(0, 1)

def plus_one_v2(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

A = [1, 2, 9]
plus_one(A)
print(A)

B = [9, 9, 9]
plus_one(B)
print(B)


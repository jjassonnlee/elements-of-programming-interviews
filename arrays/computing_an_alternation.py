"""
Given an array A, rearrange A's elements to get a new array B having the property
B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5]...
"""
def computing_an_alternation(A):
    if len(A) <= 1: return A
    B = list(A)
    for i in range(0, len(B)-1):
        if i % 2 == 0 and B[i] > B[i+1]:
            B[i], B[i+1] = B[i+1], B[i]
        elif i % 2 != 0 and B[i] < B[i+1]:
            B[i], B[i+1] = B[i+1], B[i]
    return B



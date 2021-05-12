"""
Given an array A of n elements, and a permutation P, apply P to A.
Do not use extra space.
"""
def apply_permutation(A, P):
    for i in range(len(A)):
        j = i
        while P[j] >= 0:
            A[i], A[P[j]] = A[P[j]], A[i]
            tmp = P[j]
            P[j] -= len(P)
            j = tmp

    P[:] = [a + len(P) for a in P]


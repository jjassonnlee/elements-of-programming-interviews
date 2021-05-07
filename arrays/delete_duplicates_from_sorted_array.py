"""
Given a sorted array, remove all duplicates. Modify the array in place.
Your function should return 1 + index of the last element.
"""
def delete_duplicates(A):
    if len(A) <= 1: return len(A)
    # i is the index to place the next unique element
    # j is 1 + the index of the last occurrence of the next unique element
    i = 1
    for j in range(i, len(A)):
        if A[j] != A[j-1]:
            A[i] = A[j]
            i += 1
    return i

"""
Implement a function which takes as input an array and a key,
and updates the array so that all occurrences of the input key
have been removed and the remaining elements have been shifted left
to fill the empty indices. Again, return 1 + index of last element.
"""
def delete_element(A, k):
    if len(A) <= 1: return len(A)
    n = A[k]
    i = 0
    for j in range(len(A)):
        if A[j] != n:
            A[i] = A[j]
            i += 1
    return i

"""
Given a sorted array A and a positive integer m, update A so that if x
appears m times in A, it appears exactly min(2, m) times in A.
Same as above, return the 1 + index of last element of 'new' array.
"""
def truncate_if_appear_m_times(A, m):
    if len(A) < 1 or len(A) < m:
        return len(A)

    n = min(2, m)
    i = 0
    j = 1
    while j < len(A):
        # count number of occurrences of A[j-1]
        count = 1
        while j < len(A) and A[j] == A[j-1]:
            count += 1
            j += 1
        # if count == m, make A[i] appear n times
        if count == m:
            for _ in range(n):
                A[i] = A[j-1]
                i += 1
        elif count != m:
            for _ in range(count):
                A[i] = A[j-1]
                i += 1
        j += 1
    return i


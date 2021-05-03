"""
Partition an array into three parts:
Less than, Equal to, and Greater than a pivot value
"""
def dutch_flag_partition(pivot_index, A):
    p = A[pivot_index]
    l, m, r = 0, 0, len(A)-1

    while m <= r:
        if A[m] < p:
            A[l], A[m] = A[m], A[l]
            l += 1
            m += 1
        elif A[m] == p:
            m += 1
        elif A[m] > p:
            A[m], A[r] = A[r], A[m]
            r -= 1

"""
Assuming that keys take one of three values, reorder the array
so that all objects with the same key appear together.
"""
def dutch_flag_three(A):
    i = 0
    j = 1
    k = 0
    # make i and j point and 2 diff values
    while A[j] == A[i]:
        j += 1
    # move j to end of A. now i is at 0 and j is at len(A)-1
    A[j], A[-1] = A[-1], A[j]
    j = len(A) - 1
    # use k to go thru A and swap with i or j as needed
    while k <= j:
        if A[k] == A[0]:
            A[k], A[i] = A[i], A[k]
            i += 1
            k += 1
        elif A[k] == A[-1]:
            A[k], A[j] = A[j], A[k]
            j -= 1
        else:
            k += 1

"""
Given an array A of n objects with keys that take one of four values,
reorder the array such that all objects with the same key appear together.
"""
def dutch_flag_four(A):
    a = 0
    b = 0
    c = 0
    # make a, b, c point at diff values
    while A[b] == A[a]:
        b += 1
    while A[c] == A[a] or A[c] == A[b]:
        c += 1
    # swap b to index 1; swap c to index -1
    A[1], A[b] = A[b], A[1]
    A[-1], A[c] = A[c], A[-1]
    # make a point at first element not equal to A[0]
    # make b point at first element not equal to A[a]
    # make c point at first element not equal to A[-1], counting backwards
    a = 1
    b = 1
    while A[b] == A[a]:
        b += 1
    c = len(A) - 1
    while A[c] == A[-1]:
        c -= 1

    i = b
    while i <= c:
        if A[i] == A[0]:
            A[a], A[i] = A[i], A[a]
            A[b], A[i] = A[i], A[b]
            a += 1
            b += 1
            i += 1
        elif A[i] == A[a]:
            A[b], A[i] = A[i], A[b]
            b += 1
            i += 1
        elif A[i] == A[-1]:
            A[i], A[c] = A[c], A[i]
            c -= 1
        else:
            i += 1

"""
Given an array A of n objects with Boolean-valued keys, reorder the array
such that objects with the key 'False' appear first.
"""
def dutch_flag_boolean(A):
    ...

"""
Given an array A of n objects with Boolean-valued keys, reorder the array
such that objects with the key 'False' appear first.
The relative ordering of the 'True's must be preserved
"""
def dutch_flag_boolean_v2(A):
    ...


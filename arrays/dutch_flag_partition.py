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
def variant1(A):
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
def variant2(A):


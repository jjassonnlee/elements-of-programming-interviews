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

"""
Given a sorted array, remove all duplicates. Modify the array in place.
Your function should return 1 + index of the last element.
"""
def delete_duplicates(A):
    if len(A) <= 1: return
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
def delete_element(A):
    ...

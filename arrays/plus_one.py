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

"""
Take two strings of bits encoding binary numbers, and return a new
string of bit representing the sum of the two numbers.
"""
def add_binary_strings(s, t):
    # zero pad the shorter string
    if len(s) < len(t):
        s = (len(t) - len(s)) * '0' + s
    if len(s) > len(t):
        t = (len(s) - len(t)) * '0' + t
    # iterate backwards and add the digits; carry if needed
    ans = []
    carry = 0
    for i in range(len(s) - 1, -1, -1):
        mod = int(s[i]) + int(t[i]) + carry
        carry = mod // 2
        mod = mod % 2
        ans.insert(0, str(mod))
    if carry == 1:
        ans.insert(0, '1')
    return "".join(ans)



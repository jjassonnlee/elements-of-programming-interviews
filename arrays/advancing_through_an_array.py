"""
Given an array of integers where A[i] denotes the maximum you can advance from index i,
return whether it is possible to advance to the last index starting from index 0
"""
def advancing_through_an_array(A):
    max_reach = 0
    i = 0
    while i <= max_reach and max_reach < len(A)-1:
        max_reach = max(max_reach, A[i]+i)
        i += 1
    return max_reach >= len(A)-1

"""
Write a program to compute minimum number of steps needed to advance to the last index.
Return -1 if you can't reach the last index.
"""
def minimum_steps(A):
    # Init dp array. Use len(A) as init val because max steps possible is len(A)-1
    dp = [len(A)] * len(A)
    dp[0] = 0

    for i in range(len(A)):
        for j in range(i+1, i+A[i]+1):
            if j < len(A):
                dp[j] = min(1+dp[i], dp[j])

    return -1 if dp[-1] == len(A) else dp[-1]

def minimum_steps_v2(A):
    """
    I found this answer on leetcode that uses O(1) space instead of O(n)
    """
    l = 0
    r = A[0]
    ans = 1
    while r < len(A)-1:
        ans += 1
        nxt = max(i + A[i] for i in range(l, r+1))
        l, r = r, nxt
    return ans


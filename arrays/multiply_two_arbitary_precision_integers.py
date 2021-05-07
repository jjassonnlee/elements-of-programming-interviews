"""
Write a program that takes two arrays representing integers, and returns an
array of integers representing their product.
"""
def multiply(x, y):
    sign = -1 if (x[0] < 0) ^ (y[0] < 0) else 1
    x[0], y[0] = abs(x[0]), abs(y[0])
    ans = [0] * (len(x) + len(y))

    for i in reversed(range(len(x))):
        for j in reversed(range(len(y))):
            ans[i + j + 1] += x[i] * y[j]
            ans[i + j] += ans[i + j + 1] // 10
            ans[i + j + 1] %= 10

    # ignore leading 0s
    i = 0
    while ans[i] == 0:
        i += 1

    return [sign * ans[i]] + ans[i+1:]


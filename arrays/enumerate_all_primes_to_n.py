"""
Generate a list of all primes in the range [1,n]
"""
def generate_primes(n):
    is_prime = [False, False] + [True] * (n-1)
    ans = []

    for i in range(2, n+1):
        if is_prime[i]:
            ans.append(i)
            # Sieve p's multiples
            for j in range(i, n+1, i):
                is_prime[j] = False
    return ans



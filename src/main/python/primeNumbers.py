def gen_primes(M=0, N=0):
    """Generate primes up to N"""

    primes=set()
    for n in range(N):
        if n>1:
            if all(n % p > 0 for p in primes):
                primes.add(n)
                if n>=M:
                    yield n

a, b=100, 200
print(*gen_primes(a, b))

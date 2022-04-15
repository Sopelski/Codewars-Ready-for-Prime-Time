'''Method that takes a maximum bound and returns all primes up to and including the maximum bound.'''

def prime(n):
    liczby = []
    sieve = set(range(2, n+1))
    while sieve:
        prime = min(sieve)
        liczby.append(prime)
        sieve -= set(range(prime, n+1, prime))
    return print(liczby)

prime(50)
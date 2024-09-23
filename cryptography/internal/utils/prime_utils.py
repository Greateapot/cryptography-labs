"""
is_prime_trial_division, is_prime_miller_rabin, is_prime functions
source: https://gist.github.com/ppoffice/e10e0a418d5dafdd5efe9495e962d3d2
"""

import random
from math import ceil, sqrt


def is_prime_trial_division(n: int) -> bool:
    """Test if a given integer n is a prime number using trial division"""
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


# prime numbers with 1000
known_primes = [2] + [x for x in range(3, 1000, 2) if is_prime_trial_division(x)]


def is_prime_miller_rabin(n: int, precision: int) -> bool:
    """Test if a given integer n is a prime number using miller-rabin test
    https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Probably_correct_answers
    """

    def try_composite(a, d, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, pow(2, i) * d, n) == n - 1:
                return False
        return True

    if n % 2 == 0:
        return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(try_composite(a, d, s) for a in known_primes[:2])
    if n < 25326001:
        return not any(try_composite(a, d, s) for a in known_primes[:3])
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(try_composite(a, d, s) for a in known_primes[:4])
    if n < 2152302898747:
        return not any(try_composite(a, d, s) for a in known_primes[:5])
    if n < 3474749660383:
        return not any(try_composite(a, d, s) for a in known_primes[:6])
    if n < 341550071728321:
        return not any(try_composite(a, d, s) for a in known_primes[:7])
    return not any(try_composite(a, d, s) for a in known_primes[:precision])


def is_prime(n: int, precision: int = 16) -> bool:
    """Test if a given integer is a prime number"""
    assert n > 0
    if n in known_primes:
        return True
    elif n < 100000:
        return is_prime_trial_division(n)
    else:
        return is_prime_miller_rabin(n, precision)


def generate_prime(n: int = 512) -> int:
    """Generates prime number with bitlength `n`."""
    assert n > 0 and n < 4096

    x = random.getrandbits(n)
    if not x & 1:
        x += 1

    prime = 0

    while prime == 0:
        if is_prime(x):
            prime = x
        x += 2

    return prime


__all__ = (
    "generate_prime",
    "is_prime",
    "is_prime_miller_rabin",
    "is_prime_trial_division",
)

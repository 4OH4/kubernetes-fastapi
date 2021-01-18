# -*- coding: utf-8 -*-
"""
Long-running calculation to provide some work for the API to do

@author: 4oh4

Run from directory above to test:
python -m logic.business_logic

"""


import math
import time
import random

max_range = 2500000000000


def calc_largest_prime_factor(n: int):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return int(prime_factor)


def run_prime_factor_calculation():

    n = int(random.uniform(max_range // 2, max_range))

    t0 = time.time()
    largest_prime_factor = calc_largest_prime_factor(n)
    elapsed_time = time.time() - t0

    return n, largest_prime_factor, elapsed_time


if __name__ == "__main__":

    n, largest_prime_factor, elapsed_time = run_prime_factor_calculation()

    print(
        f"The largest prime factor of {n} is {largest_prime_factor}. Calculation took {elapsed_time:0.3f} seconds."
    )

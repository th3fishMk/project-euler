# Problem 007
# 10 001st prime


from sympy import *

primes = []
last_number = 2

while len(primes) < 10_001:
    if isprime(last_number):
        primes.append(last_number)
    last_number += 1

print(primes.pop())

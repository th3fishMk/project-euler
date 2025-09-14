# Problem 003
# Largest Prime Factor

def find_prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors


factors = find_prime_factors(600851475143)
print(factors.pop())

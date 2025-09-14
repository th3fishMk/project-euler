# problem 005
# Smallest multiple

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]


def find_prime_divisors(num):
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


smallest = 1
for i in range(1, 21):
    if (smallest % i == 0):
        pass
    elif i in prime_numbers:
        smallest = smallest * i
    else:
        divs = find_prime_divisors(i)
        divisible = False
        for div in divs:
            smallest = smallest*div
            if smallest % i == 0:
                break

print(smallest)

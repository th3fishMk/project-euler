import sympy
# Problem 35
# circular primes

prospects = [2, 3, 5, 7]
new_circulars = [1, 3, 7, 9]

valid_digits = [1, 3, 7, 9]

for x in new_circulars:
    if len(str(x)) >= 7:
        break
    for y in valid_digits:
        new_number = int(str(x) + str(y))
        if sympy.isprime(new_number):
            new_circulars.append(new_number)

new_circulars = new_circulars[4:]

for i in new_circulars:
    prospects.append(i)

prospects.sort()

circulars = []

for i in prospects:
    is_circular = True
    i_string = str(i)
    for x in range(len(i_string)):
        sliced = i_string[1:]
        sliced += i_string[:1]
        if not sympy.isprime(int(sliced)):
            is_circular = False
    if is_circular:
        circulars.append(i)


print(len(circulars))

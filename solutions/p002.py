# Problem 002

fibs = [1, 2]
sum = 0
while (fibs[-1] < 4_000_000):
    fibs.append(fibs[-2] + fibs[-1])

for i in fibs:
    if (i % 2 == 0):
        sum += i

print(sum)

# Problem 001

sum = 0
for i in range(1, 1000):
    if i % 5 == 0 or i % 3 == 0:
        sum += i
print(sum)

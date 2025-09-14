# Problem 001
# Multiples of 3 or four

sum = 0
for i in range(1, 1000):
    if i % 5 == 0 or i % 3 == 0:
        sum += i
print(sum)

# problem 003

sumOfSquares = 0

for i in range(1, 101):
    sumOfSquares += i**2

squareOfSum = 0

for i in range(1, 101):
    squareOfSum += i
squareOfSum = squareOfSum ** 2

print(squareOfSum-sumOfSquares)

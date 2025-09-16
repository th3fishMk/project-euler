# P004
# largest palindrome product
palindromes = []

def is_palindromic(num):
    if str(num)[::-1] == str(num):
        return True

for x in range(1000,900,-1):
    for y in range(1000,900,-1):
        testing = x*y
        if is_palindromic(testing):
            palindromes.append(testing)

palindromes.sort()

print(palindromes.pop())

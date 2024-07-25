numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

def isPrimes(number):
    if number < 1:
        return False
    if number < 3:
        return True

    for i in range(2, number - 1):
        if number % i == 0:
            return False

    return True


for i in numbers:
    if isPrimes(i):
        primes.append(i)
    else:
        not_primes.append(i)

print('Простые числа:')
print(primes)
print('Непростые числа:')
print(not_primes)
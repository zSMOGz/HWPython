def is_prime(func):
    def wrapper(first, second, three):
        result = func(first, second, three)

        if result < 1:
            print('Составное')
        elif result < 3:
            print('Простое')
        else:
            is_prime_result = True
            for i in range(2, result - 1):
                if result % i == 0:
                    print('Составное')
                    is_prime_result = False
                    break
            if is_prime_result:
                print('Простое')

        return result

    return wrapper


@is_prime
def sum_three(first, second, three):
    return first + second + three


result = sum_three(2, 3, 6)
print(result)

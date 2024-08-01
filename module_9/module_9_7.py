
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            print('Составное')
        else:
            for i in range(2, int(result)):
                if result % i == 0:
                    print('Составное')
                    break
            else:
                print('Простое')

        return result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

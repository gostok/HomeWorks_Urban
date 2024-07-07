numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
a = 0 

for i in range(len(numbers)):
    is_prime = True 
    a = numbers[i]
    
    # убираем число '1':
    if a < 2:   
        print(a) 
        continue
    
    b = a ** (1 / 2)

    for j in range(2, int(b + 1)):
        if a % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
            break

    if not (is_prime):
        not_primes.append(a)
    else:
        primes.append(a)



print('Простые числа' , primes)
print('Не простые числа' , not_primes)
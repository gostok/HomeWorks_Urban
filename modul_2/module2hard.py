

import random

def get_cipher():
    list_cipher = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num_cipher = range(3, 21)
    cipher = random.choice(num_cipher)
    return cipher

n = get_cipher()
print('Шифр: ', n) 

def get_password(n):
    dict_password = {
    
        3: 12,
        4: 13,
        5: 1423,
        6: 121524,
        7: 162534,
        8: 13172635,
        9: 1218273645,
        10: 141923283746,
        11: 11029384756,
        12: 12131511124210394857,
        13: 112211310495867,
        14: 1611325212343114105968,
        15: 1214114232133124115106978,
        16: 1317115262143531341251161079,
        17: 11621531441351261171089,
        18: 12151811724272163631545414513612711810,
        19: 118217316415514613712811910,
        20: 13141911923282183731746416515614713812911   

    }
    password = dict_password.get(n)
    return password



num_password = range(1, n)
num_password_2 = range(1, n)
list_password = []
result = ''

for i in num_password:
    for j in num_password_2:
        n_pass = i
        n_pass2 = j
        if n_pass >= n_pass2:
            continue
        else:
            kratno_ = n % (n_pass + n_pass2)
            if kratno_ == 0:
                list_password.append([n_pass, n_pass2])
                result = result + str(n_pass) + str(n_pass2)

print('Пары чисел: ', * list_password)
print('Пароль: ', result, '')

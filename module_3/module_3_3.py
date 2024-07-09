# 1.Функция с параметрами по умолчанию:

# def print_params(a = 1, b = 'str', c = True):
#     print(a, b, c)

# print_params(a = 'str', b = False, c = 123)
# print_params(b = 25)
# print_params(c = [1, 2, 3])


# 2.Распаковка параметров:

# def print_params(a, b, c, d, e, f):
    
#     print(a, b, c, d, e, f)

# values_list = [1, 2, 3]
# values_dict = {
#     'd':
#     25,
#     'e':
#     'str',
#     'f':
#     True
    
# }
# print_params(*values_list, **values_dict)


# 3.Распаковка + отдельные параметры:

def print_params(a, b, c):
    print(a, b, c)

values_list_2 = [25, 'str']
print_params(*values_list_2, 42)
# Работа со словарями:
my_dict = {'Anton':
           1999,
           'Andrey':
           1991,
           'Sergey':
           2002
       
}
print(my_dict)
print(my_dict.get('Anton'))
print(my_dict.get('Denis'))


my_dict.update({
    'Denis':
    2001,
    'Alex':
    1998

})
print(my_dict)


a = my_dict.pop('Sergey')
print(my_dict)
print(a)


# Работа с множествами:
my_set = {1, 2 , 2, 'book', 'book', 1, 5, 2, 1, False, False }
print(my_set)

my_set.update({26,27})
my_set.discard(2)
print(my_set)
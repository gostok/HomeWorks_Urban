# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99



data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]


def calculate_structure_sum(*args):
    global data_structure

    sum1 = sum(data_structure[0]) # 1. [1, 2, 3]
    print(sum1)

    dict_ = dict(data_structure[1])
    items_1 = dict_.items()
    sum2 = sum(data_structure[1].values()) + len(items_1) # 2. {'a': 4, 'b': 5}
    print(sum2)

    list_1 = list(data_structure[2])  
    dict_1 = list_1.pop(1)
    items_2 = list(dict_1.keys())
    sum3 = list_1[0] + len(items_2[0]) + len(items_2[1]) + sum(dict_1.values())  # 3. (6, {'cube': 7, 'drum': 8})
    print(sum3)

    sum4 = len(data_structure[3])  # 4. Hello
    print(sum4)

    list_2 = list(data_structure[4])
    list_2_2 = list(list_2[1])
    list_2_3 = list(list_2_2[0])
    list_2_4 = list(list_2_3[0])
    print(list_2_4)
    list_3 = list(list_2_4[2])
    print(list_3)
    str_1 = len(list_2_4[1]) # 'Urban'
    str_2 = len(list_3[0]) # 'Urban2'
    sum5 = list_2_4[0] + list_3[1] + str_1 + str_2 # 5. ((), [{(2, 'Urban', ('Urban2', 35))}])
    print(sum5) 

    sum_all = sum1 + sum2+ sum3 + sum4 + sum5
    data_structure = sum_all
    return data_structure
   

result = calculate_structure_sum(data_structure)
print(result) 




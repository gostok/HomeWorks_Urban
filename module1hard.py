#дан список:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#дано множество:
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# переводим множество в список с помощью list() и отсортируем в Алфавитном порядке с помощью sorted()
students_list = list(sorted(students))
print(students_list)

# находим средние баллы в списке grades sum() / len() 
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
c = sum(grades[2]) / len(grades[2])
d = sum(grades[3]) / len(grades[3])
e = sum(grades[4]) / len(grades[4])

#объединяем значения переменных в один список
grades_2 = [a, b, c, d, e]
print(grades_2)


# создаем словарь, соединяя два списка, с помощью класса dict() - словарь; и функции zip(), которая соединяет два разных списка
dictionary_ = dict(zip(students_list, grades_2))

print(dictionary_)
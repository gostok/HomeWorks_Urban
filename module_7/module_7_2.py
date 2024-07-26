import io
from pprint import pprint as pp

def custom_write(file_name, strings):

    strings_position = {}

    file = open(file_name, 'w', encoding='utf-8')

    num_string = 1
    for i in strings:
        start_ = file.tell()
        file.write(i + '\n')
        strings_position[(num_string, start_)] = i
        num_string += 1

    file.close()
    return strings_position



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
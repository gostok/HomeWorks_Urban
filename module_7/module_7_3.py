

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                words = []

                for i in lines:
                    lower_lines = i.strip().lower()

                    for j in punctuation:
                        lower_lines = lower_lines.replace(j, '')

                    strings = lower_lines.split()
                    words.extend(strings)

                all_words[name] = words

        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1


        return result

    def count(self, word):
        result = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                result[name] = count
        return result


# № 1

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


# № 2

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))


# № 3

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))


# № 4

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))


# № 5

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))

def all_variants(text):

    for i in range(1, len(text) + 1):

        for j in range(len(text) - i + 1):
            yield text[j:j+i]


a = all_variants("abc")
for i in a:
     print(i)
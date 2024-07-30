def all_variants(text: str):
    for i in range(1, len(text) + 1):
        for j in range(len(text) - (i - 1)):
            yield text[j:(i + j)]  # возвращает значение


a = all_variants("abc")

for i in a:
    print(i)

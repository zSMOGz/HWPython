def custom_write(file_name, strings):
    try:
        file = open(file_name, 'w', encoding='utf-8')
    except:
        return None

    strings_positions = {}
    string_index = 0
    for current_string in strings:
        strint_key = (str(string_index), file.tell())
        strings_positions[strint_key] = current_string

        file.write(f'{current_string}\n')

        string_index += 1
    file.close()

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

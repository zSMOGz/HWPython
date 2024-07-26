def get_multiplied_digits(number: int):
    str_number = f'{number}'
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number[0])


while True:
    try:
        str_number = input('Введите число: ')
        print(get_multiplied_digits(int(str_number)))
    except:
        print('Вы ввели не число')

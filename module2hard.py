def get_combination():
    combination = []

    for first_number_in_combination in range(1, seed - 1):
        for count_try_find_element in range(1, seed - 1):
            element2 = count_try_find_element + first_number_in_combination

            if seed % (first_number_in_combination + element2) == 0:
                combination.append(first_number_in_combination)
                combination.append(element2)

    for index_element in range(0, len(combination)):
        if (index_element % 2 == 0
                or index_element == 0):
            print(f'{combination[index_element]},', end = ' ')
        else:
            print(combination[index_element])

is_continue = False

seed = 0

while not is_continue:
    try:
        seed = int(input('Введите целое число больше 2: '))
        if seed <= 2:
            print('Ошибка ввода, я же просил число больше 2!')
        else:
            get_combination()
    except:
        print('Ошибка ввода, я же просил число!')


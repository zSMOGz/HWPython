calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(input_str: str):
    count_calls()

    return (len(input_str),
            input_str.upper(),
            input_str.lower())

def is_contains(check_str: str,
                list_to_search: list):
    count_calls()

    # Если нужно принебречь регистром, то оператором in не обойтись
    for current_line in list_to_search:
        if check_str.upper() == current_line.upper():
            return True

    return False

print(string_info('1, 2, 3, 4, 5'))
print(string_info('Эту строку нельзя понять'))
print(string_info('7, 11, 16'))
print(string_info('Пришло время разбираться'))
print(is_contains('БарАн', ["Ан24", "Банан", "Олень"]))
print(is_contains('сТроКу',['Эту', 'строку', 'нельзя', 'понять']))
print(calls)
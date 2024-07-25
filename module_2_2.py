try:
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    third = int(input('Введите третье число: '))
except:
    print('Ошибка ввода')

if first == second == third:
    print(3)
elif (first != second
      and first != third
      and second != third):
    print(0)
else:
    print(2)

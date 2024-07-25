my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_my_list: int = -1

while True:
    index_my_list += 1

    if (index_my_list >= len(my_list)
            or my_list[index_my_list] < 0): #Отличный стандарт, очень нравится. Красиво
        break

    if my_list[index_my_list] == 0:
        continue

    print(my_list[index_my_list])
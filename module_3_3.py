def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, "Два", 3.33]
values_dict = {'a': 'А', 'b': 'B', 'c': 'C'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'Три']
print_params(*values_list_2, False)

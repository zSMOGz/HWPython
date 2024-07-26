def calculate_structure_sum(sum_numbers: float, *args):
    inner_value = 0.0

    for arg in args:
        if arg is None:
            return sum_numbers
        elif isinstance(arg, float):
            return sum_numbers + arg
        elif isinstance(arg, int):
            return sum_numbers + arg
        elif isinstance(arg, str):
            return sum_numbers + len(arg)
        elif isinstance(arg, bool):
            return sum_numbers
        elif (isinstance(arg, list)
              or isinstance(arg, tuple)
              or isinstance(arg, set)):
            for line in arg:
                inner_value = calculate_structure_sum(sum_numbers, line)
                if inner_value is not None:
                    sum_numbers = inner_value
            return sum_numbers
        elif isinstance(arg, dict):
            for line in arg.items():
                inner_value = calculate_structure_sum(sum_numbers, line)
                if inner_value is not None:
                    sum_numbers = inner_value
            return sum_numbers


global_sum_numbers = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
global_sum_numbers = calculate_structure_sum(global_sum_numbers, data_structure)
print(global_sum_numbers)

def get_matrix(n, m, value):
    if (n < 1
            or m < 2):
        return

    matrix = []

    for i in range(n):
        line = []
        for j in range(m):
            line.append(value)

        matrix.append(line)

    return matrix

print(get_matrix(5, 6, 1))
print(get_matrix(3, 3, 555))
print(get_matrix(1, 4, 4))

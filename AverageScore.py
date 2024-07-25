import statistics

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted(students)

average_score = {}

indexGades = 0
for student in students:
    average_score[student] = round(statistics.fmean(grades[indexGades]), 2)
    indexGades += 1

print(average_score)
team1_num = 6
team2_num = 6
print("В команде Мастера кода участников: %i!" % team1_num)
print("В команде Волшебники данных участников: %(team_num)i!" % {"team_num": team2_num})
print('')
print("Итого сегодня в командах участников: %i и %i!" % (team1_num, team2_num))
score1 = 40
score2 = 42
print('')
print("Команда Мастера кода решила задач: {0}!".format(score1))
print("Команда Волшебники данных решила задач: {score}!".format(score=score2))
team1_time = 1552.512
team2_time = 2153.31451
print('')
print("Мастера кода решили задачи за {0} с!".format(team1_time))
print("Волшебники данных решили задачи за {0} с!".format(team2_time))

print('')
print(f"Команды решили {score1} и {score2} задач")

tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
print('')
print(f"Результат битвы: {challenge_result}")
print('')
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

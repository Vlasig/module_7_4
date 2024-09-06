# Использование %:

team1_num = 5 # Количество участников первой команды
team2_num = 6 # Количество участников второй команды
print("В команде Мастера кода участников: %d!" %(team1_num))
print("Итого сегодня в командах участников: %d и %d!" %(team1_num, team2_num))

# Использование format():

score_1 = 40 # Количество очков первой команды
score_2 = 42 # Количество очков второй команды
team1_time = 1552.512 # Время первой команды
team2_time = 2153.31451 # Время второй команды
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team1_time))

# Использование f-строк:

def challenge_result(score_1, score_2, team1_time, team2_time):
    tasks_total = score_1 + score_2
    time_avg = round(((team1_time + team2_time) / tasks_total), 1)
    print(f'Команды решили {score_1} и {score_2} задач.')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Мастера кода'
        print(f'Результат битвы: победа команды {result}!')
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Волшебники данных'
        print(f'Результат битвы: победа команды {result}!')
    else:
        result = 'Ничья'
        print(f'Результат битвы: {result}!')

challenge_result(score_1, score_2, team1_time, team2_time)



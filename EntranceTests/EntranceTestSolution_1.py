"""
Задача 1. Перевод секунд в минуты и часы
Напишите программу, которая переводит переданное количество секунд в часы и минуты.
Обратите внимание: необходимо указывать корректное склонение слов (секунда/секунды/секунд, минута/минуты/минут,
час/часа/часов).
На стандартный поток ввода подается количество секунд, в ответ программа выводит его в виде часов, минут и секунд.
Если значение часов/минут/секунд равно нулю, то оно не выводится.

Пример 1:
Ввод: 3600
Вывод: 1 час

Пример 2:
Ввод: 75
Вывод: 1 минута 15 секунд

Пример 3:
Ввод: 7205
Вывод: 2 часа 5 секунд
"""


# Решение
def get_time():
    temp = input('Введите количество секунд:')
    if temp == '':
        raise Exception("Вы ничего не ввели")
    elif int(temp) < 0:
        raise Exception("Введённое число меньше 0")
    else:
        temp = int(temp)
        return [temp // 60 // 60, temp // 60 % 60, temp % 60]


def set_user_friendly_time_text(x):
    time_text = [[' час', ' часа', ' часов'],
                [' минута', ' минуты', ' минут'],
                [' секунда', ' секунды', ' секунд']]
    result = []
    for i in range(len(x)):
        if x[i] > 0:
            if x[i] % 100 // 10 == 1:
                result += str(x[i]) + time_text[i][2]
            elif x[i] % 10 == 1:
                result.append(str(x[i]) + time_text[i][0])
            elif 2 <= x[i] % 10 <= 4:
                result.append(str(x[i]) + time_text[i][1])
            elif 5 <= x[i] % 10 <= 9:
                result.append(str(x[i]) + time_text[i][2])
    return result


while True:
    try:
        print(" ".join(map(str, set_user_friendly_time_text(get_time()))))
        break
    except Exception as e:
        print(e)
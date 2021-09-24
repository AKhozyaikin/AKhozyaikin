# -*- coding: utf-8 -*-
import random
import time
# получаем кол-во часов и привидим их в минутный вид
all_time = int(25)

#собираю пустой список
times = []
i = 0

#забиваем массив со временем данніми
while i <= all_time:
    #подсчет длинні временного отрезка
    long_time = round(random.uniform(4.8, 5.2), 1)
    times.append(long_time)
    i = i + 1

#из списка формируем кортеж
times_s = tuple(times)
massive_elem = len(times)
print(times_s, massive_elem)

#проверка общего кол-ва времени
number_massive_elem = 0 #обьявляем переменную, в коротой будет храниться значение времени всех сегментов времени без 0-го
all_time_in_all_segments = round(sum(times), 1) - times[0]
print(all_time_in_all_segments)



#Проверка таймера по времени в количестве элементов массива
while number_massive_elem < massive_elem:
    #time.sleep(times[number_massive_elem] * 60)
    print(times[number_massive_elem])
    number_massive_elem = number_massive_elem + 1

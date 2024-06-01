x = [] # создаём массив
summ = 0 # создаём переменную для подсчёта суммы
import random # подключаем модуль работы со случайными величинами
for i in range(100): # добавляем случайные значения в массив
    x.append(random.randint(1,50))
for i in range(100): # суммируем все значения в массиве
    summ += x[i]
print("Сумма: ", summ)
print("Среднее значение: ", summ / 100)

from collections import deque
st = deque() # создаём стек
another_element = 0 # создаём переменную для подсчёта суммы
import random # подключаем модуль работы со случайными величинами
for i in range(100): # добавляем случайные значения в массив
    st.append(random.randint(1,50))
for j in range(100): # суммируем все значения в массиве
    another_element += st.pop()
print("Сумма: ", another_element)
print("Среднее значение: ", another_element / 100)


x = [] # создаём массив
summ = 0 # создаём переменную для подсчёта суммы
import random # подключаем модуль работы со случайными величинами
for i in range(100): 
    x.append(random.randint(1,50))
max = x[0]
min = x[0]
for i in range(100): 
    if max < x[i]:
        max = x[i]
    if min > x[i]:
        min = x[i]
print("Максимальное значение: ", max)
print("Минимальное значение: ", min)

import random # подключаем модуль работы со случайными величинами
from collections import deque
st = deque() # создаём стек
for i in range(100): 
    st.append(random.randint(1,50))
max = st.pop()
min = st.pop()
for i in range(98):
    element_stack = st.pop()
    if max < element_stack:
        max = element_stack
    if min > element_stack:
        min = element_stack
print("Максимальное значение: ", max)
print("Минимальное значение: ", m)


import random
# 100 самых популярных глаголов в английском языке
verbs = ['be', 'have', 'do', 'say', 'go', 'can', 'get', 'would', 'make', 
       'know', 'will', 'think', 'take', 'see', 'come', 'could', 'want',
       'look', 'use', 'find', 'give', 'tell', 'work', 'may', 'should', 'call',
       'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep',
       'let', 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'might', 'show', 
       'hear', 'play', 'run', 'move', 'like', 'live', 'believe', 'hold', 'bring',
       'happen', 'must', 'write', 'provide', 'sit', 'stand', 'lose', 'pay',
       'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 
       'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read',
       'allow', 'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 
       'remember', 'love', 'consider', 'appear', 'buy', 'wait', 'serve', 'die',
       'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain']
# список со значениями от 1 до 100
list_one = [ ]
for g in range(1, 101):
    list_one.append(g)
dictionary_one = {}
# заполняем словарь: 100 случайных пар ключ + строка
for i in range(100):
    dictionary_one[list_one[i]] = random.choice(verbs)
# считываем по ключам все значения и выводим
for j in range(1, len(dictionary_one) + 1):
    print(dictionary_one.get(j))
# затем удаляем все пары
for k in range(1, len(dictionary_one) + 1):
    del dictionary_one[k]

import random
from collections import deque
# 100 самых популярных глаголов в английском языке
verbs = ['be', 'have', 'do', 'say', 'go', 'can', 'get', 'would', 'make', 
       'know', 'will', 'think', 'take', 'see', 'come', 'could', 'want',
       'look', 'use', 'find', 'give', 'tell', 'work', 'may', 'should', 'call',
       'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep',
       'let', 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'might', 'show', 
       'hear', 'play', 'run', 'move', 'like', 'live', 'believe', 'hold', 'bring',
       'happen', 'must', 'write', 'provide', 'sit', 'stand', 'lose', 'pay',
       'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 
       'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read',
       'allow', 'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 
       'remember', 'love', 'consider', 'appear', 'buy', 'wait', 'serve', 'die',
       'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain']
# список со значениями от 1 до 100
st = deque() # создаём стек
for g in range(1, 101):
    st.append(g)
dictionary_one = {}
# заполняем словарь: 100 случайных пар ключ + строка
for i in range(100):
    dictionary_one[st.pop()] = random.choice(verbs)
# считываем по ключам все значения и выводим
for j in range(1, len(dictionary_one) + 1):
    print(dictionary_one.get(j))
# затем удаляем все пары
for k in range(1, len(dictionary_one) + 1):
    del dictionary_one[k]


def number_of_repetitions(list_of_val, n_1):
    dictionary_of_numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0} # создание словаря с ключами от 1 до 10
    final_list = [] # создание итогового (возвращаемого) списка 
    for w in range(len(list_of_val)): # подсчёт повторений каждого числа
        if list_of_val[w] == 1:
            dictionary_of_numbers[1] = dictionary_of_numbers[1] + 1
        if list_of_val[w] == 2:
            dictionary_of_numbers[2] = dictionary_of_numbers[2] + 1
        if list_of_val[w] == 3:
            dictionary_of_numbers[3] = dictionary_of_numbers[3] + 1
        if list_of_val[w] == 4:
            dictionary_of_numbers[4] = dictionary_of_numbers[4] + 1
        if list_of_val[w] == 5:
            dictionary_of_numbers[5] = dictionary_of_numbers[5] + 1
        if list_of_val[w] == 6:
            dictionary_of_numbers[6] = dictionary_of_numbers[6] + 1
        if list_of_val[w] == 7:
            dictionary_of_numbers[7] = dictionary_of_numbers[7] + 1
        if list_of_val[w] == 8:
            dictionary_of_numbers[8] = dictionary_of_numbers[8] + 1
        if list_of_val[w] == 9:
            dictionary_of_numbers[9] = dictionary_of_numbers[9] + 1
        if list_of_val[w] == 10:
            dictionary_of_numbers[10] = dictionary_of_numbers[10] + 1
    for e in range(1, len(dictionary_of_numbers) + 1): # добавление в итоговый список всех значений, превышающих N
        if dictionary_of_numbers.get(e) > n_1:
            final_list.append(e)
    return final_list

from collections import deque
def number_of_repetitions(list_of_val, n_1):
    dictionary_of_numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0} # создание словаря с ключами от 1 до 10
    st = deque() # создаём стек
    st.append('e')
    for w in range(len(list_of_val)): # подсчёт повторений каждого числа
        if list_of_val[w] == 1:
            dictionary_of_numbers[1] = dictionary_of_numbers[1] + 1
        if list_of_val[w] == 2:
            dictionary_of_numbers[2] = dictionary_of_numbers[2] + 1
        if list_of_val[w] == 3:
            dictionary_of_numbers[3] = dictionary_of_numbers[3] + 1
        if list_of_val[w] == 4:
            dictionary_of_numbers[4] = dictionary_of_numbers[4] + 1
        if list_of_val[w] == 5:
            dictionary_of_numbers[5] = dictionary_of_numbers[5] + 1
        if list_of_val[w] == 6:
            dictionary_of_numbers[6] = dictionary_of_numbers[6] + 1
        if list_of_val[w] == 7:
            dictionary_of_numbers[7] = dictionary_of_numbers[7] + 1
        if list_of_val[w] == 8:
            dictionary_of_numbers[8] = dictionary_of_numbers[8] + 1
        if list_of_val[w] == 9:
            dictionary_of_numbers[9] = dictionary_of_numbers[9] + 1
        if list_of_val[w] == 10:
            dictionary_of_numbers[10] = dictionary_of_numbers[10] + 1
    for e in range(1, len(dictionary_of_numbers) + 1): # добавление в итоговый список всех значений, превышающих N
        if dictionary_of_numbers.get(e) > n_1:
            st.append(e)
    return st


def UFO(N, data, octal):
    final_list = [] # список для формирования ответа
    for i in range(N):
        if octal == True: # перевод в восмиричную систему счисления очередного элемента исходного списка
            decimal_number = int(str(data[i]), 8)
            final_list.append(decimal_number)
        if octal == False:  # перевод в шестнадцатиричную систему счисления очередного элемента исходного списка
            decimal_number = int(str(data[i]), 16)
            final_list.append(decimal_number)     
    return final_list

from collections import deque
def UFO(N, data, octal):
    st = deque() # создаём стек
    for i in range(N):
        if octal == True: # перевод в восмиричную систему счисления очередного элемента исходного списка
            decimal_number = int(str(data[i]), 8)
            st.append(decimal_number)
        if octal == False:  # перевод в шестнадцатиричную систему счисления очередного элемента исходного списка
            decimal_number = int(str(data[i]), 16)
            st.append(decimal_number)     
    return final_list

# 4. Шум, переименованы переменные, удалены очевидные комментарии
x = float(input()) # вводим первое число
y = float(input()) # вводим второе число
# преобразовываем введённые числа
x = int(x * 1000)
y = int(y * 1000)
# сравниваем преобразованные числа
if x == y:
    print("Числа совпадают до третьего знака после запятой")
else
    print("Числа не совпадают до третьего знака после запятой")

first_number = float(input())
second_number = float(input())
first_number = int(x * 1000) # преобразовываем введённые числа
second_number = int(y * 1000)
if first_number == second_number:
    print("Числа совпадают до третьего знака после запятой")
else
    print("Числа не совпадают до третьего знака после запятой")


# 4. Шум, переименованы переменные, удалены очевидные комментарии
x = int(input()) # год рождения
if x % 100 == 0 and x % 400 != 0 or x % 4 != 0:
    print(x, "- не високосный год")
else: 
    print(x, "- високосный год")

year_of_birth = int(input())
if year_of_birth % 100 == 0 and year_of_birth % 400 != 0 or year_of_birth % 4 != 0:
    print(year_of_birth, "- не високосный год")
else: 
    print(year_of_birth, "- високосный год")


# 4. Шум, переименованы переменные, удалены очевидные комментарии
x1 = int(input()) # количество ящиков золота, которые утащил Джек
x2 = int(input()) # количество ящиков золота, которые утащил Джон
x3 = int(input()) # количество ящиков золота, которые утащил Джун
if x1 == x2 == x3:
    print("all equals")
elif x1 != x2 and x1 != x3 and x2 != x3:
    print("all different")
else:
    print("equal or different")

Jacks_drawers = int(input())
Johns_boxes = int(input())
Junes_drawers = int(input())
if Jacks_drawers == Johns_boxes == Junes_drawers:
    print("all equals")
elif Jacks_drawers != Johns_boxes and Jacks_drawers != Junes_drawers and Johns_boxes != Junes_drawers:
    print("all different")
else:
    print("equal or different")


# 4. Шум, переименованы переменные, удалены очевидные комментарии
N = int(input()) # вводим число до которого включительно будем суммировать
sum = 0 # задаём переменную в которой будет накапливаться сумма
for i in range(1, N + 1): 
    sum += i 
print("Сумма чисел равна", sum)

N = int(input()) # вводим число до которого включительно будем суммировать
sum_of_numbers= 0 # сумма чисел
for i in range(1, N + 1): 
    sum_of_numbers += i 
print("Сумма чисел равна", sum_of_numbers)


# 7. Удалены избыточные комментарии функции
import random
# функция которая находит в списке элемент, равный контрольному числу
def control_number (list_1, x):
    for i in range(len(list_1)):
        if list_1[i] == x:
            return i
        if i == len(list_1)-1:
            return -1
# создание списка и контрольного числа
list_1 = []
x = int(input("INPUT:"))     
for j in range(10):
    list_1.append(random.randint(1,50))
print (control_number (list_1, x))

import random
def control_number (list_1, x):
    for i in range(len(list_1)):
        if list_1[i] == x:
            return i
        if i == len(list_1)-1:
            return -1
list_1 = []
x = int(input("INPUT:"))
for j in range(10):
    list_1.append(random.randint(1,50))
print (control_number (list_1, x))


# 7. Удалены избыточные комментарии
# генерация списка с числами в диапазоне от 1 до 10
list_of_values = []
for q in range(15):
    random_number = random.randint(1, 10)
    list_of_values.append(random_number)
# генерация числа N
n = random.randint(1, 3)
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

list_of_values = []
for q in range(15):
    random_number = random.randint(1, 10)
    list_of_values.append(random_number)
n = random.randint(1, 3)
def number_of_repetitions(list_of_val, n_1):
    dictionary_of_numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0} 


# 4 Шум, переименованы переменные, удалены очевидные комментарии
def SumOfThe(N, data):
    summ = 0 # variable for the sum of all numbers except the next one
    for j in range(N):
        x = data.pop(0) # variable for the next item in the list    
        for j in range(len(data)):
            summ += data[j]
        if summ == x: # comparing the next item with the sum of the remaining items in the list
            return x
        else:
            summ = 0
            data.append(x)

def SumOfThe(N, data):
    sum_of_numbers_except_following = 0 
    for j in range(N):
        x = data.pop(0) # variable for the next item in the list    
        for j in range(len(data)):
            sum_of_numbers_except_following += data[j]
        if sum_of_numbers_except_following == x: 
            return x
        else:
            sum_of_numbers_except_following = 0
            data.append(x)


# 7. Удалены избыточные комментарии
import itertools 
def BiggerGreater(input):
    # рассчитываем значение исходного слова
    original_value = ''
    for i in range(len(input)):
        original_value += str(dictionary.get(input[i]))
    current_value = 999999999999999999999 # максимально большое значение
    final_word = '' # переменная для записи результата
    meaning = '' # переменная для очередного значения
    perm_set = itertools.permutations(input)
…

import itertools 
def BiggerGreater(input):
    # рассчитываем значение исходного слова
    original_value = ''
    for i in range(len(input)):
        original_value += str(dictionary.get(input[i]))
    current_value = 999999999999999999999 # максимально большое значение
    final_word = ''
    meaning = ''
    perm_set = itertools.permutations(input)
…


# 7. Удалены избыточные комментарии
def Football(F:list[int], N: int) -> bool:
    # обработка исключений
    summ_el: int = 0 
    for el in range(len(F) - 1):
        if F[el] < F[el+1]:
            summ_el += 1
    if summ_el == N - 1:
        return False
    # вариант 1: поменять местами два произвольных элемента массива
    for i in range(N):
        for j in range(N):
            F[i], F[j] = F[j], F[i] # меняем два очередных элемента местами
            # проверка того, что элементы массива расположены по возрастанию
            summ: int = 0 
            for k in range(len(F) - 1):
                if F[k] < F[k+1]:
                    summ += 1
            if summ == N - 1:
                return True
            F[i], F[j] = F[j], F[i] # возаращаем элементы массива к исходным

def Football(F:list[int], N: int) -> bool:
    # обработка исключений
    summ_el: int = 0 
    for el in range(len(F) - 1):
        if F[el] < F[el+1]:
            summ_el += 1
    if summ_el == N - 1:
        return False
    # вариант 1: поменять местами два произвольных элемента массива
    for i in range(N):
        for j in range(N):
            F[i], F[j] = F[j], F[i]
            # проверка того, что элементы массива расположены по возрастанию
            summ: int = 0 
            for k in range(len(F) - 1):
                if F[k] < F[k+1]:
                    summ += 1
            if summ == N - 1:
                return True
            F[i], F[j] = F[j], F[i]


# 4. Шум, переименованы переменные, удалены очевидные комментарии
def MadMax(N, Tele):
# sorting the array in ascending order
    Tele.sort()
    s = (len(Tele)//2) # middle
    Tele_start = Tele[0:s] # the first part of the list
    Tele_end = Tele[s: len(Tele)-1] # the second part of the list
    Tele_end.sort(reverse=True) # the second part of the list is in reverse order
    new_list = Tele_start + [max(Tele)] + Tele_end # "assembling" the final list
    # output of the resulting list
    return new_list

def MadMax(N, Tele):
# sorting the array in ascending order
    Tele.sort()
    middle = (len(Tele)//2)
    Tele_start = Tele[0: middle] # the first part of the list
    Tele_end = Tele[middle: len(Tele)-1] # the second part of the list
    Tele_end.sort(reverse=True) # the second part of the list is in reverse order
    new_list = Tele_start + [max(Tele)] + Tele_end # "assembling" the final list
    # output of the resulting list
    return new_list


# 4. Шум, переименованы переменные, удалены очевидные комментарии
def SherlockValidString(s):
    # создание словаря и подсчет элементов
    dictionary = {}
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 0
…
    # обработка исключений
    if len(dictionary) == 2:
        key_1 = dictionary[list(dictionary.keys())[0]] # первый элемент словаря
        key_2 = dictionary[list(dictionary.keys())[1]] # второй элемент словаря

def SherlockValidString(s):
    # создание словаря и подсчет элементов
    dictionary = {}
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 0
…
    # обработка исключений
    if len(dictionary) == 2:
        first_key= dictionary[list(dictionary.keys())[0]] 
        second_key= dictionary[list(dictionary.keys())[1]]


# 4. Шум, переименованы переменные, удалены очевидные комментарии
def MaximumDiscount(N, price):
    price.sort(reverse=True) # сортировка списка по убыванию
    # учитываем, что количество цен может быть меньше трех
    if N < 3:
        return 0
    samm = 0 # переменная для подсчета суммы максимальной скидки
    for i in range(2, N, 3): # цикл для суммирования каждого третьего числа
        samm += price[i]
    return samm

def MaximumDiscount(N, price):
    price.sort(reverse=True) # сортировка списка по убыванию
    # учитываем, что количество цен может быть меньше трех
    if N < 3:
        return 0
    sum_of_maximum_discount = 0 
    for i in range(2, N, 3): 
        sum_of_maximum_discount += price[i]
    return sum_of_maximum_discount


# 4. Шум, переименованы переменные, удалены очевидные комментарии
import re
def TankRush(H1, W1, S1, H2, W2, S2):
    List_S1 = S1.split() # разбиваем изначальную первую строку на строки массива
    List_S2 = S2.split() # разбиваем изначальную вторую строку на строки массива
    summ = 0 # переменная для подсчета количества совпадений
    count = 0 # переменная для подсчёта строк
    # проверка условия, что масив одномерный и в этом случае достаточно проверить входимость одной строки в другую
    if H2 == 1 and S2 in S1: 
        return True
    for i in range(len(List_S1) - 1):
        # обработка исключений
        L1 = List_S1[0]
        res = all(ele == L1[0] for ele in L1) 
        # если все символы строки одинаковые, то проходим по всей длине строки
        if res:        
            indexes = list(range(1, len(List_S1[i])))
            count += 1 
        # если исключений не найдено
        if not res:
            indexes = [match.start() for match in re.finditer((List_S2[0]), List_S1[i])] # находим все индексы вхождения в первую строчку массива 1
            count += 1 
        # проверка в соответствии со всеми найдеными индексами остальных (нижних) строк массива
        for j in indexes:
            n = count
            for k in range(1, H2):          
                srring = List_S1[n]
                if srring[j : j + W2] == List_S2[k]:
                    summ += 1
                if summ == H2 - 1:
                    return True
                n += 1
            summ = 0
    return False

import re
def TankRush(H1, W1, S1, H2, W2, S2):
    List_S1 = S1.split() # разбиваем изначальную первую строку на строки массива
    List_S2 = S2.split() # разбиваем изначальную вторую строку на строки массива
    number_of_matches = 0
    number_of_lines= 0 


# 7. Переименованы названия функций, удалены избыточные комментарии
# функция которая оставляет в списке только четные значения
def even(list_original: list, counter: int) -> list:
    if counter < 1: # условие выхода из рекурсии
        return None
    if list_original[counter - 1] % 2 == 0: # проверка на четность
        print(list_original[counter - 1])
    counter -= 1
    return even(list_original, counter)
# функция для получения исходных данных (списка)
def even_value(initial_list: list) -> list:
    return even(initial_list, len(initial_list))

def only_even_values_remain (list_original: list, counter: int) -> list:
    if counter < 1: # условие выхода из рекурсии
        return None
    if list_original[counter - 1] % 2 == 0: # проверка на четность
        print(list_original[counter - 1])
    counter -= 1
    return even(list_original, counter)
# функция для получения исходных данных (списка)
def getting_source_data (initial_list: list) -> list:
    return even(initial_list, len(initial_list))


# 7. Переименованы названия переменных, удалены избыточные комментарии
def army_communication_matrix(n: int, matrix) -> str:
    m = n - 1 # размер подматрицы
    result_sum = 0 # сумма числе подматрицы
    result = '' # строка для представления результата
    while m >= 2:
        for x in range(len(matrix[0]) - m + 1):
            for y in range(len(matrix) - m + 1):
                s_111 = []
                summ = 0
                for k in range(m):
                    s_1 = matrix[y + k]
                    s_11 = s_1[x : x + m]
                    s_111.append(s_11)
                    # вычисляем сумму подматрицы
                    summ_0 = sum(s_111[k])
                    summ += summ_0
                # проверка очередного значения суммы чисел подматрицы с текущим максимальным
                if summ > result_sum:
                    result_sum = summ
                    result = str(x) + ' ' + str(y) + ' ' + str(m)
        m -= 1
    return result

def army_communication_matrix(n: int, matrix) -> str:
    size_of_submatrix = n - 1
    sum_numbers_of_submatrix= 0
    resulting_string = ''

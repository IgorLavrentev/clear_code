def number_of_repetitions(list_of_val, n_1):
…
    final_list = [] # создание итогового (возвращаемого) списка 
    for e in range(1, len(dictionary_of_numbers) + 1): # добавление в итоговый список всех значений, превышающих N
        if dictionary_of_numbers.get(e) > n_1:
            final_list.append(e)
    return final_list
# инициализация переменной непосредственно перед циклом

def two_roster(way, extension, flag):
…
    # формирование списка с файлами заданного расширения
        files_list_end = [] # список файлов с заданным расширением
        file_extension = extension # расшириение искомых файлов
        for i in range (len(files_list)):
            name = files_list[i]
            if name[-(len(file_extension)):] == file_extension:
                files_list_end.append(name)
        # объединение списков файлов и каталогов
        final_list = [] # итоговый список
        final_list.append(files_list_end)
        final_list.append(directories_list)
        # вывод на экран игогового списка со списком файлов и каталогов
        print(final_list)
    else: pass
# инициализация переменных непосредственно перед циклом

n = 100 # размер массива
const = 100
# переименование переменной на приоритетное имя const

# функция получает на вход два типа (расширения) графических форматов
def form(extension_one, extension_two):
    files_list = []
    # поиск фйлов и подкаталогов в каталоге
    for root, dirs, files in os.walk('.'):
        files_list += files
    # формирование списка с файлами заданного расширения
    files_list_end = []
    for i in range (len(files_list)):
        name = files_list[i]
        if name[-(len(extension_one)):] == extension_one:
            files_list_end.append(name)
…
# инициализация переменной непосредственно перед циклом

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
    summ = -1
# присвоение переменной summ недопустимого значения после завершения работы с ней

def ShopOLAP(N, items):
…
    # удаление из писка временных элементов ' ' 
    if count != 0:
        del items[-count:]
    count = -1
…
# присвоение переменной count недопустимого значения после завершения работы с ней

import itertools 
def BiggerGreater(input):
    # работа с исключениями (если все буквы одинаковые)
    summ = 0
    for e in range(len(input)):
        if input[e] == input[0]:
            summ += 1
    if summ == len(input):
        return ''
    summ = -1
…
# присвоение переменной summ недопустимого значения после завершения работы с ней

def Football(F:list[int], N: int) -> bool:
    # обработка исключений
    summ_el: int = 0 
    for el in range(len(F) - 1):
        if F[el] < F[el+1]:
            summ_el += 1
    if summ_el == N - 1:
        return False
    summ_el = -1
…
# присвоение переменной sum_el недопустимого значения после завершения работы с ней

def SherlockValidString(s):
…
    # обработка исключений
    if len(dictionary) == 2:
        key_1 = dictionary[list(dictionary.keys())[0]] # первый элемент словаря
        key_2 = dictionary[list(dictionary.keys())[1]] # второй элемент словаря
    if len(dictionary) == 2 and int(key_1) == int(key_2):
        return True
    if len(dictionary) == 2 and int(key_1) == int(key_2) - 1:
        return True
    if len(dictionary) == 2 and int(key_1) - 1 == int(key_2):
        return True
key_1 = '***ERROR***'
key_2 = '***ERROR***'
…
# присвоение переменным key_1 и key_2 недопустимого значения после завершения работы с ними

def BigMinus(s1, s2):
…
    final_line = ''
    # меняем порядок элементов строки, так как цикл шёл с конца строки
    final_line = preliminary_line[::-1].lstrip("0")
    if final_line == '':
        final_line = '0'
    return final_line
# инициализация переменной непосредственно перед циклом

def MisterRobot(N, data):
…
    data_new = data.copy()
    data_new.sort()
    # проверка полученного списка со списком отсортированным встроенной функцией
    if data == data_new:
        return True
    return False
# инициализация переменной непосредственно перед циклом

def MassVote(N, Votes):
    # определяем каличество процентов для каждого кандидата (в виде списка)
    one_percent = 100/sum(Votes)
    list_percentages = [0]
    for i in range(N): 
        list_percentages.append(round(Votes[i] * one_percent, 3))
    # проверяем условие того, что максимальное число одно (выиграл только один кандидат)
    summ = 0
    flag = True
    for j in range(1, N + 1):
        if list_percentages[j] == max(list_percentages):
            summ += 1
    if summ > 1:
        flag = False
    summ = -1
…
# присвоение переменной summ недопустимого значения после завершения работы с ней

def SynchronizingTables(N, ids, salary):
    dictionary = {}
    salary.sort() # sorting the salary array
    # matching account numbers and salaries using a dictionary
    i = 0
    for j in range(min(ids), max(ids) + 1):
        if j in ids:
            dictionary[j] = salary[i]
            i += 1
    i = -1
    salary.clear() # deleting the contents of the salary array
    # filling in the salary list according to the accounting numbers
    for k in ids:
        salary.append(dictionary[k])
    return salary
# присвоение переменной i недопустимого значения после завершения работы с ней

import re
def TankRush(H1, W1, S1, H2, W2, S2):
…
    summ = 0 # переменная для подсчета количества совпадений
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
# инициализация переменной непосредственно перед циклом

def artificial_muscle_fibers(arr: list) -> int:
…
    # проверка двух ближайших значений
    # если значения совпадают впервые, то +1 к ответу
    quantity = 0
    for k in range(len(arr) - 1):
        if arr[k] == arr[k + 1] and flag is False:
            quantity += 1
            flag = True
        if arr[k] != arr[k + 1]:
            flag = False
    return quantity
# инициализация переменной непосредственно перед циклом

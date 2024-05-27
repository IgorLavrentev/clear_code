import os.path
from zipfile import ZipFile
# функция получает на вход два параметра: имя файла архива и расширение файла
def archive(name_a, file_e):
    archive_name = name_a # название архива
    file_extension = file_e # расширение файлов для поиска
    list_names = [] # список файлов с заданным расширением
…
    for i in range(len(list_names_all)):
        fi = list_names_all[i]
        if fi[-(len(file_extension)): ] == file_extension:
            list_names.append(fi)
    # извлечение файла из архива в текущий каталог
    for j in range(len(list_names)):
        with ZipFile(archive_name) as testzip:
            testzip.extract(list_names[j])
…

import os.path
from zipfile import ZipFile
# функция получает на вход два параметра: имя файла архива и расширение файла
def archive(name_a, file_e):
    archive_name = name_a # название архива
    list_names = [] # список файлов с заданным расширением
…
    file_extension = file_e # расширение файлов для поиска
    for i in range(len(list_names_all)):
        fi = list_names_all[i]
        if fi[-(len(file_extension)): ] == file_extension:
            list_names.append(fi)
    # извлечение файла из архива в текущий каталог
    for j in range(len(list_names)):
        with ZipFile(archive_name) as testzip:
            testzip.extract(list_names[j])
# группировка связанных команд


import os.path
def catalog_deletion(catalog):
    directories_list = [] # список каталогов
    files_list = [] # список файлов
    folder = catalog # каталог, который нужно удалить
    # Проверка: существует ли каталог
    existence = os.path.isdir(catalog)
    if existence != True:
        return print('Каталога не существует')
    # поиск фйлов и подкаталогов в каталоге
    for root, dirs, files in os.walk(folder):
        directories_list += dirs
        files_list += files
    if directories_list == []:

import os.path
def catalog_deletion(catalog):
    # Проверка: существует ли каталог
    existence = os.path.isdir(catalog)
    if existence != True:
        return print('Каталога не существует')
    directories_list = [] # список каталогов
    files_list = [] # список файлов
    folder = catalog # католог, который нужно удалить
    # поиск фйлов и подкаталогов в каталоге
    for root, dirs, files in os.walk(folder):
        directories_list += dirs
        files_list += files
    if directories_list == []:
…
# группировка связанных команд


# генерация списка с числами в диапазоне от 1 до 10
list_of_values = []
for q in range(15):
    random_number = random.randint(1, 10)
    list_of_values.append(random_number)
# генерация числа N
n = random.randint(1, 3)
def number_of_repetitions(list_of_val, n_1):
    dictionary_of_numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0} # создание словаря с ключами от 1 до 10
…

def creating_list_of_numbers():
    list_of_val = []
    for q in range(15):
        random_number = random.randint(1, 10)
        list_of_val.append(random_number)
    return list_of_val
list_of_values = creating_list_of_numbers()
# генерация числа N
n = random.randint(1, 3)
def number_of_repetitions(list_of_val, n_1):
    dictionary_of_numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0} # создание словаря с ключами от 1 до 10
…
# создание отдельной функции для связанных команд 


import os.path
# три параметра функции: путь к каталогу, расширение файла и булев флажок
def two_roster(way, extension, flag):
    if flag == True:
        final_list = [] # итоговый список
        directories_list = [] # список каталогов
        files_list = [] # список файлов
        files_list_end = [] # список файлов с заданным расширением
        file_extension = extension # расшириение искомых файлов
    # поиск фйлов и подкаталогов в каталоге
        for root, dirs, files in os.walk(way):
            directories_list += dirs
            files_list += files
    # формирование списка с файлами заданного расширения
        for i in range (len(files_list)):
            name = files_list[i]
            if name[-(len(file_extension)):] == file_extension:
                files_list_end.append(name)
        # объединение списков файлов и каталогов
        final_list.append(files_list_end)
        final_list.append(directories_list)
        # вывод на экран игогового списка со списком файлов и каталогов
        print(final_list)
    else: pass
path = 'test' # пример пути

import os.path
# три параметра функции: путь к каталогу, расширение файла и булев флажок
def two_roster(way, extension, flag):
    if flag == True:
        directories_list = [] # список каталогов
        files_list = [] # список файлов
    # поиск фйлов и подкаталогов в каталоге
        for root, dirs, files in os.walk(way):
            directories_list += dirs
            files_list += files
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
path = 'test' # пример пути
# группировка связанных команд


import random
# формируем массив
list_1 = []
for i in range(10):
    list_1.append(random.randint(1,50))
# функция сортировки массива
def Sorting_array(list1):
    for k in range(9):
        for j in range(9-k):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1
import random
def formation_of_array():
    array_of_numbers = []
    for i in range(10):
        array_of_numbers.append(random.randint(1,50))
    return array_of_numbers
list1 = formation_of_array()
# функция сортировки массива
def Sorting_array(list1):
    for k in range(9):
        for j in range(9-k):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1
# создание отдельной функции для связанных команд 


import os.path
from PIL import Image, ImageDraw, ImageColor, ImageFont
# функция получает на вход два типа (расширения) графических форматов
def form(extension_one, extension_two):
    files_list = []
    files_list_end = []
    # поиск фйлов и подкаталогов в каталоге
    for root, dirs, files in os.walk('.'):
        files_list += files
    # формирование списка с файлами заданного расширения
    for i in range (len(files_list)):
        name = files_list[i]
        if name[-(len(extension_one)):] == extension_one:
            files_list_end.append(name)
    # конвертация в другой формат
    for j in range(len(files_list_end)):
        im = Image.open(files_list_end[j])
        word = files_list_end[j]
        im.save(word[ :len(word) - len(extension_one)] + extension_two, extension_two)
        # рисование в центре изображения незаполненного квадрата, внутри которого написаны две строчки
        draw = ImageDraw.Draw(im)
        sz = im.size
        draw.rectangle([sz[0]/2 - 100,sz[1]/2 - 100, sz[0]/2 + 100,sz[1]/2 + 100])
        font = ImageFont.truetype("arial.ttf", 35)
        draw.text((sz[0]/2 - 40, sz[1]/2 - 40), 'Hello,\nWorld!', font=font, fill="blue")
        im.save(word[ :len(word) - len(extension_one)] + extension_two, extension_two)
        os.remove(files_list_end[j])

import os.path
from PIL import Image, ImageDraw, ImageColor, ImageFont
# функция получает на вход два типа (расширения) графических форматов
def form(extension_one, extension_two):
    files_list = []
    # поиск фйлов и подкаталогов в каталоге
    for root, dirs, files in os.walk('.'):
        files_list += files
    # формирование списка с файлами заданного расширения
    for i in range (len(files_list)):
        name = files_list[i]
        if name[-(len(extension_one)):] == extension_one:
            files_list_end.append(name)
    # конвертация в другой формат
    files_list_end = []
    for j in range(len(files_list_end)):
        im = Image.open(files_list_end[j])
        word = files_list_end[j]
        im.save(word[ :len(word) - len(extension_one)] + extension_two, extension_two)
        # рисование в центре изображения незаполненного квадрата, внутри которого написаны две строчки
        draw = ImageDraw.Draw(im)
        sz = im.size
        draw.rectangle([sz[0]/2 - 100,sz[1]/2 - 100, sz[0]/2 + 100,sz[1]/2 + 100])
        font = ImageFont.truetype("arial.ttf", 35)
        draw.text((sz[0]/2 - 40, sz[1]/2 - 40), 'Hello,\nWorld!', font=font, fill="blue")
        im.save(word[ :len(word) - len(extension_one)] + extension_two, extension_two)
        os.remove(files_list_end[j])
# группировка связанных команд


import random
class Dwarf:  # дварф
    def __init__(
        self, Dwarf_name, Dwarf_health_points, Dwarf_speed, Dwarf_weapon, Dwarf_workId
    ):
        self.name = Dwarf_name  # имя
        self._health_points = Dwarf_health_points  # очки здоровья
        self._speed = Dwarf_speed  # скорость
        self._weapon = Dwarf_weapon  # оружее
    def Run(self, new_speed):  # метод изменения скорости
        self._speed = new_speed
    def medicine_chest_plus(self, health_points_plus):  # метод аптечки
        self._health_points += health_points_plus
    def medicine_chest_minus(self, health_points_minus):  # метод урона
        self._health_points -= health_points_minus
    def change_weapons(self):  # смена оружия
        i = random.randint(0, 2)
        wep = ["меч", "лук", "булава"]
        self.weapon = wep[i]
class Weapon:  # оружие
    def __init__(self, Weapon_name, Weapon_cost, Weapon_damage, Weapon_weight):
        self.name = Weapon_name  # имя
        self.cost = Weapon_cost  # стоимость
        self.damage = Weapon_damage  # урон
        self.weight = Weapon_weight  # вес
class Animal:  # животное
    def __init__(
        self,
        Animal_name,
        Animal_health_points,
        Animal_weight,
        Animal_cost,
        Animal_hostility,
    ):
        self.name = Animal_name  # имя
        self._health_points = Animal_health_points  # очки здоровья
        self.weight = Animal_weight  # вес
        self.cost = Animal_cost  # стоимость
        self.hostility = (
            Animal_hostility  # враждебность, 0 - не враждебно, 1 - враждебно
        )
    def weight_loss(self, killogram_squared):  # метод потери веса
        self.weight -= pow(killogram_squared, 2)
    def cost_increase(self, increase):  # метод увеличения стоимости
        self.cost = self.cost * increase
    def become_hostile(self):  # метод превращения в враждебное животное
        self.hostility = 1
        self.cost -= 100
# изменение публичных полей класса на закрытые


def WordSearch(len, s,  subs):

    # вычисляем длину строки
    counter = 0
    for i in s:
        counter += 1
…

def WordSearch(len, s,  subs):
     # функция вычисления длинны строки
    def line_length(original_str):
        line_counter = 0
        for i in original_str:
            line_counter += 1
        return line_counter
    # вычисляем длину строки
    counter = line_length(s)
    
# создание отдельной функции для связанных команд 


def Keymaker(k: int) -> str:
    doors_array = [] # создание массива (первый шаг: открытие дверей)
    for i in range(k):
        doors_array.append(1)
    # второй шаг (закрытие каждой второй двери)
    for j in range(1, k, 2):
        doors_array[j] = 0
    # третий и последующие шаги
    for f in range(k - 2):
        for a in range(2 + f, k, 3 + f):
            if doors_array[a] == 0:
                doors_array[a] = 1
                continue
            if doors_array[a] == 1:
                doors_array[a] = 0
                continue
    # для ответа в виде строки
    string = ''
    for el in doors_array:
        string += str(el)
    return string
def Keymaker(k: int) -> str:
    # создание массива (первый шаг: открытие дверей)
    def creating_array_open_doors(number_of_doors):
        doors_array = []
        for i in range(number_of_doors):
            doors_array.append(1)
        return doors_array
    doors_array = creating_array_open_doors(k)
    # второй шаг (закрытие каждой второй двери)
    for j in range(1, k, 2):
        doors_array[j] = 0
    # третий и последующие шаги
    for f in range(k - 2):
        for a in range(2 + f, k, 3 + f):
            if doors_array[a] == 0:
                doors_array[a] = 1
                continue
            if doors_array[a] == 1:
                doors_array[a] = 0
                continue
    # для ответа в виде строки
    string = ''
    for el in doors_array:
        string += str(el)
    return string
# создание отдельной функции для связанных команд 


def SherlockValidString(s):
    # создание словаря и подсчет элементов
    dictionary = {}
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 0
    for k, v in dictionary.items(): 
        quantity = s.count(k)
        dictionary[k] = quantity
…

def SherlockValidString(s):
    # создание словаря и подсчет элементов
    dictionary = {}
    def counting_elements(s):
        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = 0
        return dictionary
    dictionary = counting_elements(s)
    for k, v in dictionary.items(): 
        quantity = s.count(k)
        dictionary[k] = quantity
…
# создание отдельной функции для связанных команд 


import math
def TheRabbitsFoot(s, encode):
    # зашифровка строки
    if encode == True:
        # подготовка к формированию матрицы
        s_1 = s.replace(' ', '')
        N = len(s_1)
        q = math.sqrt(N)
        max = round(q, 0)
        min = int(q)
        # проверка, что количество элементов достаточно
        if max * min < N:
            min += 1
        list_f = [] # список для разбиения строки
        # формирование матрицы
        while s_1 != '':
            s_parth = s_1[0 : min]
            list_f.append(s_parth)
            s_1 = s_1[min: ]
        list_fin = [] # итоговый список
        str_fin = '' # итоговая строка
        counter = 0 # счетчик для учета разной длины строк матрицы
        # зашифровка
        for i in range(min):
            for k in list_f:
                if counter == len(k):
                    del list_f[list_f.index(k)]
                    continue
                str_fin += k[i]
            counter += 1
            list_fin.append(str_fin)
            str_fin = ""
        # переводим список в строку
        string = ''
        for el in list_fin:
            string += el
            string += ' '
        return string.rstrip()
    # расшифровка строки
    if encode == False:
        counter = 0 # счетчик для учета разной длины слов 
        srt_f = '' # итоговая строка
        fruits_list = s.split(" ")
        for i in range(len(fruits_list[0])):
            for j in fruits_list:
                if len(j) < counter + 1:
                    continue
                srt_f += j[counter]
            counter += 1
        return srt_f

import math
def TheRabbitsFoot(s, encode):
    # зашифровка строки
    def string_encryption(s):
        # подготовка к формированию матрицы
        s_1 = s.replace(' ', '')
        N = len(s_1)
        q = math.sqrt(N)
        max = round(q, 0)
        min = int(q)
        # проверка, что количество элементов достаточно
        if max * min < N:
            min += 1
        list_f = [] # список для разбиения строки
        # формирование матрицы
        while s_1 != '':
            s_parth = s_1[0 : min]
            list_f.append(s_parth)
            s_1 = s_1[min: ]
        list_fin = [] # итоговый список
        str_fin = '' # итоговая строка
        counter = 0 # счетчик для учета разной длины строк матрицы
        # зашифровка
        for i in range(min):
            for k in list_f:
                if counter == len(k):
                    del list_f[list_f.index(k)]
                    continue
                str_fin += k[i]
            counter += 1
            list_fin.append(str_fin)
            str_fin = ""
        # переводим список в строку
        string = ''
        for el in list_fin:
            string += el
            string += ' '
        return string.rstrip()
    # расшифровка строки
    def decryption_string(s):
        counter = 0 # счетчик для учета разной длины слов 
        srt_f = '' # итоговая строка
        fruits_list = s.split(" ")
        for i in range(len(fruits_list[0])):
            for j in fruits_list:
                if len(j) < counter + 1:
                    continue
                srt_f += j[counter]
            counter += 1
        return srt_f
    if encode == True:
        return string_encryption(s)
    if encode == False: 
        return decryption_string(s)
# создание отдельной функции для связанных команд 

N = int(input()) # вводим число до которого включительно будем суммировать
sum = 0 # задаём переменную в которой будет накапливаться сумма
for i in range(1, N + 1): 
    sum += i 
print("Сумма чисел равна", sum)

sum = 0 # задаём переменную в которой будет накапливаться сумма
N = int(input()) # вводим число до которого включительно будем суммировать
for i in range(1, N + 1): 
    sum += i 
print("Сумма чисел равна", sum)
# группировка связанных команд


N = int(input()) # вводим число до которого включительно будем суммировать
sum = 0 # задаём переменную в которой будет накапливаться сумма
kv = 0 # задаём переменную в которой будет квадрат очередного числа
for i in range(1, N + 1): 
    kv = i * i
    sum += kv
    kv = 0
print ("Суммы квадратов чисел равны", sum)

sum = 0 # задаём переменную в которой будет накапливаться сумма
kv = 0 # задаём переменную в которой будет квадрат очередного числа
N = int(input()) # вводим число до которого включительно будем суммировать
for i in range(1, N + 1): 
    kv = i * i
    sum += kv
    kv = 0
print ("Суммы квадратов чисел равны", sum)
# группировка связанных команд


x = int(input())# вводим количество оценок
summ1 = 0 # переменная для подсчёта количества четвёрок
summ2 = 0 # переменная для подсчёта количества пятёрок
summ3 = 0 # переменная для подсчёта количества троек
summ4 = 0 # переменная для подсчёта количества двоек
for i in range(x):
    y = int(input())
    if y % 2 == 0:
        summ1 += 1
    elif y % 5 == 0:
        summ2 += 1
    elif y % 3 == 0:
        summ3 += 1
    elif y % 13 == 0:
        summ4 += 1
print("Количество четвёрок:", summ1, "Количество пятёрок:", summ2,"Количество троек:", summ3, "Количество двоек:", summ4)

summ1 = 0 # переменная для подсчёта количества четвёрок
summ2 = 0 # переменная для подсчёта количества пятёрок
summ3 = 0 # переменная для подсчёта количества троек
summ4 = 0 # переменная для подсчёта количества двоек
x = int(input())# вводим количество оценок
for i in range(x):
    y = int(input())
    if y % 2 == 0:
        summ1 += 1
    elif y % 5 == 0:
        summ2 += 1
    elif y % 3 == 0:
        summ3 += 1
    elif y % 13 == 0:
        summ4 += 1
print("Количество четвёрок:", summ1, "Количество пятёрок:", summ2,"Количество троек:", summ3, "Количество двоек:", summ4)
# группировка связанных команд


x = [] # создаём массив
summ = 0 # создаём переменную для подсчёта суммы
import random # подключаем модуль работы со случайными величинами
for i in range(100): # добавляем случайные значения в массив
    x.append(random.randint(1,50))
for i in range(100): # суммируем все значения в массиве
    summ += x[i]
print("Сумма: ", summ)
print("Среднее значение: ", summ / 100)

import random # подключаем модуль работы со случайными величинами
x = [] # создаём массив
summ = 0 # создаём переменную для подсчёта суммы
for i in range(100): # добавляем случайные значения в массив
    x.append(random.randint(1,50))
for i in range(100): # суммируем все значения в массиве
    summ += x[i]
print("Сумма: ", summ)
print("Среднее значение: ", summ / 100)
# группировка связанных команд

# 1. Информативный комментарий
N = int(input("Введите количество роутеров: "))
for i in range(1, N + 1):
    x = int(input()) # ввод кодов уязвимости роутера
    if x == 171: 
        print("Порядковый номер уязвимого роутера: ", i)
        break
    elif i == N:
        print("Уязвимостей не найдено")

N = int(input("Введите количество роутеров: "))
for i in range(1, N + 1):
    x = int(input()) # ввод кодов уязвимости роутера    if x == 171: # условие выхода из цикла, порядковый номер уязвимого роутера
        print("Порядковый номер уязвимого роутера: ", i)
        break
    elif i == N:
        print("Уязвимостей не найдено")


# 1. Информативный комментарий
number = int(input( )) #номер билета на трамвай
sum1 = 0
sum2 = 0
for i in range(3): # вычисляем сумму первых трёх цифр
    sum1 += number % 10
    number//= 10
for j in range(3): # вычисляем сумму последних трёх цифр
    sum2 += number % 10
    number//= 10
if sum1 == sum2: # сравниваем суммы
    print ("Счастливый билет")
else:
    print("Обычный билет")

number = int(input( )) #номер билета на трамвай
sum1 = 0 # переменная для накопления суммы первых трех чисел
sum2 = 0 # переменная для накопления суммы последних трех чисел
for i in range(3): # вычисляем сумму первых трёх цифр
    sum1 += number % 10
    number//= 10
for j in range(3): # вычисляем сумму последних трёх цифр
    sum2 += number % 10
    number//= 10
if sum1 == sum2: # сравниваем суммы
    print ("Счастливый билет")
else:
    print("Обычный билет")


# 1. Информативный комментарий
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

x = int(input())# вводим количество оценок
summ1 = 0 # переменная для подсчёта количества четвёрок
summ2 = 0 # переменная для подсчёта количества пятёрок
summ3 = 0 # переменная для подсчёта количества троек
summ4 = 0 # переменная для подсчёта количества двоек
for i in range(x): 
    y = int(input()) # вводим очередную оценку
    if y % 2 == 0:
        summ1 += 1
    elif y % 5 == 0:
        summ2 += 1
    elif y % 3 == 0:
        summ3 += 1
    elif y % 13 == 0:
        summ4 += 1
print("Количество четвёрок:", summ1, "Количество пятёрок:", summ2,"Количество троек:", summ3, "Количество двоек:", summ4)


# 1. Информативный комментарий
x = 1 # задаём переменную для вывода количества звёздочек на одной строке
for j in range(9): # задаём цикл для вывода очередной строки
    for i in range(x): # задаём цикл для вывода звёздочек
        print("*", end='')
    if j < 4:
        x += 1
    else:
        x -= 1
    print(" ")

# код для рисования узора
x = 1 # задаём переменную для вывода количества звёздочек на одной строке
for j in range(9): # задаём цикл для вывода очередной строки
    for i in range(x): # задаём цикл для вывода звёздочек
        print("*", end='')
    if j < 4:
        x += 1
    else:
        x -= 1
    print(" ")


# 1. Информативный комментарий
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

x = [] # создаём массив
summ = 0 # создаём переменную для подсчёта суммы
import random # подключаем модуль работы со случайными величинами
for i in range(100): 
    x.append(random.randint(1,50))
max = x[0] # предварительное максимальное значение
min = x[0] # предварительное максимальное значение
for i in range(100): 
    if max < x[i]:
        max = x[i]
    if min > x[i]:
        min = x[i]
print("Максимальное значение: ", max)
print("Минимальное значение: ", min)


# 1. Информативный комментарий
import random
list100 = [] # формируем массив
n = 100 # размер массива
for i in range(n):
    list100.append(random.randint(1,50))
for j in range(n//2):
    x = list100[99-j]
    list100[99-j] = list100[j]
    list100[j] = x

import random
list100 = [] # формируем массив
n = 100 # размер массива
for i in range(n):
    list100.append(random.randint(1,50))
for j in range(n//2):
# перестановка местами первого и последнего элемента списка
    x = list100[99-j]
    list100[99-j] = list100[j]
    list100[j] = x


# 1. Информативный комментарий
import os.path
from zipfile import ZipFile
# функция получает на вход два параметра: имя файла архива и расширение файла
def archive(name_a, file_e):
    archive_name = name_a # название архива
    file_extension = file_e # расширение файлов для поиска
    list_names = [] # список файлов с заданным расширением
    # проверка, корректен ли архив
    with ZipFile(archive_name) as testzip:
        if testzip.testzip() != None:
            return print('Архив не корректен')
    # сканирование текущего каталога в поисках файлов с заданным расширением
    with ZipFile(archive_name) as testzip:
        list_names_all = testzip.namelist()
    for i in range(len(list_names_all)):
        fi = list_names_all[i]
        if fi[-(len(file_extension)): ] == file_extension:
            list_names.append(fi)
    # извлечение файла из архива в текущий каталог
    for j in range(len(list_names)):
        with ZipFile(archive_name) as testzip:
            testzip.extract(list_names[j])
    # создание нового архива
    ZipFile("new_test.zip", "w")
    # добавление в архив файлов с заданным расширением
    for k in range(len(list_names)):
        with ZipFile('new_test.zip', 'a') as testzip:
            testzip.write(list_names[k])
    # удаление файлов и каталогов с заданным расширением из текущей директории 
    for d in range(len(list_names)):
        if list_names[d].find('/') != -1:
            way_and_name = list_names[d]
            os.remove(way_and_name[:list_names[d].find('/')] + '/' + way_and_name[list_names[d].find('/') + 1:])
            os.rmdir(way_and_name[:list_names[d].find('/')])
        else:
            os.remove(list_names[d])
    print(f'Создание нового архива с файлами "{file_extension}" завершено!')

    # создание нового архива с названием "new_test.zip", возможно дать другое название
    ZipFile("new_test.zip", "w")


# 4. Предупреждения о последствиях
import random
class Dwarf:  # дварф
    def __init__(
        self, Dwarf_name, Dwarf_health_points, Dwarf_speed, Dwarf_weapon, Dwarf_workId
    ):
        self.name = Dwarf_name  # имя
        self.health_points = Dwarf_health_points  # очки здоровья
        self.speed = Dwarf_speed  # скорость
        self.weapon = Dwarf_weapon  # оружее
    def Run(self, new_speed):  # метод изменения скорости
        self.speed = new_speed
    def medicine_chest_plus(self, health_points_plus):  # метод аптечки
        self.health_points += health_points_plus
    def medicine_chest_minus(self, health_points_minus):  # метод урона
        self.health_points -= health_points_minus
    def change_weapons(self):  # смена оружия
        i = random.randint(0, 2)
        wep = ["меч", "лук", "булава"]
        self.weapon = wep[i]

    def change_weapons(self):  # смена оружия (выполняется случайным образом)
        i = random.randint(0, 2)
        wep = ["меч", "лук", "булава"]
        self.weapon = wep[i]


# 5. Усиление
import random 
class transport: # класс транспрта
    def __init__(self, transport_length, transport_width, transport_height, transport_weight):
        self._length = transport_length # длина транспортного средства
        self._width = transport_width # ширина транспортного средства
        self._height = transport_height # высота транспортного средства
        self._weight = transport_weight # масса транспортного средства
    def engine(self): # двигатель
        print('JT8D')
    def pr(self, __car_speed): # метод для ad hoc полиморфизма
        print(__car_speed)
    def pr(self, __roll_angle): # метод для ad hoc полиморфизма
        print(__roll_angle)
class rims(): # класс автомобильных дисков
    def __init__(self, r):
        self.radius = r
class car(transport): # класс автомобилей
    def __init__(self, transport_length, transport_width, transport_height, transport_weight, eng_type, s, r):
        super().__init__(transport_length, transport_width, transport_height, transport_weight)
        self.__engine_type = eng_type # 1 -ДВС, 2 - электродвигатель
        self.__car_speed = s # скорость автомобиля
        self.__stopping_distance_coefficient = 0 # коэффициент тормозного пути
        self.__car_rims = rims(r) # диски автомобиля
        self.__car_boost = 'yes' # возможно ли ускорение ('yes' или 'no')
    def engine(self): # двигатель
        print(self.__engine_type)
    def get_car_rims(self): # метод вывода на печать радиуса диска
        print(self.__car_rims.radius)
    def speed(self, __new_speed): # скорость
        self.__car_speed = __new_speed
    def get_car_speed(self): # метод вывода на печать скорости автомобиля
        print(self.__car_speed)
    def driving_style(self,__car_speed):  # стиль вождения
        if 1 < __car_speed < 40:
            return 'Стиль вождения дачный'
        elif 40 <= __car_speed < 90:
            return 'Стиль вождения профессиональный'
        elif 90 <= __car_speed:
            return 'Стиль вождения агрессивный'
    def ABS(self, a): # включение антиблокировочной системы, 1 - система включена, 0 - система выключена
        if a == 1:
            self.__stopping_distance_coefficient = 0.7
        elif a == 0:
            self.__stopping_distance_coefficient = 1

    def driving_style(self,__car_speed):  # стиль вождения, зависит от скорости
        if 1 < __car_speed < 40:
            return 'Стиль вождения дачный'
        elif 40 <= __car_speed < 90:
            return 'Стиль вождения профессиональный'
        elif 90 <= __car_speed:
            return 'Стиль вождения агрессивный'


# 1. Информативный комментарий
def PrintingCosts(Line):
    # создание словаря
    dictionary = {} 
    dictionary[' '] = 0; dictionary['!'] = 9; dictionary['"'] = 6; dictionary['#'] = 24; dictionary['$'] = 29; dictionary['%'] = 22; 
    dictionary['&'] = 24; dictionary['\''] = 3; dictionary['('] = 12; dictionary[')'] = 12; dictionary['*'] = 17; dictionary['+'] = 13; 
    dictionary[','] = 7; dictionary['-'] = 7; dictionary['.'] = 4; dictionary['/'] = 10; dictionary['0'] = 22; dictionary['1'] = 19; 
    dictionary['2'] = 22; dictionary['3'] = 23; dictionary['4'] = 21; dictionary['5'] = 27; dictionary['6'] = 26; dictionary['7'] = 16; 
    dictionary['8'] = 23; dictionary['9'] = 26; dictionary[':'] = 8; dictionary[';'] = 11; dictionary['<'] = 10; dictionary['='] = 14; 
    dictionary['>'] = 10; dictionary['?'] = 15; dictionary['@'] = 32; dictionary['A'] = 24; dictionary['B'] = 29; dictionary['C'] = 20; 
    dictionary['D'] = 26; dictionary['E'] = 26; dictionary['F'] = 20; dictionary['G'] = 25; dictionary['H'] = 25; dictionary['I'] = 18; 
    dictionary['J'] = 18; dictionary['K'] = 21; dictionary['L'] = 16; dictionary['M'] = 28; dictionary['N'] = 25; dictionary['O'] = 18;  
    dictionary['P'] = 23; dictionary['Q'] = 31; dictionary['R'] = 28; dictionary['S'] = 25; dictionary['T'] = 16; dictionary['U'] = 23; 
    dictionary['V'] = 19; dictionary['W'] = 26; dictionary['X'] = 18; dictionary['Y'] = 14; dictionary['Z'] = 22; dictionary['['] = 18; 
    dictionary['\\'] = 10; dictionary[']'] = 18; dictionary['^'] = 7; dictionary['_'] = 8; dictionary['`'] = 3; dictionary['a'] = 23; 
    dictionary['b'] = 25; dictionary['c'] = 17; dictionary['d'] = 25; dictionary['e'] = 23; dictionary['f'] = 18; dictionary['g'] = 30; 
    dictionary['h'] = 21; dictionary['i'] = 15; dictionary['j'] = 20; dictionary['k'] = 21; dictionary['l'] = 16; dictionary['m'] = 22; 
    dictionary['n'] = 18; dictionary['o'] = 20; dictionary['p'] = 25; dictionary['q'] = 25; dictionary['r'] = 13; dictionary['s'] = 21; 
    dictionary['t'] = 17; dictionary['u'] = 17; dictionary['v'] = 13; dictionary['w'] = 25; dictionary['x'] = 13; dictionary['y'] = 24; 
    dictionary['z'] = 19; dictionary['{'] = 17; dictionary['|'] = 12; dictionary['}'] = 18; dictionary['~'] = 9; 
    counter = len(dictionary) 
    summ = 0 # переменная для суммы расхода тонера
    for i in range(len(Line)):
        for key in dictionary:
            if Line[i] == key:
                summ += dictionary.get(key)
                counter -= 1
        if counter == len(dictionary): # условия для добавления количества тонера для значений вне заданной таблицы
            summ += 23
        counter = len(dictionary)
    return summ

def PrintingCosts(Line):
    # создание словаря раскладки символов ASCII и соответствующего им объёма тонера
    dictionary = {} 
    dictionary[' '] = 0; dictionary['!'] = 9; dictionary['"'] = 6; dictionary['#'] = 24; dictionary['$'] = 29; dictionary['%'] = 22; 
    dictionary['&'] = 24; dictionary['\''] = 3; dictionary['('] = 12; dictionary[')'] = 12; dictionary['*'] = 17; dictionary['+'] = 13; 
    dictionary[','] = 7; dictionary['-'] = 7; dictionary['.'] = 4; dictionary['/'] = 10; dictionary['0'] = 22; dictionary['1'] = 19; 
    dictionary['2'] = 22; dictionary['3'] = 23; dictionary['4'] = 21; dictionary['5'] = 27; dictionary['6'] = 26; dictionary['7'] = 16; 
    dictionary['8'] = 23; dictionary['9'] = 26; dictionary[':'] = 8; dictionary[';'] = 11; dictionary['<'] = 10; dictionary['='] = 14; 
    dictionary['>'] = 10; dictionary['?'] = 15; dictionary['@'] = 32; dictionary['A'] = 24; dictionary['B'] = 29; dictionary['C'] = 20; 
    dictionary['D'] = 26; dictionary['E'] = 26; dictionary['F'] = 20; dictionary['G'] = 25; dictionary['H'] = 25; dictionary['I'] = 18; 
    dictionary['J'] = 18; dictionary['K'] = 21; dictionary['L'] = 16; dictionary['M'] = 28; dictionary['N'] = 25; dictionary['O'] = 18;  
    dictionary['P'] = 23; dictionary['Q'] = 31; dictionary['R'] = 28; dictionary['S'] = 25; dictionary['T'] = 16; dictionary['U'] = 23; 
    dictionary['V'] = 19; dictionary['W'] = 26; dictionary['X'] = 18; dictionary['Y'] = 14; dictionary['Z'] = 22; dictionary['['] = 18; 
    dictionary['\\'] = 10; dictionary[']'] = 18; dictionary['^'] = 7; dictionary['_'] = 8; dictionary['`'] = 3; dictionary['a'] = 23; 
    dictionary['b'] = 25; dictionary['c'] = 17; dictionary['d'] = 25; dictionary['e'] = 23; dictionary['f'] = 18; dictionary['g'] = 30; 
    dictionary['h'] = 21; dictionary['i'] = 15; dictionary['j'] = 20; dictionary['k'] = 21; dictionary['l'] = 16; dictionary['m'] = 22; 
    dictionary['n'] = 18; dictionary['o'] = 20; dictionary['p'] = 25; dictionary['q'] = 25; dictionary['r'] = 13; dictionary['s'] = 21; 
    dictionary['t'] = 17; dictionary['u'] = 17; dictionary['v'] = 13; dictionary['w'] = 25; dictionary['x'] = 13; dictionary['y'] = 24; 
    dictionary['z'] = 19; dictionary['{'] = 17; dictionary['|'] = 12; dictionary['}'] = 18; dictionary['~'] = 9; 


# 4. Предупреждение о последствиях
def artificial_muscle_fibers(arr: list) -> int:
    flag = False
    quantity = 0
    # сортировка списка по убыванию
    for i in range(len(arr)): # i проходит от 0 до длины списка
        counter = i + 1  # при каждом проходе задается новое значение counter
        for j in range(counter, len(arr)): # counter проходит от i + 1 до длины списка
            # сравнение i-го элемента с индексом элемента 'counter'
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        counter += 1
    # проверка двух ближайших значений
    # если значения совпадают впервые, то +1 к ответу
    for k in range(len(arr) - 1):
        if arr[k] == arr[k + 1] and flag is False:
            quantity += 1
            flag = True
        if arr[k] != arr[k + 1]:
            flag = False
    return quantity

def artificial_muscle_fibers(arr: list) -> int:
    flag = False
    quantity = 0
    # сортировка списка по убыванию (обязательное условие выполнения задачи)
    for i in range(len(arr)): # i проходит от 0 до длины списка
        counter = i + 1  # при каждом проходе задается новое значение counter
        for j in range(counter, len(arr)): # counter проходит от i + 1 до длины списка


# 5. Усиление
import ctypes
class DynArray:
    def __init__(self):
        self.count = 0  # текущее количество элементов в массиве
        self.capacity = 16  # текущая ёмкость буфера
        self.array = self.make_array(
            self.capacity
        )  # указатель на блок памяти нужной ёмкости, хранящий элементы PyObject
    def __len__(self):
        return self.count
    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]
    # увеличение емкости буфера и перезапись массива в новый массив
    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    def append(self, itm):
        # сравнивание текущего количества элементов в массиве и текущей емкости буфера
        if self.count == self.capacity:
            self.resize(2 * self.capacity) # увеличение текущей ёмкости буфера в 2 раза
        self.array[self.count] = itm # добавление элемента в массив
        self.count += 1 # увеличение текущего количества элементов в массиве на +1

    def append(self, itm):
        # сравнивание текущего количества элементов в массиве и текущей емкости буфера
        if self.count == self.capacity:
            self.resize(2 * self.capacity) # увеличение текущей ёмкости буфера в 2 раза (при необходимости возможно увеличить)
        self.array[self.count] = itm # добавление элемента в массив
        self.count += 1 # увеличение текущего количества элементов в массиве на +1

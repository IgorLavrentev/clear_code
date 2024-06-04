# Задание 3.1


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


sum1 = 0 # первые три цифры числа
sum2 = 0 # последние три цифры числа


X = int(input()) # объём горшочка
Y = int(input()) # выедаемые горсти
k = 0
n = 1 # переменная для подсчёта количества дней
while X > Y:
    k = k + X – Y 
    Y += Y # количество съеденного меда Винни-Пухом
    n += 1
print("Всего горстей мёда Винни-Пух накопил в бочке:", X + k)
print("Ушло дней на накопление мёда:", n)

k = 0 # количество меда в бочке


import itertools 
def BiggerGreater(input):
    # работа с исключениями (если все буквы одинаковые)
    summ = 0
    for e in range(len(input)):
        if input[e] == input[0]:
            summ += 1
    if summ == len(input):
        return ''
    # словарь русских букв
    dictionary_ru = {'а' : '01', 'б' : '02', 'в' : '03', 'г' : '04', 'д' : '05', 'е' : '06', 'ё' : '07', 'ж' : '08', 'з' : '09', 'и' : '10', 'й' : '11', 'к' : '12', 
                     'л' : '13', 'м' : '14', 'н' : '15', 'о' : '16', 'п' : '17', 'р' : '18', 'с' : '19', 'т' : '20', 'у' : '21', 'ф' : '22', 'х' : '23', 'ц' : '24',
                     'ч' : '25', 'ш' : '26', 'щ' : '27', 'ъ' : '28', 'ы' : '29', 'ь' : '30', 'э' : '31', 'ю' : '32', 'я' : '33'}
    # словарь английских букв
    dictionary_eng = {'a' : '01', 'b' : '02', 'c' : '03', 'd' : '04', 'e' : '05', 'f' : '06', 'g' : '07', 'h' : '08', 'i' : '09', 'j' : '10', 'k' : '11', 'l' : '12', 
                      'm' : '13', 'n' : '14', 'o' : '15', 'p' : '16', 'q' : '17', 'r' : '18', 's' : '19', 't' : '20', 'u' : '21', 'v' : '22', 'w' : '23', 'x' : '24', 
                      'y' : '25', 'z' : '26'}
    # выбираем словарь
    if input[0] in dictionary_ru:
        dictionary = dictionary_ru
    if input[0] in dictionary_eng:
        dictionary = dictionary_eng
    # рассчитываем значение исходного слова
    original_value = ''
    for i in range(len(input)):
        original_value += str(dictionary.get(input[i]))
    current_value = 999999999999999999999 # максимально большое значение
    final_word = '' # переменная для записи результата
    meaning = '' # переменная для очередного значения
    perm_set = itertools.permutations(input) 
    # присваиваем переменной порядковое значение в соответствии со словарем
    for val in perm_set:
        for j in range(len(val)):
            meaning += str(dictionary.get(val[j])) 
        if  current_value > int(meaning) > int(original_value): # сравниваем с иходным словом
            current_value = int(meaning)
            final_word = val
        meaning = ''
    # если перестановками не получилось получить искомое слово в соответствии с условими
    if final_word == input:
        return ''
    # вывод результата
    string = ''.join(final_word)
    return string

    perm_set = itertools.permutations(input) # возвращает итератор с последовательными перестановками из элементов входной последовательности


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

    # третий и последующие шаги переключения дверей, на n-м производится переключение каждой n-й двери
    for f in range(k - 2):
        for a in range(2 + f, k, 3 + f):
            if doors_array[a] == 0:
                doors_array[a] = 1
                continue
            if doors_array[a] == 1:
                doors_array[a] = 0
                continue


def odometer(oksana):
    distance = 0
    distance += oksana[0] * oksana[1]
    if len(oksana) > 2:
        for i in range(2, len(oksana) - 1, 2):
            previous = oksana[i - 1]
            distance += oksana[i] * (oksana[i + 1] - previous)
    return distance

    distance = 0 # общая протяженность поездки


def BigMinus(s1, s2):
    if int(s1) < int(s2): # меняем местами исходные данные если первое число меньше второго
        s1, s2 = s2, s1
    # ставим нули перед меньшей строкой
    s_temporary = s2[::-1]
    for k in range(len(s1) - len(s2)):
        s_temporary += '0'
    s2 = s_temporary[::-1]
    preliminary_line = ''
    final_line = ''
    flag = False
    # цикл по всей длине большей строки
    for i in range(len(s1) - 1, -1, -1):
        if int(s2[i]) <= int(s1[i]) and flag == False: 
            preliminary_line += str(int(s1[i]) - int(s2[i]))
        elif (int(s2[i]) > int(s1[i])) and (int(s1[i - 1]) == 0) and (flag == False):
            preliminary_line += str(10 + int(s1[i]) - int(s2[i]))
            s1 = s1[: i-1] + "9" + s1[i:]
            flag = True
        # учет флагов
        elif flag == True and (int(s1[i - 1]) == 0):
            preliminary_line += str(9 - int(s2[i]))
            s1 = s1[: i-1] + "9" + s1[i:]
            flag == True
        elif flag == True and (int(s1[i - 1]) != 0):
            preliminary_line += str(9 - int(s2[i]))
            s1 = s1[: i-1] + str(int(s1[i-1])-1) + s1[i:] 
            flag = False
        else:
            preliminary_line += str(10 + int(s1[i]) - int(s2[i]))
            s1 = s1[: i-1] + str(int(s1[i-1])-1) + s1[i:]
    # меняем порядок элементов строки, так как цикл шёл с конца строки
    final_line = preliminary_line[::-1].lstrip("0")
    if final_line == '':
        final_line = '0'
    return final_line

    preliminary_line = '' #строка получаемая после вычета одного числа из другого (формируется в обратном порядке)


# функция сортировки списка
def sorting_list(trc_1, Lo, Mid, Hi) -> list:
    if Mid > Hi: # условие окончания рекурсии
        return trc_1
    if trc_1[Mid] == 2:
        trc_1[Mid], trc_1[Hi] = trc_1[Hi], trc_1[Mid]
        Hi -= 1
    if trc_1[Mid] == 1:
        Mid += 1
    if trc_1[Mid] == 0:
        trc_1[Mid], trc_1[Lo + 1] = trc_1[Lo + 1], trc_1[Mid]
        Lo += 1
        Mid += 1
    return sorting_list(trc_1, Lo, Mid, Hi)
# функция для получения исходных данных (строки)
def TRC_sort(trc: list) -> list:
    # работа с исключениями
    if trc == [0,1] or trc == [1]:
        return trc
    l_initial  = -1
    m_initial  = 0
    h_initial  = len(trc) - 1
    return sorting_list(trc, l_initial, m_initial, h_initial)
# функция сортировки списка
def sorting_list(trc_1, Lo, Mid, Hi) -> list:
    if Mid > Hi: # условие окончания рекурсии
        return trc_1
    if trc_1[Mid] == 2:
        trc_1[Mid], trc_1[Hi] = trc_1[Hi], trc_1[Mid]
        Hi -= 1
    if trc_1[Mid] == 1:
        Mid += 1
    if trc_1[Mid] == 0:
        trc_1[Mid], trc_1[Lo + 1] = trc_1[Lo + 1], trc_1[Mid]
        Lo += 1
        Mid += 1
    return sorting_list(trc_1, Lo, Mid, Hi)

    l_initial  = -1 # индекс крайнего правого 0 в начале массива
    m_initial = 0 # индекс крайнего правого 1 	в начале массива
    h_initial  = len(trc) – 1 # индекс крайнего левого 2 в хвосте


# Задание 3.2


zp1 = int(input()) # зарплата джуна
zp2 = int(input()) # зарплата миддла
zp3 = int(input()) # зарплата сеньора
if zp1 > zp2 and zp1 > zp3 and zp2 < zp3:
    print ("Самая высокая зарплата у джуна, различие в" , zp1/zp2 , "раз")
if zp1 > zp2 and zp1 > zp3 and zp3 < zp2:
    print ("Самая высокая зарплата у джуна, различие в", zp1/zp3 , "раз")

if zp2 > zp1 and zp2 > zp3 and zp1 < zp3:
    print ("Самая высокая зарплата у миддла, различие в", zp2/zp1 , "раз")
if zp2 > zp1 and zp2 > zp3 and zp3 < zp1:
    print ("Самая высокая зарплата у миддла, различие в", zp2/zp3 , "раз")

if zp3 > zp1 and zp3 > zp2 and zp2 < zp1:
    print ("Самая высокая зарплата у сеньора, различие в", zp3/zp2 , "раз")
if zp3 > zp1 and zp3 > zp2 and zp1 < zp2:
    print ("Самая высокая зарплата у сеньора, различие в", zp3/zp1 , "раз")

juniors_salary = int(input())
middles_salary = int(input())
senors_salary = int(input())
if juniors_salary > middles_salary and juniors_salary > senors_salary and middles_salary < senors_salary:
    print ("Самая высокая зарплата у джуна, различие в" , juniors_salary/middles_salary , "раз")
if juniors_salary > middles_salary and juniors_salary > senors_salary and senors_salary < middles_salary:
    print ("Самая высокая зарплата у джуна, различие в", juniors_salary/senors_salary , "раз")

if middles_salary > juniors_salary and middles_salary > senors_salary and juniors_salary < senors_salary:
    print ("Самая высокая зарплата у миддла, различие в", middles_salary/juniors_salary , "раз")
if middles_salary > juniors_salary and middles_salary > senors_salary and senors_salary < juniors_salary:
    print ("Самая высокая зарплата у миддла, различие в", middles_salary/senors_salary , "раз")

if senors_salary > juniors_salary and senors_salary > middles_salary and middles_salary < juniors_salary:
    print ("Самая высокая зарплата у сеньора, различие в", senors_salary/middles_salary , "раз")
if senors_salary > juniors_salary and senors_salary > middles_salary and juniors_salary < middles_salary:
    print ("Самая высокая зарплата у сеньора, различие в", senors_salary/juniors_salary , "раз")


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

number_one = float(input())
number_two = float(input())
# преобразовываем введённые числа
number_one = int(number_one * 1000)
number_two = int(number_two * 1000)
# сравниваем преобразованные числа
if number_one == number_two:
    print("Числа совпадают до третьего знака после запятой")
else
    print("Числа не совпадают до третьего знака после запятой")


x = int(input()) # вводим год рождения
if x % 100 == 0 and x % 400 != 0 or x % 4 != 0:
    print(x, "- не високосный год")
else: 
    print(x, "- високосный год")

year_of_birth = int(input())
if year_of_birth % 100 == 0 and year_of_birth % 400 != 0 or year_of_birth % 4 != 0:
    print(year_of_birth, "- не високосный год")
else: 
    print(year_of_birth, "- високосный год")


age = int(input()) # вводим возраст пёсика
if age <= 2:
    print(age * 10.5)
else:
    print(21 + (age-2) * 4)

doggies_age= int(input())
if doggies_age <= 2:
    print(doggies_age * 10.5)
else:
    print(21 + (doggies_age -2) * 4)


hour = int(input("Назначенное время свидания:"))
summ = 0
for i in range(2, hour):
    if hour % i == 0:
        summ += i
if summ % 2 == 0:
    print("Любит")
else:
    print("Не любит")

appointed_date_time = int(input("Назначенное время свидания:"))
summ = 0
for i in range(2, appointed_date_time):
    if appointed_date_time% i == 0:
        summ += i
if summ % 2 == 0:
    print("Любит")
else:
    print("Не любит")

7.1. Приведите пять примеров правильного именования булевых переменных
flag – is_ more
# если занимаем десяток у следующего значения
flag – is_command_undo
# если текущая команда была Undo
flag – is_ point
# если в строке есть точка
flag– is_equality
# если значения равны
flag– is_even_number
# если числа четные

7.2. Подходящие случаи, когда можно использовать типичные имена булевых переменных
flag – success
# показатель, что максимальное число найдено не одно
flag - found
# если значения совпадают True, если не совпадают False

7.3. Случаи, когда вместо i j k нагляднее использовать более выразительное имя
for step in range(repeat):
# шаги (повторения) поворотов матрицы
i – door, j – door, f – door, a – door
# проход по каждой двери
for k, v in dictionary.items():
k, v - key, value
# ключ и значение в словаре
for p in range(0, len(battalion), 2):
p - polygons
# полигоны плацдарма
j - stop_point
# точка остановки на светофоре

7.4. Случаи, когда можно использовать пары имён - антонимы
Tele_start
Tele_end
# начальная и конечная часть массива
l_initial, m_initial, h_initial - left _initial, middle_initial, right_initial
# исходные данные для создания массива

7.5. Присвоение временным переменным выразительных имен (возможно полностью избавиться)
# Было
string = ''.join(final_word)
return string
# Стало
return ''.join(final_word)
# Было
ind = i.find(subs)
ind_last = ind + subs_counter - 1
# Стало
ind_last = i.find(subs)+ subs_counter - 1
# Было
maxx = max(a[j:k+1])
B.append(maxx)
# Стало
B.append(max(a[j:k+1]))
# Переименовать new_list - resulting_list
# Избавиться от переменной
# Было
new_list = Tele_start + [max(Tele)] + Tele_end 
return new_list
# Стало
return Tele_start + [max(Tele)] + Tele_end

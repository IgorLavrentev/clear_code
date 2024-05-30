r = int(input("Радиус окружности: "))
PI = 3.14
print("Периметр окружности:", 2 * PI * r)
# значение 3,14 связывается с переменной PI во время написания кода, 
# в данном случае такой выбор сделан по причине того, что значение математической константы «пи»
# постоянно и не повлечет за собой необходимости менять это значение по тексту программы

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
        self._engine_type = eng_type # 1 -ДВС, 2 - электродвигатель
        self._car_speed = s # скорость автомобиля
        self._stopping_distance_coefficient = 0 # коэффициент тормозного пути
        self._car_rims = rims(r) # диски автомобиля
        self._car_boost = 'yes' # возможно ли ускорение ('yes' или 'no')
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
My_car = car(1400, 200, 300, 5, 2, 30, 15)
Another_car= car(1300, 1500, 200, 5, 2, 40, 15)
ALLOWED_SPEED = 90  # разрешенная скорость
My_car._car_speed = ALLOWED_SPEED
Another_car._car_speed = ALLOWED_SPEED
# значение 90 связывается с переменной во время компиляции кода, такой выбор сделан для того,
# чтобы любому создаваемому объекту класса можно было присвоить максимальную разрешенную
# скорость при езде по трассе

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
My_Dwarf = Dwarf()
My_Dwarf.wep = read_title_weapon() # оружие полученное из другого файла
# значение, например, «меч» связывается с переменной во время выполнения программы,
# такой выбор сделан для того, чтобы отдельно хранить и модернизировать (обновлять и изменять)
# класс оружия в отдельном файле и обращаться к нему в случае необходимости


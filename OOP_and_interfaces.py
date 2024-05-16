# программа 1
class Dwarf:  # класс Дварфов
    name = "Простак"  # имя
    age = 35  # возраст
    height = 152  # рост
    speed = 8  # скорость
    weapon = 1  # оружее
    language = "eng"  # язык
    trained_animal = "Alpaca"  # тренируемое животное

class weapon:  # класс оружия
    name = "Baton"  # имя
    cost = 100  # стоимость
    damage = 7  # урон
    weight = 10  # вес

class armour:  # класс доспехов
    name = "armor"  # имя
    cost = 50  # стоимость
    damage = 0  # урон
    weight = 20  # вес

class animals:  # класс животных
    name = "Alpaca"  # имя
    weight = 10  # вес
    cost = 900  # стоимость
    hostility = "no"  # враждебность

class factory_creation_living_beings: # фабрика для создания живых существ
    def create_beings(beings_tupe):
        if beings_tupe == 'Dwarf': # если нужно создать Дварфа
            return Dwarf()
        if beings_tupe == 'animals': # если нужно создать животное
            return animals()

class factory_creation_armor_or_weapons: # фабрика для создания оружия или доспехов
    def create_beings(beings_tupe):
        if beings_tupe == 'weapon': # если нужно создать оружие
            return weapon()
        if beings_tupe == 'armour': # если нужно создать доспехи
            return armour()


# программа 2
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

class car(transport): # класс автомобилей
    def __init__(self, transport_length, transport_width, transport_height, transport_weight, eng_type, s, r):
        super().__init__(transport_length, transport_width, transport_height, transport_weight)
        self.__engine_type = eng_type # 1 -ДВС, 2 - электродвигатель
        self.__car_speed = s # скорость автомобиля
        self.__stopping_distance_coefficient = 0 # коэффициент тормозного пути
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

class aircraft(transport): # класс самолетов 
    def __init__(self, transport_length, transport_width, transport_height, transport_weight, angle):
        super().__init__(transport_length, transport_width, transport_height, transport_weight)
        self.__roll_angle = angle

    def roll_angle_new(self, new_angle): # угол крена
        self.__roll_angle = new_angle

    def get_roll_angle(self): # метод вывода на печать угла крена
        print(self.__roll_angle)

    def check_roll_angle(self, __roll_angle): # проверка допустимого угла крена 
        if 0 < abs(__roll_angle) < 30:
            return 'Допустимый угол крена'
        else:
            return 'Недопустимый угол крена'
    
    def engine(self): # двигатель
        print(self.__roll_angle)

class factory_creation_armor_or_weapons: # фабрика для создания авто или самолёта
    def create_beings(beings_tupe):
        if beings_tupe == 'car': # если нужно создать авто
            return car()
        if beings_tupe == 'aircraft': # если нужно создать самолёт
            return aircraft()

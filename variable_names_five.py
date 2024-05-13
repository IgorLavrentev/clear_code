# 3.1. Улучшите пять имён классов в вашем коде
class manned_spacecraft(spacecraft) - class spacecraft_pilot(spacecraft)
class automatic_spacecraft(spacecraft) - class spacecraft_automation(spacecraft)
class solar_panels - class panels_sun
class train(transport) # новый класс поездов
class ship(transport) # новый класс кораблей

# 3.2. Улучшите семь имён методов и объектов по схеме из пункта 2
class transport
class car(transport):
speed_change # изменение скорости
speed_stop # сброс скорости до нуля
fuel_consumption # расход топлива 
engine_type # тип двигателя
weight # масса
length # длина
width # ширина
class aircraft(transport):
speed_change # изменение скорости
speed_stop # сброс скорости до нуля
fuel_consumption # расход топлива
engine_type # тип двигателя
weight # масса
length # длина
width # ширина
class spacecraft(): # класс космических аппаратов
class manned_spacecraft(spacecraft): # класс пилотируемых космических аппаратов
orbit_correction # коррекция орбиты
engine_type # тип двигателя
weight # масса
length # длина
width # ширина
area_solar_panels # площадь солнечных панелей
height_orbit # высота орбиты
class automatic_spacecraft(spacecraft): # класс автоматических космических аппаратов
orbit_correction # коррекция орбиты
engine_type # тип двигателя
weight # масса
length # длина
width # ширина
area_solar_panels # площадь солнечных панелей
height_orbit # высота орбиты

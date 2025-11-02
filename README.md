# Тема 8. Основы объектно-ориентированного программирования
Отчёт по Теме 8 выполнил:
- Беляев Даниил Алексеевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |      +      |
|  Задание 2  |     +       |      +      |
|  Задание 3  |     +       |      +      |
|  Задание 4  |     +       |      +      |
|  Задание 5  |     +       |      +      |


# Лабораторные работа 1
## Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, mark, model):
        self.mark = mark  # Устанавливаем марку
        self.model = model  # Устанавливаем модель
        

# Создание экземпляра (объекта) класса Car

new_car = Car("Lada", "2107")
```
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e0979bb4-1a87-4f34-8313-54e764d93daa" />

# Лабораторные работа 2
## Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
# Определяем класс Car
class Car:
    def __init__(self, mark, model):
        self.mark = mark  # Устанавливаем марку
        self.model = model  # Устанавливаем модель

    def drive(self):  # Метод drive имитирует движение автомобиля.
        print(f"Автомобиль {self.mark} {self.model} едет!")


# Создание экземпляра (объекта) класса Car

new_car = Car("Lada", "2107")
new_car.drive()

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0ec95314-fb44-4c27-b5c5-d51665ac08b1" />

# Создаем объект класса Car
my_car = Car("Toyota", "Corolla")

# Вызываем метод drive у созданного объекта
my_car.drive()
```
### Результат


# Лабораторные работа 3
##     3) Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться.
Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль. 

```python
class Car:
    def __init__(self, mark, model):
        self.mark = mark  # Устанавливаем марку
        self.model = model  # Устанавливаем модель

    def drive(self):  # Метод drive имитирует движение автомобиля.
        print(f"Автомобиль {self.mark} {self.model} едет!")


# Создание экземпляра (объекта) класса Car

new_car = Car("Lada", "2107")
new_car.drive()

class ElectricCar(Car):
    # конструктор класса ElectricCar
    # принимает дополнительный параметр battery_capacity (емкость батареи)
    def __init__(self, mark, model, battery_capacity):

        super().__init__(mark, model)

        self.battery_capacity = battery_capacity

    # новый метод
    def charge(self):
        print(f"Charging the {self.mark} {self.model} with {self.battery_capacity} kWh")

new_electric_car = ElectricCar("Tesla", "Model S", 100)

new_electric_car.charge()
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4784866b-9600-4442-aabd-a86a320499eb" />


# Лабораторные работа 4
## Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
# Класс Car с инкапсуляцией
class Car:
    # Конструктор класса
    def __init__(self, make, model):
        self._make = make # Защищенный атрибут (одно подчеркивание) условно приватный - доступен, но не рекомендуется использовать извне
        self.__model = model # Приватный атрибут (два подчеркивания) строго приватный - доступ ограничен
    # Метод для движения автомобиля использует защищенный и приватный атрибуты внутри класса
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

# Создаем объект класса Car
my_car = Car("Toyota", "Corolla")
# Доступ к защищенному атрибуту (работает, но не рекомендуется)
print(my_car._make)
# print(my_car.__model)  # Ошибка! Приватный атрибут не доступен
# Вызываем метод drive() - внутри класса доступны все атрибуты
my_car.drive()
```
### Результат


# Лабораторные работа 5
## Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
# Базовый класс Shape
class Shape:
    def area(self) -> float:
        return 0.0


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2


if __name__ == "__main__":
    shapes = [
        Rectangle(30, 20),
        Circle(50)
    ]

    for shape in shapes:
        print(shape.area())
```
### Результат






# Самостоятельная работа 2
## Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class SmartHome:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.lights_on = False
        self.temperature = 22

    def toggle_lights(self):
        """Включить/выключить свет"""
        self.lights_on = not self.lights_on
        status = "включен" if self.lights_on else "выключен"
        print(f"Свет {status}")

    def set_temperature(self, new_temp):
        """Установить температуру"""
        self.temperature = new_temp
        print(f"Температура установлена на {self.temperature}°C")

    def show_info(self):
        """Показать информацию о доме"""
        print(f"Умный дом: {self.name}")
        print(f"Комнат: {self.rooms}")
        print(f"Свет: {'включен' if self.lights_on else 'выключен'}")
        print(f"Температура: {self.temperature}°C")


# Создаем объект и тестируем
my_home = SmartHome("Мой дом", 3)

print("=== Тестирование умного дома ===")
my_home.show_info()

print("\n=== Включаем свет ===")
my_home.toggle_lights()

print("\n=== Меняем температуру ===")
my_home.set_temperature(24)

print("\n=== Выключаем свет ===")
my_home.toggle_lights()

print("\n=== Финальный статус ===")
my_home.show_info()
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/74130fc3-b228-44b1-ae1f-15a351424d3e" />



# Самостоятельная работа 3
## Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class SmartHome:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.lights_on = False
        self.temperature = 22
    
    def toggle_lights(self):
        """Включить/выключить свет"""
        self.lights_on = not self.lights_on
        status = "включен" if self.lights_on else "выключен"
        print(f"Свет {status}")
    
    def set_temperature(self, new_temp):
        """Установить температуру"""
        self.temperature = new_temp
        print(f"Температура установлена на {self.temperature}°C")
    
    def show_info(self):
        """Показать информацию о доме"""
        print(f"Умный дом: {self.name}")
        print(f"Комнат: {self.rooms}")
        print(f"Свет: {'включен' if self.lights_on else 'выключен'}")
        print(f"Температура: {self.temperature}°C")


class SmartApartment(SmartHome):
    def __init__(self, name, rooms, floor):
        super().__init__(name, rooms)
        self.floor = floor
        self.intercom_enabled = False
    
    def toggle_intercom(self):
        """Включить/выключить домофон"""
        self.intercom_enabled = not self.intercom_enabled
        status = "включен" if self.intercom_enabled else "выключен"
        print(f"Домофон {status}")
    
    def show_info(self):
        """Показать информацию о квартире (переопределенный метод)"""
        print(f"Умная квартира: {self.name}")
        print(f"Комнат: {self.rooms}")
        print(f"Этаж: {self.floor}")
        print(f"Свет: {'включен' if self.lights_on else 'выключен'}")
        print(f"Температура: {self.temperature}°C")
        print(f"Домофон: {'включен' if self.intercom_enabled else 'выключен'}")


# Демонстрация работы
print("=== ТЕСТИРОВАНИЕ НАСЛЕДОВАНИЯ ===\n")

print("1. Базовый класс - Умный дом:")
home = SmartHome("Семейный дом", 4)
home.toggle_lights()
home.set_temperature(23)
home.show_info()

print("\n" + "="*40 + "\n")

print("2. Наследуемый класс - Умная квартира:")
apartment = SmartApartment("Студия в центре", 2, 5)
apartment.toggle_lights()
apartment.set_temperature(25)
apartment.toggle_intercom()
apartment.show_info()

print("\n" + "="*40 + "\n")

print("3. Проверка наследования методов:")
print("Метод toggle_lights() из родительского класса:")
apartment.toggle_lights()

print("\nМетод set_temperature() из родительского класса:")
apartment.set_temperature(21)

print("\nФинальный статус квартиры:")
apartment.show_info()
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/63c44428-5459-42aa-9f4c-fcf2ef68d161" />


# Самостоятельная работа 4
## Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class SmartHome:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self._lights_on = False  # защищенный атрибут
        self.__temperature = 22  # приватный атрибут
        self.__security_code = "0000"  # приватный атрибут

    def toggle_lights(self):
        """Включить/выключить свет"""
        self._lights_on = not self._lights_on
        status = "включен" if self._lights_on else "выключен"
        print(f"Свет {status}")

    def set_temperature(self, new_temp):
        """Установить температуру с проверкой диапазона"""
        if 10 <= new_temp <= 35:
            self.__temperature = new_temp
            print(f"Температура установлена на {self.__temperature}°C")
        else:
            print("Ошибка: температура должна быть от 10°C до 35°C")

    def get_temperature(self):
        """Геттер для температуры"""
        return self.__temperature

    def set_security_code(self, old_code, new_code):
        """Сеттер для кода безопасности"""
        if old_code == self.__security_code:
            if len(new_code) == 4 and new_code.isdigit():
                self.__security_code = new_code
                print("Код безопасности успешно изменен")
            else:
                print("Ошибка: код должен состоять из 4 цифр")
        else:
            print("Ошибка: неверный старый код")

    def check_security_code(self, code):
        """Проверить код безопасности"""
        return code == self.__security_code

    def _get_energy_consumption(self):
        """Защищенный метод для расчета энергопотребления"""
        base_consumption = self.rooms * 0.5
        if self._lights_on:
            base_consumption += 0.3
        return base_consumption

    def show_energy_info(self):
        """Публичный метод для показа информации об энергопотреблении"""
        consumption = self._get_energy_consumption()
        print(f"Текущее энергопотребление: {consumption} кВт/ч")

    def show_info(self):
        """Показать публичную информацию о доме"""
        print(f"Умный дом: {self.name}")
        print(f"Комнат: {self.rooms}")
        print(f"Свет: {'включен' if self._lights_on else 'выключен'}")
        print(f"Температура: {self.get_temperature()}°C")


# Демонстрация работы
print("=== ДЕМОНСТРАЦИЯ ИНКАПСУЛЯЦИИ ===\n")

# Создаем объект
home = SmartHome("Мой дом", 3)

print("1. Работа с публичными методами:")
home.toggle_lights()
home.set_temperature(24)
home.show_info()
home.show_energy_info()

print("\n2. Попытка прямого доступа к защищенным атрибутам:")
print(f"Доступ к защищенному атрибуту _lights_on: {home._lights_on}")

print("\n3. Попытка прямого доступа к приватным атрибутам:")
try:
    print(home.__temperature)
except AttributeError as e:
    print(f"Ошибка доступа: {e}")

print("\n4. Работа с кодом безопасности:")
home.set_security_code("0000", "1234")
print(f"Проверка кода '1234': {home.check_security_code('1234')}")
print(f"Проверка кода '9999': {home.check_security_code('9999')}")

print("\n5. Валидация данных:")
home.set_temperature(40)  # Неверная температура
home.set_temperature(25)  # Верная температура

print("\n6. Просмотр всех атрибутов объекта через dir():")
print([attr for attr in dir(home) if not attr.startswith('__')])

print("\n7. Обход инкапсуляции (не рекомендуется):")
# Технически можно получить доступ, но это нарушает принципы ООП
print(f"Температура через обход: {home._SmartHome__temperature}")
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cda003c2-14d8-4fb5-9c04-583d922f67f7" />


# Самостоятельная работа 5
## Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class SmartDevice:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        pass

    def get_status(self):
        pass

    def execute_command(self, command):
        pass


class SmartLight(SmartDevice):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self.brightness = brightness
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return f"💡 Свет {self.name} включен"

    def turn_off(self):
        self.is_on = False
        return f"💡 Свет {self.name} выключен"

    def get_status(self):
        status = "включен" if self.is_on else "выключен"
        return f"Свет {self.name}: {status}, яркость: {self.brightness}%"

    def execute_command(self, command):
        if command == "включить":
            return self.turn_on()
        elif command == "выключить":
            return self.turn_off()
        elif command == "статус":
            return self.get_status()
        else:
            return f"Неизвестная команда для света: {command}"


class SmartThermostat(SmartDevice):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self.temperature = temperature
        self.is_active = False

    def turn_on(self):
        self.is_active = True
        return f"🌡️ Термостат {self.name} активирован"

    def set_temperature(self, temp):
        self.temperature = temp
        return f"🌡️ Температура установлена на {temp}°C"

    def get_status(self):
        status = "активен" if self.is_active else "неактивен"
        return f"Термостат {self.name}: {status}, температура: {self.temperature}°C"

    def execute_command(self, command):
        if command == "включить":
            return self.turn_on()
        elif command == "статус":
            return self.get_status()
        elif command.startswith("установить "):
            temp = command.replace("установить ", "")
            return self.set_temperature(int(temp))
        else:
            return f"Неизвестная команда для термостата: {command}"


class SmartSpeaker(SmartDevice):
    def __init__(self, name, volume=30):
        super().__init__(name)
        self.volume = volume
        self.is_playing = False

    def turn_on(self):
        self.is_playing = True
        return f"🔊 Колонка {self.name} воспроизводит музыку"

    def turn_off(self):
        self.is_playing = False
        return f"🔊 Колонка {self.name} остановлена"

    def get_status(self):
        status = "играет" if self.is_playing else "молчит"
        return f"Колонка {self.name}: {status}, громкость: {self.volume}%"

    def execute_command(self, command):
        if command == "включить":
            return self.turn_on()
        elif command == "выключить":
            return self.turn_off()
        elif command == "статус":
            return self.get_status()
        elif command.startswith("громкость "):
            vol = command.replace("громкость ", "")
            self.volume = int(vol)
            return f"🔊 Громкость установлена на {vol}%"
        else:
            return f"Неизвестная команда для колонки: {command}"


# Функции, демонстрирующие полиморфизм
def control_device(device, command):
    """Универсальная функция управления любым устройством"""
    result = device.execute_command(command)
    print(result)


def show_all_statuses(devices):
    """Показать статусы всех устройств"""
    print("\n📊 Статусы всех устройств:")
    for device in devices:
        print(f"  - {device.get_status()}")


def turn_on_all_devices(devices):
    """Включить все устройства"""
    print("\n🔄 Включаем все устройства:")
    for device in devices:
        print(f"  - {device.turn_on()}")


# Демонстрация работы
print("=== ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА ===\n")

# Создаем разные устройства
light = SmartLight("Гостинная")
thermostat = SmartThermostat("Центральный")
speaker = SmartSpeaker("Музыкальный центр")

# Собираем все устройства в один список
devices = [light, thermostat, speaker]

print("1. Управление устройствами через полиморфные методы:\n")

# Универсальное управление разными устройствами
control_device(light, "включить")
control_device(thermostat, "включить")
control_device(speaker, "включить")

print("\n2. Разные команды для разных устройств:\n")
control_device(thermostat, "установить 24")
control_device(speaker, "громкость 50")

print("\n3. Показ статусов через полиморфизм:")
show_all_statuses(devices)

print("\n4. Включение всех устройств через полиморфизм:")
turn_on_all_devices(devices)

print("\n5. Обработка неизвестных команд:")
control_device(light, "прыгнуть")
control_device(thermostat, "танцевать")

print("\n6. Итерация по устройствам с вызовом полиморфных методов:")
commands = ["статус", "выключить", "статус"]

for device in devices:
    print(f"\nУправляем {device.name}:")
    for command in commands:
        # Проверяем, поддерживает ли устройство команду "выключить"
        if command == "выключить" and hasattr(device, 'turn_off'):
            print(f"  - {device.turn_off()}")
        else:
            control_device(device, command)
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/753221ba-dd84-4aef-9cec-a4e774b8d1dd" />



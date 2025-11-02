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

print("\n" + "=" * 40 + "\n")

print("2. Наследуемый класс - Умная квартира:")
apartment = SmartApartment("Студия в центре", 2, 5)
apartment.toggle_lights()
apartment.set_temperature(25)
apartment.toggle_intercom()
apartment.show_info()

print("\n" + "=" * 40 + "\n")

print("3. Проверка наследования методов:")
print("Метод toggle_lights() из родительского класса:")
apartment.toggle_lights()

print("\nМетод set_temperature() из родительского класса:")
apartment.set_temperature(21)

print("\nФинальный статус квартиры:")
apartment.show_info()
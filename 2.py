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
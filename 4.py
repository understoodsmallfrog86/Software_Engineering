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
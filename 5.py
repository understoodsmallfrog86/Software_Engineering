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
class SmartHome:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.lights_on = False
        self.temperature = 22
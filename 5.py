class AgeValidationError(Exception):
    def __init__(self, age, message="Недопустимый возраст"):
        self.age = age
        self.message = f"{message}: {age}"
        super().__init__(self.message)

def validate_age(age):
    if not isinstance(age, int) or age < 0 or age > 150:
        raise AgeValidationError(age)
    return True

def create_user_profile(name, age):
    try:
        validate_age(age)
        return f"Пользователь {name} (возраст: {age}) создан успешно"
    except AgeValidationError as e:
        return f"Ошибка создания профиля: {e}"

def calculate_retirement_years(age):
    try:
        validate_age(age)
        years_left = 65 - age
        if years_left > 0:
            return f"До пенсии осталось {years_left} лет"
        else:
            return "Вы уже на пенсии"
    except AgeValidationError as e:
        return f"Ошибка расчета: {e}"

print(create_user_profile("Анна", 25))
print(create_user_profile("Петр", -5))
print(calculate_retirement_years(45))
print(calculate_retirement_years(200))
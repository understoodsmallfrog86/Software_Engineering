def calculate_with_two():
    try:
        user_input = input("Введите число для сложения с 2: ")
        number = float(user_input)
        result = 2 + number
        return f"2 + {number} = {result}"
    except ValueError:
        return "Неподходящий тип данных. Ожидалось число."

print(calculate_with_two())
print(calculate_with_two())
def repeat_operation(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                result = func(*args, **kwargs)
                results.append(result)
                print(f"Попытка {i+1}: {result}")
            return results
        return wrapper
    return decorator

@repeat_operation(3)
def generate_password(length=8):
    import random
    import string
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return password

@repeat_operation(2)
def create_username(first_name, last_name):
    return f"{first_name}_{last_name}_{random.randint(100, 999)}"

generate_password(10)
create_username("Иван", "Петров")
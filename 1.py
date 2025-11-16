import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time:.6f} секунд")
        return result
    return wrapper

@timer
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

@timer
def process_data():
    total = 0
    for i in range(1000000):
        total += i
    return total

if __name__ == '__main__':
    calculate_factorial(10000)
    process_data()
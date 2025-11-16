# Тема 10. Декораторы и исключения
Отчёт по Теме 10 выполнил:
- Беляев Даниил Алексеевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |     +       |
|  Задание 2  |     +       |     +       |
|  Задание 3  |     +       |     +       |
|  Задание 4  |     +       |     +       |
|  Задание 5  |     +       |     +       |


# Лабораторные работа 1
## Вам нужно написать программу, которая будет считать числа Фибоначчи для 100 и запустить ее без этого декоратора и с ним, посмотреть на разницу во времени решения поставленной задачи. P.S. при запуске без декоратора можете долго не ждать, для наглядности хватит 10 секунд ожидания.

```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(100))
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ceaa4395-d3fc-45ba-af66-3b6574ff2778" />



# Лабораторные работа 2
## Напишите декоратор для функции, который будет принимать все параметры вызываемой функции (имя, возраст) и проверять чтобы возраст был больше 0 и меньше 130.

```python
def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 130:
            age = 'Недопустимый возраст'
        input_func(name, age)
    return output_func

@check
def personal_info(name, age):
    print(f"Имя: {name} Возраст: {age}")

if __name__ == '__main__':
    personal_info('Sigma', 25)
    personal_info('Alfa', -5)
    personal_info('wtf', 180, 1313, -854)
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/01549f79-6ff2-4957-ba70-e4a5873e42fb" />



# Лабораторные работа 3
## Воспользуйтесь исключениями, чтобы неподходящий тип данных не ломал ваш сайт. Также дополнительно можете обернуть весь код функции в try/except/finally для того, чтобы программа вас оповестила о том, что выявлена какая-то ошибка или программа успешно выполнена.

```python
def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i]*15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Вся информаия обработана')

if __name__ == '__main__':
    data([1, 15, 'Я','Пытаюсь','сломать','твой','сайт', 89, 34])

```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f2319818-6e13-4067-b94d-6ed8e83e9da1" />



# Лабораторные работа 4
## Продолжая работу над сайтом, вы решили написать собственное исключение, которое будет вызываться в случае, если в функцию проверки имени при регистрации передана строка длиннее десяти символов, а если имя имеет допустимую длину, то в консоль выводиться “Успешная регистрация”

```python
class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name) > 10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешная регистрация')

if __name__ == '__main__':
    name = '123456789'
    check_name(name)
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8072d182-3902-4488-b50f-f746b930ca2c" />


# Лабораторные работа 5
## После запуска сайта вы поняли, что вам необходимо добавить логгер, для отслеживания его работы. Готовыми вариантами вы не захотели пользоваться, и поэтому решили создать очень простую пародию. Для этого создали две функции: 		init		() (вызывается при создании класса декоратора в программе) и 	call	() (вызывается при вызове декоратора). Создайте необходимый вам декоратор. Выведите все логи в консоль.

```python
class SiteChecker:
    def __init__(self, func):
        print('> Класс SiteChecker метод __init__ успешный запуск')
        self.func = func
    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@SiteChecker
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/706c1c24-06e1-4080-bd77-1c4ed2000295" />


# Самостоятельная работа 1
##  Вовочка решил заняться спортивным программированием на python, но для этого он должен знать за какое время выполняется его программа. Он решил, что для этого ему идеально подойдет декоратор для функции, который будет выяснять за какое время выполняется та или иная функция. Помогите Вовочке в его начинаниях и напишите такой декоратор.

```python
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
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/85c0a670-59e9-47a8-89a0-3a541860f3a6" />




# Самостоятельная работа 2
## Посмотрев на Вовочку, вы также загорелись идеей спортивного программирования, начав тренировки вы узнали, что для решения некоторых задач необходимо считывать данные из файлов. Но через некоторое время вы столкнулись с проблемой что файлы бывают пустыми, и вы не получаете вводные данные для решения задачи. После этого вы решили не просто считывать данные из файла, а всю конструкцию оборачивать в исключения, чтобы избежать такой проблемы. Создайте пустой файл и файл, в котором есть какая-то информация. Напишите код программы. Если файл пустой, то, нужно вызвать исключение (“бросить исключение”) и вывести в консоль “файл пустой”, а если он не пустой, то вывести информацию из файла.

```python
def read_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            
        if not content:
            raise Exception("Файл пустой")
            
        return content
        
    except FileNotFoundError:
        return "Файл не найден"
    except Exception as e:
        return str(e)

file1_content = read_file_content('data.txt')
print(file1_content)

file2_content = read_file_content('empty.txt')
print(file2_content)
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b4e75aec-61cf-4a89-910e-c8f3fb3a7f30" />




# Самостоятельная работа 3
## Напишите функцию, которая будет складывать 2 и введенное пользователем число, но если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка “Неподходящий тип данных. Ожидалось число.”. Реализовать функционал программы необходимо через try/except и подобрать правильный тип исключения. Создавать собственное исключение нельзя. Проведите несколько тестов, в которых исключение вызывается и нет. Результатом выполнения задачи будет листинг кода и получившийся вывод в консоль

```python
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
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9c0586d0-05cc-44ed-a2eb-cf2777e22a71" />



# Самостоятельная работа 4
## Создайте собственный декоратор, который будет использоваться для двух любых вами придуманных функций. Декораторы, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс декоратора, две как-то связанными с ним функциями, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода.

```python
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
```

### Результат
![Uploading image.png…]()



# Самостоятельная работа 5
## Создайте собственное исключение, которое будет использоваться в двух любых фрагментах кода. Исключения, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс исключения, код к котором в двух местах используется это исключение, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода.

```python
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
```

### Результат
![Uploading image.png…]()



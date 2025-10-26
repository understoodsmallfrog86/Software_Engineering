# Тема 7. Работа с файлами (ввод, вывод)
Отчёт по Теме 7 выполнил:
- Беляев Даниил Алексеевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |    +       |
|  Задание 2  |     +       |    +       |
|  Задание 3  |     +       |    +       |
|  Задание 4  |     +       |    +       |
|  Задание 5  |     +       |    +       |
|  Задание 6  |     +       |           |
|  Задание 7  |     +       |           |
|  Задание 8  |     +       |           |
|  Задание 9  |     +       |           |
|  Задание 10 |    +        |           |

# Лабораторные работа 1
## Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

```
first
second
third
```




# Лабораторные работа 2
## Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
with open('input.txt') as f:
    print(next(f))
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3ae6ee84-8055-4797-a845-9b7e57fb6e82" />




# Лабораторные работа 3
## Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
with open('input.txt') as f:
    print(f.read().splitlines())
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/44660a23-494d-4e5d-ad4e-07d99fd8b6d2" />



# Лабораторные работа 4
##

```python
with open('input.txt') as f:
    print(*f, sep='')
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/378e3f8d-e0b7-45d8-ae01-cc5223d99c59" />



# Лабораторные работа 5
## Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open('input.txt') as f:
    print(*f, sep='')
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/378e3f8d-e0b7-45d8-ae01-cc5223d99c59" />

# Лабораторные работа 6
## Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open('input.txt', 'a+') as f:
    f.write('\nfourth')
    f.seek(0)
    print(f.read())
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d0ceec88-84e1-4b0b-b9d2-2dfb1393557e" />


# Лабораторные работа 7
## Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
```python
data = ['One', 'two', 'three']
with open('input.txt', 'w') as f:
    f.writelines(f'Cycle run {item}\n' for item in data)
print('Done!')
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/715f9cb9-ed52-4409-b050-bdad351e9abe" />


# Лабораторные работа 8
## 
```python
import os

for root, dirs, files in os.walk('D:/мемы'):
    print(f'Папка {root} содержит:\nДиректории: {",".join(dirs)}\nФайлы: {",".join(files)}\n{"-"*40}')
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/414b222e-f603-48ae-868a-43a8f29c91c0" />


# Лабораторные работа 9
## 
```python
with open('input.txt', encoding='utf-8') as f:
    words = f.read().split()
    longest = max(words, key=len)
    print(longest)

```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a02ced65-dbfb-4fb8-81a5-d75d39f25fa6" />


# Лабораторные работа 10
## 
```python
import csv
from datetime import datetime
from time import sleep

with open("rows_300.csv", 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for i in range(1, 301):
        now = datetime.now()
        writer.writerow([i, now.second, now.microsecond])
        sleep(0.01)
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/863c3c3e-3e8f-489b-acf9-4fbe1187f932" />


# Самостоятельная работа 1
## Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация. 

```python
import re
from collections import Counter

with open("input.txt", encoding='utf-8') as f:
    words = re.findall(r'\w+', f.read().lower())

print(f"Общее количество слов: {len(words)}")
print(f"Самое частое слово: '{Counter(words).most_common(1)[0][0]}'")
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c5ef44cf-d49e-4565-8dc0-f91c71651af2" />


# Самостоятельная работа 2
## У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def manage_expenses():
    while True:
        choice = input("1 - Добавить расход, 2 - Показать расходы, 3 - Выход: ")
        if choice == "1":
            with open("rashod.txt", "a", encoding='utf-8') as f:
                f.write(f"{input('Сумма: ')} {input('Категория: ')}\n")
        elif choice == "2":
            try:
                with open("rashod.txt", encoding='utf-8') as f:
                    print("История расходов:\n" + f.read())
            except FileNotFoundError:
                print("Файл пуст")
        elif choice == "3":
            break

manage_expenses()
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bfc8c301-5edb-4181-882f-bd324d06d6f9" />




# Самостоятельная работа 3
## Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
with open("input.txt", encoding='utf-8') as f:
    lines = f.readlines()

print(f"Букв: {sum(c.isalpha() for line in lines for c in line)}")
print(f"Слов: {sum(len(line.split()) for line in lines)}")
print(f"Строк: {len(lines)}")
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2afe780f-4329-4a53-8742-3e917f9018c0" />




# Самостоятельная работа 4
## Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если
файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. Запрещенные слова: hello email python the exam wor is

```python
def censor_text():
    with open('Запрещёные_слова.txt', encoding='utf-8') as f:
        forbidden = set(f.read().split())
    
    text = """Hello, world! Python IS the programming language of thE future. 
My EMAIL is....
PYTHON is awesome!!!!"""
    
    for word in forbidden:
        text = text.replace(word, '*' * len(word))
    print(text)

censor_text()
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e8454a83-c234-4da5-887a-b72c7c7b0adf" />

# Самостоятельная работа 5
## Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```python
import random
import string

def generate_password(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=length))

with open("passwords.txt", "w", encoding='utf-8') as f:
    f.writelines(f"Пароль {i}: {generate_password()}\n" for i in range(1, 6))

print("Пароли сохранены")
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/858b4418-99f6-434d-a3bc-174f18129823" />




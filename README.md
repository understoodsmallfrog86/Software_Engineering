# Тема 11. Итераторы и генераторы
Отчёт по Теме 11 выполнил:
- Беляев Даниил Алексеевич
- Группа: АИС-23-1
  
| Задание     | Лаб_Раб     | Сам_Раб     | 
| ----------- | ----------- | ----------- |
|  Задание 1  |     +       |      +      |
|  Задание 2  |     +       |      +      |
|  Задание 3  |     +       |            |
|  Задание 4  |     +       |            |
|  Задание 5  |     +       |            |


# Лабораторные работа 1
## Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()

```python
num = [0,1,2,3,4,5]
for item in num:
    print(item)
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c2c01a2c-b554-420e-8049-45b935099219" />


# Лабораторные работа 2
## Класс итератор с гибкой настройкой и удобными применением

```python
class CountDown:
    def __init__(self,start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__ == "__main__":
    counter = CountDown(10)
    for i in counter:
        print(i)
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/54119ef1-8412-4356-8996-80ff438dc21a" />


# Лабораторные работа 3
## Генератор списка

```python
a = [i** 2 for i in range(1,5)]

print('a - ', a)
for i in a:
    print(i)

print('iter(a) - ', iter(a))
for i in a:
    print(i)
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/63f76c97-12fd-487c-8a16-ebb9ab2ade2d" />


# Лабораторные работа 4
## Выражения генераторы
```python
b = (i** 2 for i in range(1,5))
print(b)
print('first')
for i in b:
    print(i)
print('second')
for i in b:
    print(i)
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7b3e0c26-f428-4516-8ba5-866e33d25d5a" />


# Лабораторные работа 5
## Такой же счетчик, как и в первом задании, только это генератор и использует yield 

```python
def countdown(count):
    while count >=0:
        yield count
        count -= 1

if __name__ == '__main__':
    counter = countdown(10)
    for i in counter:
        print(i)
```
### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6c174417-db0d-4084-a807-521a49cc947d" />


# Самостоятельная работа 1
## Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи при помощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(*fib(250))
```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/aa134494-d5b2-4f37-a67c-317dba1a9059" />


# Самостоятельная работа 2
## К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла

```python
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 250
with open("fib.txt", "w") as file:
    for number in fib(n):
        file.write(f"{number}\n")


```

### Результат
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1221b045-53a5-4418-8cec-26de25e9e23c" />



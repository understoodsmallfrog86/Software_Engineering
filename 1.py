def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 250
with open("fib.txt", "w") as file:
    for number in fib(n):
        file.write(f"{number}\n")


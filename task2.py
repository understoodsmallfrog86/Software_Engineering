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
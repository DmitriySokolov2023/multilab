def advanced_calculator():
    print("Добро пожаловать в расширенный калькулятор!")
    print("Введите математическое выражение (например, 3 + 4 * 2), или 'q' для выхода.")

    while True:
        expression = input("Введите выражение: ")
        if expression.lower() == 'q':
            print("До свидания!")
            break
        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except (SyntaxError, NameError, ZeroDivisionError):
            print("Ошибка: некорректное выражение.")

# Запуск расширенного калькулятора
advanced_calculator()
import sympy as sp

# Функция для вычисления выражений
def evaluate_expression(expr):
    try:
        # Преобразуем выражение в символьное и вычисляем
        result = sp.sympify(expr)
        return result
    except Exception as e:
        return f"Ошибка в выражении: {e}"

# Функция для дифференцирования
def differentiate(expr, variable):
    try:
        # Преобразуем выражение в символьное
        symbol = sp.symbols(variable)
        diff_expr = sp.diff(expr, symbol)
        return diff_expr
    except Exception as e:
        return f"Ошибка при дифференцировании: {e}"

# Функция для интегрирования
def integrate(expr, variable):
    try:
        # Преобразуем выражение в символьное
        symbol = sp.symbols(variable)
        integral_expr = sp.integrate(expr, symbol)
        return integral_expr
    except Exception as e:
        return f"Ошибка при интегрировании: {e}"

# Основной калькулятор
def calculator():
    print("Простой калькулятор с символьными вычислениями (sympy).")
    print("Доступные операции: +, -, *, /, дифференцирование, интегрирование.")
    
    while True:
        print("\nВведите выражение или команду (для выхода введите 'exit'):")
        expr = input("Введите выражение: ")

        if expr.lower() == 'exit':
            print("Выход из калькулятора.")
            break

        # Проверка на дифференцирование
        if expr.startswith("diff"):
            try:
                _, expression, variable = expr.split()
                result = differentiate(expression, variable)
            except ValueError:
                result = "Ошибка: неправильный формат команды для дифференцирования."
        # Проверка на интегрирование
        elif expr.startswith("integrate"):
            try:
                _, expression, variable = expr.split()
                result = integrate(expression, variable)
            except ValueError:
                result = "Ошибка: неправильный формат команды для интегрирования."
        else:
            result = evaluate_expression(expr)

        print(f"Результат: {result}")

# Запуск калькулятора
calculator()
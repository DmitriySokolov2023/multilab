import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, нет ли ошибки
        data = response.json()
        return data['rates'].get(target_currency, None)
    except requests.exceptions.RequestException:
        print("Ошибка при получении данных. Проверьте подключение к интернету.")
        return None

def currency_converter():
    base_currency = input("Введите код исходной валюты (например, USD, EUR, RUB): ").upper()
    target_currency = input("Введите код целевой валюты: ").upper()
    amount = input("Введите сумму для конвертации: ")

    try:
        amount = float(amount)
        rate = get_exchange_rate(base_currency, target_currency)

        if rate:
            converted_amount = amount * rate
            print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            print("Ошибка: Неверный код валюты.")
    except ValueError:
        print("Ошибка: Введите корректное число.")

# Запуск программы
currency_converter()
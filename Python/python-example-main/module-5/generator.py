import random
import string

def generate_password(length=12, complexity=3):
    """
    Генерирует случайный пароль заданной длины и сложности.
    
    complexity:
    1 - Только буквы
    2 - Буквы + цифры
    3 - Буквы + цифры + спецсимволы
    """
    lower = string.ascii_lowercase  # строчные буквы
    upper = string.ascii_uppercase  # заглавные буквы
    digits = string.digits          # цифры
    symbols = string.punctuation    # спецсимволы

    if complexity == 1:
        chars = lower + upper  # Только буквы
    elif complexity == 2:
        chars = lower + upper + digits  # Буквы + цифры
    else:
        chars = lower + upper + digits + symbols  # Полный набор

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_password(password):
    """Сохраняет пароль в файл passwords.txt"""
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("✅ Пароль сохранен в passwords.txt")

def main():
    print("🔐 Генератор паролей 🔐")
    
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        complexity = int(input("Выберите сложность (1 - буквы, 2 - буквы+цифры, 3 - буквы+цифры+символы): ") or 3)
        count = int(input("Сколько паролей сгенерировать? (по умолчанию 1): ") or 1)

        print("\n🎲 Сгенерированные пароли:")
        for _ in range(count):
            password = generate_password(length, complexity)
            print(password)
            
            save_option = input("💾 Хотите сохранить этот пароль? (y/n): ")
            if save_option.lower() == 'y':
                save_password(password)
    
    except ValueError:
        print("⚠ Ошибка! Введите число.")

if __name__ == "__main__":
    main()

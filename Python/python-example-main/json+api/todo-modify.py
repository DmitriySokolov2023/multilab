
import json
from datetime import datetime

TODO_FILE = "todo_list.json"

# Функция загрузки задач из файла
def load_tasks():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Функция сохранения задач в файл
def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

# Функция для добавления задачи
def add_task(tasks):
    task_name = input("Введите название задачи: ")
    category = input("Введите категорию (например, Работа, Дом, Учеба): ")
    deadline = input("Введите дедлайн (в формате ГГГГ-ММ-ДД, например, 2025-03-10): ")

    # Проверка корректности даты
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("⚠ Некорректный формат даты! Дедлайн не установлен.")
        deadline = "Без дедлайна"

    # Добавляем задачу в список
    tasks.append({"task": task_name, "category": category, "deadline": deadline})
    save_tasks(tasks)
    print("✅ Задача добавлена!")

# Функция для удаления задачи
def delete_task(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} ({task['category']}, {task['deadline']})")

    try:
        task_index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"❌ Задача '{removed_task['task']}' удалена!")
        else:
            print("⚠ Неверный номер задачи!")
    except ValueError:
        print("⚠ Введите число!")

# Функция для поиска задач по ключевому слову
def search_tasks(tasks):
    keyword = input("Введите ключевое слово для поиска: ").lower()
    found_tasks = [task for task in tasks if keyword in task['task'].lower() or keyword in task['category'].lower()]
    
    if found_tasks:
        print("\n🔍 Найденные задачи:")
        for task in found_tasks:
            print(f"- {task['task']} ({task['category']}, {task['deadline']})")
    else:
        print("⚠ Ничего не найдено!")

# Основное меню программы
def main():
    tasks = load_tasks()

    while True:
        print("\n📌 Список дел:")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']} ({task['category']}, {task['deadline']})")
        else:
            print("Список пуст!")

        print("\nВыберите действие:")
        print("1 - Добавить задачу")
        print("2 - Удалить задачу")
        print("3 - Поиск задачи")
        print("4 - Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            search_tasks(tasks)
        elif choice == "4":
            print("👋 До свидания!")
            break
        else:
            print("⚠ Некорректный ввод! Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()

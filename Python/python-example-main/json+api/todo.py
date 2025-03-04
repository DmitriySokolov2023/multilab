import json

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

# Основное меню программы
def main():
    tasks = load_tasks()

    while True:
        print("\n📌 Список дел:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print("\nВыберите действие:")
        print("1 - Добавить задачу")
        print("2 - Удалить задачу")
        print("3 - Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            new_task = input("Введите новую задачу: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("✅ Задача добавлена!")

        elif choice == "2":
            try:
                task_index = int(input("Введите номер задачи для удаления: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    save_tasks(tasks)
                    print(f"❌ Задача '{removed_task}' удалена!")
                else:
                    print("⚠ Неверный номер задачи!")
            except ValueError:
                print("⚠ Введите число!")

        elif choice == "3":
            print("👋 До свидания!")
            break
        else:
            print("⚠ Некорректный ввод! Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
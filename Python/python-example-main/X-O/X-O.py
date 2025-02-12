def print_board(board):
    #Выводит игровое поле
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Проверяет победителя"""
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None  # Нет победителя

def is_full(board):
    """Проверяет, заполнено ли поле"""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Основная логика игры"""
    board = [[" " for _ in range(3)] for _ in range(3)] # Матрица из пустых строк 3x3
    current_player = "X"
    while True:
        print_board(board)
        print(f"Ходит {current_player}. Введите номер строки и столбца (0-2):")

        try:
            row, col = map(int, input().split()) # Функция меп идет по числам, которые мы вводим (например мы ввели 2 0, с помощью сплита преобразовали в [2, 0], а диструктуризация присвоила row = 2, col = 0)
            if board[row][col] != " ":
                print("Эта клетка уже занята! Попробуйте снова.")
                continue
        except (ValueError, IndexError):
            print("Некорректный ввод! Введите два числа от 0 до 2.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Игрок {winner} победил!")
            break
        if is_full(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

# Запуск игры
tic_tac_toe()
def print_board(board):
  """Выводит игровое поле в консоль."""
  print("---------")
  for row in board:
    print("|", end="")
    for cell in row:
      print(f" {cell} |", end="")
    print("\n---------")

def get_player_move(player):
  """Получает координаты хода от игрока."""
  while True:
    try:
      row, col = map(int, input(f"Игрок {player}, введите координаты хода (строка, столбец): ").split())
      if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
        return row - 1, col - 1
      else:
        print("Некорректные координаты. Попробуйте снова.")
    except ValueError:
      print("Неверный формат ввода. Попробуйте снова.")

def check_win(board):
  """Проверяет, есть ли победитель."""
  # Проверка строк
  for row in board:
    if row.count("X") == 3 or row.count("O") == 3:
      return row[0]

  # Проверка столбцов
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] != " ":
      return board[0][col]

  # Проверка диагоналей
  if board[0][0] == board[1][1] == board[2][2] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] != " ":
    return board[0][2]

  # Ничья
  if all(cell != " " for row in board for cell in row):
    return "Ничья"

  return None

# Инициализация игрового поля
board = [[" " for _ in range(3)] for _ in range(3)]

# Начало игры
current_player = "X"
while True:
  print_board(board)
  row, col = get_player_move(current_player)

  # Делаем ход
  board[row][col] = current_player

  # Проверяем, есть ли победитель
  winner = check_win(board)
  if winner:
    print_board(board)
    if winner == "Ничья":
      print("Ничья!")
    else:
      print(f"Игрок {winner} победил!")
    break

  # Переключаем ход
  current_player = "O" if current_player == "X" else "X"
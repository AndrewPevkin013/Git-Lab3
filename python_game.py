import random
def create_field():
    field = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
    ]
    return field
def draw_field(field):
    for i in range(5):
        for j in range(5):
            print(field[i][j], end=' ')
        print(" ")
def place_ship(field):
    orientation = random.randint(1, 2)
    if orientation == 1:
        # Располагаем корабль горизонтально
        row = random.randint(0, 4)
        column = random.randint(0, 2)

        for i in range(column, column + 3):
            field[row][i] = "O"
    else:
        # Располагаем корабль вертикально
        row = random.randint(0, 2)
        column = random.randint(0, 4)

        for i in range(row, row + 3):
            field[row][column] = "O"

    return field


def check_hit(field, row, column):
    if 0 <= row <= 4 and 0 <= column <= 4:
        if field[row][column] == "O":
            return 1
        else:
            return 0
    else:
        return -1


field = create_field()
field = place_ship(field)
user_field = create_field()

tries = 3

while tries > 0:
    row = int(input("Введите номер ряда (от 0 до 4)"))
    column = int(input("Введите номер столбца (оот 0 до 4)"))
    result = check_hit(field, row, column)
    if result == 1:
        print("Попадание!")
        user_field[row][column] = 'O'
    elif result == 0:
        print("Мимо!")
    else:
        print("Неправильный номер ряда или столбца")

    draw_field(user_field)

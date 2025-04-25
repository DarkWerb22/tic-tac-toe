win_state = False
playing_field = list(range(1, 10))
counter = 0
all_win_coords = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

while not win_state:
    for wands in range(0, 9, 3):
        print("|", playing_field[wands], "|", playing_field[wands + 1], "|", playing_field[wands + 2], "|")
    if counter % 2:
        print("Ход игрока 0")
        symbol = "0"
    else:
        print("Ход игрока X")
        symbol = "X"
    valid = False
    while not valid:
        position = int(input("Выберете куда поставить: "))
        if playing_field[position - 1] in ["X", "0"]:
            print("Эта клетка уже занята")
        else:
            playing_field[position - 1] = symbol
            valid = True
    counter += 1
    if counter > 4:
        for coord in all_win_coords:
            if playing_field[coord[0]-1] == playing_field[coord[1]-1] == playing_field[coord[2]-1]:
                print("Выиграл игрок", symbol)
                win_state = True
                for wands in range(0, 9, 3):
                    print("|", playing_field[wands], "|", playing_field[wands + 1], "|", playing_field[wands + 2], "|")
    if counter == 9 and not win_state:
        print("Ничья")
        win_state = True




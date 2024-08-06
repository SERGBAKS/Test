M = list(range(1, 10))  # List в дальнейшем Matrix


def draw(M): # Обёртка list в matrix
    for i in range(3):
        print(M[0 + i * 3], M[1 + i * 3], M[2 + i * 3])


def check_win(M): # Подсчёт очков
    win_cord = ((0, 1, 2),(3, 4, 5),(6, 7, 8),
                (0, 3, 6),(1, 4, 7),(2, 5, 8),
                (0, 4, 8), (2, 4, 6)
                )
    for each in win_cord:
        if M[each[0]] == M[each[1]] == M[each[2]]:
            return M[each[0]]
    return False


def player_choise(M, token):
    valid = False
    while not valid:
        print(f"Ход игрока - {token}")
        c = int(input())
        if str(M[c - 1]) not in "XO":
            M[c - 1] = token
            valid = True
        else:
            while str(M[c - 1]) in "XO":
                print("Игрок Х, эта клетка занята. Попробуй другую: ")
                c = int(input())
                M[c - 1] = token



def Main(M):
    count = 1
    win = False
    while not win:
        draw(M)
        if count % 2 != 0:
            player_choise(M, "X")
        else:
            player_choise(M, "O")
        count += 1

        tmp = check_win(M)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if count == 9:
            print("Ничья!")
            break
    draw(M)


Main(M)






















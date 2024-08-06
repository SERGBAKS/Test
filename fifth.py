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


def player_choise(M):
    count = 1
    while check_win(M) == False:
        if count % 2 != 0:
            print("Ход игрока - Х")
            count += 1
            c = int(input())
            if M[c-1] != "X" and M[c-1] != "O":
                M[c - 1] = "X"
                draw(M)
            else:
                while M[c-1] == "X" or M[c-1] == "O":
                    print("Игрок Х, эта клетка занята. Попробуй другую: ")
                    c = int(input())
                else:
                    M[c - 1] = "X"
                    draw(M)
        else:
            print("Ход игрока - O")
            count += 1
            c = int(input())
            if M[c-1] != "X" and M[c-1] != "O":
                M[c-1] = "O"
                draw(M)
            else:
                while M[c - 1] == "X" or M[c - 1] == "O":
                    print("Игрок O, эта клетка занята. Попробуй другую: ")
                    c = int(input())
                else:
                    M[c - 1] = "O"
                    draw(M)





draw(M)
player_choise(M)














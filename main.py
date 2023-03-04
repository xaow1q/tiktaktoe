field = list(range(1, 10))


def draw_board(field):
    print("-" * 13)
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Make a move " + player_token)
        try:
            player_answer = int(player_answer)
        except:
            print("Incorrect symbol, are you entering a digit?")
            continue
        if 1 <= player_answer <= 9:
            if str(field[player_answer - 1]) not in "XO":
                field[player_answer - 1] = player_token
                valid = True
            else:
                print("This cell is already engaged!")
        else:
            print("Incorrect symbol, enter a digit between 1 and 9.")


def check_win(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    counter = 0
    win = False
    while not win:
        draw_board(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print(tmp, "Win")
                win = True
                break
        if counter == 9:
            print("Draw!")
            break
    draw_board(field)


main(field)

input("Press Enter to exit!")

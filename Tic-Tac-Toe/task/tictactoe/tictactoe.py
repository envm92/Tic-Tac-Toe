# write your code here
x_plays = 0
o_plays = 0
cells = [['_' for y in range(0, 3)] for x in range(0, 3)]
turn = 'X'


def start_game():
    is_over = False
    while not is_over:
        print_board()
        check_input()
        if x_plays > 2:
            message = who_won()
            print('HELLO MESSAGE')
            print(message)
            if message != '':
                print_board()
                print(message)
                break
        change_turn()


def change_turn():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


def symbol_lines(__cells, symbol):
    # Check all the verticals
    lines = 0
    for i, __row in enumerate(__cells):
        for j, cell in enumerate(__row):
            if cell != symbol:
                break
            elif j == 2:
                lines += 1
    # Check all the horizontals
    for i, __row in enumerate(__cells):
        for j, cell in enumerate(__row):
            if __cells[j][i] != symbol:
                break
            elif j == 2:
                lines += 1
    # Check all the horizontals
    for i, _ in enumerate(__cells):
        if __cells[i][i] != symbol:
            break
        elif i == 2:
            lines += 1
    for i, _ in enumerate(__cells):
        if __cells[len(__cells) - 1 - i][i] != symbol:
            break
        elif i == 2:
            lines += 1
    return lines


def who_won():
    global x_plays
    global o_plays
    global cells
    difference_between = abs(x_plays - o_plays)
    x_lines = symbol_lines(cells, 'X')
    o_lines = symbol_lines(cells, 'O')
    if difference_between > 1 or (difference_between <= 1 and 0 < x_lines == o_lines):
        return 'Impossible'
    if x_lines == o_lines and x_lines == 0:
        print(x_plays + o_plays)
        if (x_plays + o_plays) == 9:
            return 'Draw'
        else:
            return ''
    if x_lines > o_lines:
        return 'X wins'
    elif o_lines > x_lines:
        return 'O wins'


def move(x, y):
    global cells
    global turn
    global x_plays
    global o_plays
    cells[x][y] = turn
    if turn == 'X':
        x_plays += 1
    else:
        o_plays += 1


def check_input():
    global cells
    valid = False
    while not valid:
        next_move = input('Enter the coordinates:')
        [x, y] = next_move.split(' ')
        if x.isnumeric() and y.isnumeric():
            x = int(x)
            y = int(y)
            if (1 <= x <= 3) and (1 <= y <= 3):
                if cells[x - 1][y - 1] == '_':
                    move(x - 1, y - 1)
                    valid = True
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


def print_board():
    print('---------')
    global cells
    for row in cells:
        row_to_print = '|'
        row_to_print += '  ' if row[0] == '_' else ' ' + row[0]
        row_to_print += '  ' if row[1] == '_' else ' ' + row[1]
        row_to_print += '  ' if row[2] == '_' else ' ' + row[2]
        print(row_to_print, '|')
    print('---------')


start_game()

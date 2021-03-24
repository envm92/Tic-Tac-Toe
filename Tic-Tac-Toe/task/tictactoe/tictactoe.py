# write your code here

x_plays = 0
o_plays = 0


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


def count_plays(__raw_input):
    global x_plays
    x_plays = 0
    global o_plays
    o_plays = 0
    for s in __raw_input:
        if s == 'X':
            x_plays += 1
        elif s == 'O':
            o_plays += 1
    return [x_plays, o_plays]


def who_won(__cells):
    global x_plays
    global o_plays
    global raw_input
    [x_plays, o_plays] = count_plays(raw_input)
    difference_between = abs(x_plays - o_plays)
    x_lines = symbol_lines(__cells, 'X')
    o_lines = symbol_lines(__cells, 'O')
    if difference_between > 1 or (difference_between <= 1 and 0 < x_lines == o_lines):
        pass # print('Impossible')
        return
    if x_lines == o_lines and x_lines == 0:
        if (x_plays + o_plays) == 9:
            pass # print('Draw')
        else:
            pass # print('Game not finished')
    if x_lines > o_lines:
        pass # print('X wins')
    elif o_lines > x_lines:
        pass # print('O wins')


def move(x, y):
    global cells
    cells[x][y] = 'X'


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

raw_input = input('Enter cells:')
cells = list(raw_input)
cells = [cells[i * 3:(i + 1) * 3] for i in range((len(cells) + 3 - 1) // 3)]
print_board()
who_won(cells)
check_input()
print_board()

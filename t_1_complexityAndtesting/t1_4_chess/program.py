import sys


def figure_finder(data):
    if len(data) < 8:
        return 0

    figures = []

    for row_index, line in enumerate(data):
        for col_index, char in enumerate(line):
            if char in ['R', 'B']:
                figures.append([char, col_index, row_index])
    return figures


def check_obstacle(x, y, figure, figures):
    if figure[0] == 'R':
        return (['R', x, y] == figure or ['R', x, y] not in figures) and ['B', x, y] not in figures
    else:
        return (['R', x, y] != figure and ['R', x, y] in figures) or ['B', x, y] in figures


def moves_writer(figures, table):
    for figure in figures:
        if figure[0] == 'R':
            x = figure[1]
            y = figure[2]

            for x in range(x + 1, 8):
                if check_obstacle(x, y, figure, figures):
                    table[y][x] = '0'
                else:
                    break
                x += 1

            x = figure[1]
            y = figure[2]
            for _x in range(1, x + 1):
                x = figure[1] - _x
                if check_obstacle(x, y, figure, figures):
                    table[y][x] = '0'
                else:
                    break
                _x += 1

            x = figure[1]
            y = figure[2]
            for y in range(y + 1, 8):
                if check_obstacle(x, y, figure, figures):
                    table[y][x] = '0'
                else:
                    break
                y += 1

            x = figure[1]
            y = figure[2]
            for _y in range(1, y + 1):
                y = figure[2] - _y
                if check_obstacle(x, y, figure, figures):
                    table[y][x] = '0'
                else:
                    break
                _y += 1
        else:
            if figure[0] == 'B':
                x = figure[1] + 1
                y = figure[2] + 1
                while x < 8 and y < 8:
                    if check_obstacle(x, y, figure, figures):
                        break
                    else:
                        table[y][x] = '0'
                    y += 1
                    x += 1

                x = figure[1] - 1
                y = figure[2] - 1
                while x >= 0 and y >= 0:
                    if check_obstacle(x, y, figure, figures):
                        break
                    else:
                        table[y][x] = '0'
                    y -= 1
                    x -= 1

                x = figure[1] + 1
                y = figure[2] - 1
                while x < 8 and y >= 0:
                    if check_obstacle(x, y, figure, figures):
                        break
                    else:
                        table[y][x] = '0'
                    y -= 1
                    x += 1

                x = figure[1] - 1
                y = figure[2] + 1
                while x >= 0 and y < 8:
                    if check_obstacle(x, y, figure, figures):
                        break
                    else:
                        table[y][x] = '0'
                    y += 1
                    x -= 1
    return table


def main():
    input_data = list(map(list, sys.stdin.read().strip().split('\n')))
    figures = figure_finder(input_data)

    if figures == 0:
        return 0

    table = moves_writer(figures, input_data)
    desk = str(table)

    return 64 - (desk.count('0') + len(figures))


if __name__ == '__main__':
    print(main())

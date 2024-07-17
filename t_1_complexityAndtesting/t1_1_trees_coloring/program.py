import sys


def main():
    input_data = sys.stdin.read().strip().split('\n')

    try:
        input_data = [painter.split() for painter in input_data]
        input_data = [[int(value) for value in painter] for painter in input_data]
    except:
        return 0

    if len(input_data[0]) == 0 or len(input_data[0]) == 1:
        return 0
    if len(input_data) == 1 and len(input_data[0]) == 2:
        coord = input_data[0][0]
        limit = input_data[0][1]
        return len(range(coord - limit, coord + limit)) + 1
    else:
        return range_calculator(input_data)


def range_calculator(coordinates):
    try:
        first_painter = coordinates[0]

        if coordinates[0][0] > coordinates[1][0]:
            coordinates[0] = coordinates[1]
            coordinates[1] = first_painter
        else:
            pass

        for painter in coordinates:
            painter[0], painter[1] = painter[0] - painter[1], painter[0] + painter[1]

        if coordinates[1][0] > coordinates[0][1]:
            intersection = 1
        elif coordinates[0][1] == coordinates[1][0]:
            intersection = 2
        elif coordinates[1][0] - coordinates[0][0] >= 0 >= coordinates[1][1] - coordinates[0][1]:
            intersection = len(range(coordinates[1][0], coordinates[1][1])) + 2
        elif coordinates[0][0] - coordinates[1][0] >= 0 >= coordinates[0][1] - coordinates[1][1]:
            intersection = len(range(coordinates[0][0], coordinates[0][1])) + 2
        elif coordinates[1][0] < coordinates[0][1]:
            intersection = coordinates[0][1] - coordinates[1][0] + 2
        else:
            intersection = abs(coordinates[0][1] - coordinates[1][0]) + 2
        return (len(range(coordinates[0][0], coordinates[0][1]))
                + len(range(coordinates[1][0], coordinates[1][1])) - intersection + 3)
    except:
        return 0


if __name__ == '__main__':
    print(main())

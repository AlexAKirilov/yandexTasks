import sys


def spaces_calc(space_num):
    tabs = space_num // 4
    space_to_add = (space_num - tabs * 4) / 1

    if tabs * 4 == space_num:
        return tabs
    elif tabs == 1 or tabs == 0 or space_to_add == 1:
        return min(tabs + space_to_add, ((tabs + 1) * 4 - space_num) / 1 + tabs + 1)
    elif space_num < 0:
        return space_num / -1
    else:
        backspace_to_add = ((tabs + 1) * 4 - space_num) / 1
        return min(tabs + space_to_add, tabs + 1 + backspace_to_add)


def main():
    try:
        input_data = list(map(int, sys.stdin.read().strip().split('\n')))

        lines_to_process = input_data[0]
        keys_count = 0
        if len(input_data) == 1:
            return int(spaces_calc(input_data[0]))
        else:
            for line in input_data[1:lines_to_process + 1]:
                keys_count += spaces_calc(line)

        return int(keys_count)
    except:
        return 0


if __name__ == '__main__':
    print(main())

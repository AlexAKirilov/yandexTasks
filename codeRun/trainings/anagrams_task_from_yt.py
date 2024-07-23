def letters_counter(strng):
    letters = {}
    for letter in strng:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 0
    return letters


def main():
    st_1 = 'jjjj'
    st_2 = 'jjj'
    print(letters_counter(st_1))
    print(letters_counter(st_2))
    print(letters_counter(st_1) == letters_counter(st_2))


if __name__ == '__main__':
    main()

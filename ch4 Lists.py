def list_to_string(list_of_things):
    s = ""
    c = len(list_of_things)
    for l in list_of_things:
        c -= 1
        if c == 1:
            s = s + l + " and "
        elif c == 0:
            s = s + l + " "
        else:
            s = s + l + ", "
    return s


spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(spam))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()





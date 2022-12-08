line_len = 0
line_num = 0


def is_visible(x, y, grid):
    tree = grid[x][y]
    max_left, max_top, max_right, max_bottom = 0, 0, 0, 0
    for j in range(0, y):
        if grid[x][j] > max_left:
            max_left = grid[x][j]
    for i in range(0, x):
        if grid[i][y] > max_top:
            max_top = grid[i][y]
    for j in range(y + 1, line_len):
        if grid[x][j] > max_right:
            max_right = grid[x][j]
    for i in range(x + 1, line_num):
        if grid[i][y] > max_bottom:
            max_bottom = grid[i][y]

    return 1 if tree > max_bottom or tree > max_top or tree > max_right or tree > max_left else 0


def calculate_scenic_view(x, y, grid):
    tree = grid[x][y]
    scenic_view_score = 1
    left, top, right, bottom = 0, 0, 0, 0
    for j in range(y - 1, 0, -1):
        if grid[x][j] >= tree:
            left += 1
            scenic_view_score *= (y - j)
            break
    if left == 0:
        scenic_view_score *= y
    for i in range(x - 1, 0, -1):
        if grid[i][y] >= tree:
            top += 1
            scenic_view_score *= (x - i)
            break
    if top == 0:
        scenic_view_score *= x
    for j in range(y + 1, line_len):
        if grid[x][j] >= tree:
            right += 1
            scenic_view_score *= (j - y)
            break
    if right == 0:
        scenic_view_score *= (line_len - y - 1)
    for i in range(x + 1, line_num):
        if grid[i][y] >= tree:
            bottom += 1
            scenic_view_score *= (i - x)
            break
    if bottom == 0:
        scenic_view_score *= (line_num - x - 1)

    return scenic_view_score


if __name__ == '__main__':
    f = open("input.txt", "r")

    for line in f:
        line_len = len(line.strip())
        line_num += 1

    forest = [[0 for i in range(line_len)] for j in range(line_num)]
    f.seek(0)

    i = 0
    for line in f:
        j = 0
        for char in line.strip():
            forest[i][j] = int(char)
            j += 1
        i += 1

    num_of_visible = 2 * line_num + 2 * line_len - 4
    max_scenic_view = 0
    for i in range(1, line_num - 1):
        for j in range(1, line_len - 1):
            num_of_visible += is_visible(i, j, forest)
            max_scenic_view = max(calculate_scenic_view(i, j, forest), max_scenic_view)

    print(num_of_visible)
    print(max_scenic_view)
    f.close()

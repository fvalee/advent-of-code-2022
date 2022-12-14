grid = [["."] * 700 for i in range(700)]


def print_reservoir():
    for i in range(700):
        for j in range(700):
            print(grid[i][j], end="")
        print()


def set_obstacles(d):
    for line in d:
        line = line.split("->")
        coords = len(line)
        dx, dy = 0, 0
        for i in range(coords):
            if i == 0:
                x, y = line[i].split(",")
            else:
                x, y = dx, dy
            if i < coords - 1:
                dx, dy = line[i + 1].split(",")
            x, y, dx, dy = int(x), int(y), int(dx), int(dy)
            if x == dx and y == dy:
                break
            if x == dx:
                a, b = min(y, dy), max(y, dy)
                for j in range(a, b + 1):
                    grid[j][x] = "#"
            elif y == dy:
                a, b = min(x, dx), max(x, dx)
                for j in range(a, b + 1):
                    grid[y][j] = "#"


if __name__ == '__main__':
    f = open("../input.txt", "r")
    data = []
    for line in f:
        data.append(line.strip())
    f.close()

    set_obstacles(data)
    last_row = 0
    for i in range(700):
        if "#" in grid[i]:
            last_row = i
    last_row += 2
    for i in range(700):
        grid[last_row][i] = "#"

    reached_top = False
    grains_of_sand = 0
    while True:
        i = 0
        source_y = 500
        start = grid[i][source_y]
        while True:
            if i >= last_row:
                break
            if grid[i + 1][source_y] == ".":
                i += 1
                continue
            elif grid[i + 1][source_y - 1] == ".":
                i += 1
                source_y -= 1
                continue
            elif grid[i + 1][source_y + 1] == ".":
                i += 1
                source_y += 1
                continue
            elif grid[i][source_y] != ".":
                reached_top = True
                break
            break
        if i >= last_row or reached_top:
            break
        grid[i][source_y] = "o"
        grains_of_sand += 1

    print(grains_of_sand)

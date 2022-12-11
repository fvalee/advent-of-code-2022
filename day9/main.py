current_H = "0,0"
prev_H = "0,0"
current_T = "0,0"
visited = set()


def move(direction, times):
    global current_H, prev_H
    if direction == "R":
        for i in range(times):
            prev_H = current_H
            current_H = current_H.split(",")[0] + "," + str(int(current_H.split(",")[1]) + 1)
            calculate_tail_position()
    if direction == "L":
        for i in range(times):
            prev_H = current_H
            current_H = current_H.split(",")[0] + "," + str(int(current_H.split(",")[1]) - 1)
            calculate_tail_position()
    if direction == "U":
        for i in range(times):
            prev_H = current_H
            current_H = str(int(current_H.split(",")[0]) + 1) + "," + current_H.split(",")[1]
            calculate_tail_position()
    if direction == "D":
        for i in range(times):
            prev_H = current_H
            current_H = str(int(current_H.split(",")[0]) - 1) + "," + current_H.split(",")[1]
            calculate_tail_position()


def calculate_tail_position():
    global current_H, current_T
    head = current_H.split(",")
    tail = current_T.split(",")
    if abs(int(head[0]) - int(tail[0])) > 1 or abs(int(head[1]) - int(tail[1])) > 1:
        current_T = prev_H
        visited.add(current_T)


if __name__ == '__main__':
    f = open("input.txt", "r")
    visited.add(current_T)

    for line in f:
        line = line.strip().split()
        move(line[0], int(line[1]))

    print(len(visited))
    f.close()

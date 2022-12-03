def calculate_priority(r1, r2, r3):
    dict_r1 = set(r1)
    dict_r2 = set(r2)
    dict_r3 = set(r3)

    common = dict_r1 & dict_r2 & dict_r3
    item = next(iter(common))

    return ord(item) - 96 if item.islower() else ord(item) - 38


if __name__ == '__main__':
    f = open("../input.txt", "r")

    priority_sum = 0
    line_number = 1
    lines = []
    for line in f:
        lines.append(line.strip())
        if line_number == 3:
            priority_sum += calculate_priority(lines[0], lines[1], lines[2])
            lines = []
            line_number = 1
        else:
            line_number += 1

    print(priority_sum)
    f.close()

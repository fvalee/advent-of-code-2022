def calculate_priority(c1, c2):
    set_c1 = set(c1)
    set_c2 = set(c2)

    common = set_c1 & set_c2
    item = next(iter(common))

    return ord(item) - 96 if item.islower() else ord(item) - 38


if __name__ == '__main__':
    f = open("../input.txt", "r")

    priority_sum = 0
    for line in f:
        line = line.strip()
        compartment_1 = slice(0, len(line)//2)
        compartment_2 = slice(len(line)//2, len(line))
        priority_sum += calculate_priority(line[compartment_1], line[compartment_2])

    print(priority_sum)
    f.close()

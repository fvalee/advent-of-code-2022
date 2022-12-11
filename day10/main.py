signal_strength = 0
crt = ["."] * 240


def check(c, register):
    global signal_strength
    if c in (20, 60, 100, 140, 180, 220):
        signal_strength += c * register
    if (c - 1) % 40 in (x - 1, x, x + 1):
        crt[c] = "#"


if __name__ == '__main__':
    f = open("input.txt", "r")
    x = 1
    cycle = 0

    for line in f:
        line = line.strip().split()
        if line[0] == "noop":
            cycle += 1
            check(cycle, x)
        else:
            cycle += 1
            check(cycle, x)
            cycle += 1
            check(cycle, x)
            x += int(line[1])

    print(signal_strength)
    for i in range(240):
        print(crt[i], end="")
        if i % 40 == 0:
            print()

    f.close()

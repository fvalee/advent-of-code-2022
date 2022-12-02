def calculate_points(opponent, player):
    op_entry = [value for key, value in rules.items() if opponent in key][0]
    pl_entry = [value for key, value in rules.items() if player in key][0]

    if pl_entry is op_entry:
        return pl_entry.get("points") + round_outcome.get("draw")
    elif opponent in pl_entry.get("beats"):
        return pl_entry.get("points") + round_outcome.get("win")
    else:
        return pl_entry.get("points") + round_outcome.get("loss")


if __name__ == '__main__':
    f = open("../input.txt", "r")

    rules = {
        "AX": {"beats": "CZ", "points": 1},
        "BY": {"beats": "AX", "points": 2},
        "CZ": {"beats": "BY", "points": 3}
    }
    round_outcome = {"win": 6, "draw": 3, "loss": 0}

    total_points = 0
    for line in f:
        col = line.strip().split(" ")
        total_points += calculate_points(col[0], col[1])

    print(total_points)
    f.close()

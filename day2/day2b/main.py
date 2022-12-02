def calculate_points(opponent, outcome):
    op_entry = [value for key, value in rules.items() if opponent in key][0]
    return rules[op_entry.get(outcome)].get("points") + round_outcome.get(outcome)


if __name__ == '__main__':
    f = open("../input.txt", "r")

    # If A is played, in order for X to happen, player needs to play C
    rules = {
        "A": {"X": "C", "Y": "A", "Z": "B", "points": 1},
        "B": {"X": "A", "Y": "B", "Z": "C", "points": 2},
        "C": {"X": "B", "Y": "C", "Z": "A", "points": 3}
    }
    round_outcome = {"Z": 6, "Y": 3, "X": 0}

    total_points = 0
    for line in f:
        col = line.strip().split(" ")
        total_points += calculate_points(col[0], col[1])

    print(total_points)
    f.close()

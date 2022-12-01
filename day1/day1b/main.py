if __name__ == '__main__':
    f = open("../input.txt", "r")

    all_calories = []
    current_calories_sum = 0
    for line in f:
        if line != "\n":
            current_calories_sum += int(line)
        else:
            all_calories.append(current_calories_sum)
            current_calories_sum = 0

    total_sum = 0
    for i in range(3):
        total_sum += sorted(all_calories, reverse=True)[i]

    print(total_sum)
    f.close()

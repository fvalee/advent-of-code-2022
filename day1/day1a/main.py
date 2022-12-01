if __name__ == '__main__':
    f = open("../input.txt", "r")

    max_calories = 0
    current_calories_sum = 0
    for line in f:
        if line != "\n":
            current_calories_sum += int(line)
        else:
            if max_calories < current_calories_sum:
                max_calories = current_calories_sum
            current_calories_sum = 0

    print(max_calories)
    f.close()

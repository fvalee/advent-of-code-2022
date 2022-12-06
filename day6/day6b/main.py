if __name__ == '__main__':
    f = open("../input.txt", "r")

    buffer = ""
    last_loaded_character = 0
    for line in f:
        for char in line:
            last_loaded_character += 1
            if last_loaded_character < 15:
                buffer += char
            else:
                buffer = buffer[1:] + char
                if len(buffer) == len(set(buffer)):
                    break

    print(last_loaded_character)
    f.close()

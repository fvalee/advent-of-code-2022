if __name__ == '__main__':
    f = open("../input.txt", "r")

    # Retrieve the first part of the input file, with stack configuration
    config_lines = []
    for line in f:
        if line == "\n":
            break
        config_lines.append(line.strip())

    # Initialize N stacks
    num_of_stacks = config_lines.pop().split(" ")[-1]
    stack = {}
    for i in range(int(num_of_stacks)):
        stack[i] = []

    # For each config line (bottom to top), add elements to their respective stacks
    while len(config_lines) > 0:
        line = config_lines.pop()
        j = 0
        stack_number = 1
        for i in range(3, len(line) + 1, 4):
            stack_element = line[j:i]
            if stack_element != "   ":
                stack[stack_number - 1].append(stack_element[1])
            j = i + 1
            stack_number += 1

    # For the remainder of the file, read lines and move items between stacks
    for line in f:
        line = line.split(" ")
        for n in range(int(line[1])):
            to_move = stack[int(line[3]) - 1].pop()
            stack[int(line[5]) - 1].append(to_move)

    # Read the first items in all stacks to get the puzzle answer
    on_top_of_stacks = ""
    for i in range(int(num_of_stacks)):
        on_top_of_stacks += stack[i].pop()

    print(on_top_of_stacks)
    f.close()

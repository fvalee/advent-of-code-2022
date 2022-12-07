current_folder = ""


def change_directory(dir_name):
    global current_folder
    if dir_name == "/":
        current_folder = "/"
    elif dir_name == "..":
        current_folder = "/".join(current_folder.split("/")[0:-1])
        if current_folder == "":
            current_folder = "/"
    else:
        current_folder += dir_name if current_folder == "/" else "/" + dir_name


if __name__ == '__main__':
    f = open("input.txt", "r")

    directories = {}
    for line in f:
        line = line.strip().split()
        if line[0] == "$" and line[1] == "cd":
            change_directory(line[2])
            if directories.get(current_folder) is None:
                directories[current_folder] = 0
        elif line[0] == "$" and line[1] == "ls":
            while True:
                try:
                    line = next(f).strip().split()
                    if line[0] == "$":
                        change_directory(line[2])
                        if directories.get(current_folder) is None:
                            directories[current_folder] = 0
                        break
                    elif line[0] == "dir":
                        continue
                    else:
                        directories[current_folder] += int(line[0])
                except StopIteration:
                    break

    deep_directory = {}
    for current_dir in directories:
        deep_directory[current_dir] = 0
        for d in directories:
            if d.startswith(current_dir):
                deep_directory[current_dir] += directories[d]

    sum_of_dirs_less_eq_100k = 0
    size_of_dir_to_delete = 70_000_000
    total_disk_space = 70_000_000
    required_disk_space = 30_000_000
    min_to_delete = required_disk_space - (total_disk_space - deep_directory["/"])

    for d in deep_directory:
        if deep_directory[d] <= 100_000:
            sum_of_dirs_less_eq_100k += deep_directory[d]
        if size_of_dir_to_delete > deep_directory[d] > min_to_delete:
            size_of_dir_to_delete = deep_directory[d]

    print(sum_of_dirs_less_eq_100k)
    print(size_of_dir_to_delete)
    f.close()

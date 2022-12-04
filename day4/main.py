if __name__ == '__main__':
    f = open("input.txt", "r")

    fully_contained_count = 0
    overlap_count = 0
    for line in f:
        pair = line.strip().split(",")
        boundary_1 = pair[0].split("-")
        boundary_2 = pair[1].split("-")
        set_1 = set(range(int(boundary_1[0]), int(boundary_1[1]) + 1))
        set_2 = set(range(int(boundary_2[0]), int(boundary_2[1]) + 1))
        fully_contained_count += 1 if set_1.issubset(set_2) or set_1.issuperset(set_2) else 0
        overlap_count += 1 if len(set_1.intersection(set_2)) > 0 else 0

    print(fully_contained_count)
    print(overlap_count)
    f.close()

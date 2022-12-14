import networkx as nx


def char_value(c):
    val = ord(c)
    if c == "S":
        val = ord("a")
    if c == "E":
        val = ord("z")
    return val


def get_coordinate(x, y, c):
    val = str(x) + "," + str(y)
    if c == "S":
        val = "S"
    if c == "E":
        val = "E"
    return val


if __name__ == '__main__':
    f = open("input.txt", "r")
    data = []
    for line in f:
        data.append(list(line.strip()))
    f.close()

    graph = nx.DiGraph()

    rows = len(data)
    cols = len(data[0])

    for i in range(rows):
        for j in range(cols):
            current = get_coordinate(i, j, data[i][j])
            char_current = char_value(data[i][j])
            graph.add_node(current)

            if j < (cols - 1):  # RIGHT
                _right = get_coordinate(i, j + 1, data[i][j + 1])
                char_right = char_value(data[i][j + 1])
                char_dist = char_current - char_right
                if char_dist >= -1:
                    graph.add_edge(current, _right)
            if i < (rows - 1):  # DOWN
                _down = get_coordinate(i + 1, j, data[i + 1][j])
                char_down = char_value(data[i + 1][j])
                char_dist = char_current - char_down
                if char_dist >= -1:
                    graph.add_edge(current, _down)
            if j != 0:  # LEFT
                _left = get_coordinate(i, j - 1, data[i][j - 1])
                char_left = char_value(data[i][j - 1])
                char_dist = char_current - char_left
                if char_dist >= -1:
                    graph.add_edge(current, _left)
            if i != 0:  # UP
                _up = get_coordinate(i - 1, j, data[i - 1][j])
                char_up = char_value(data[i - 1][j])
                char_dist = char_current - char_up
                if char_dist >= -1:
                    graph.add_edge(current, _up)

    min_path = len(nx.dijkstra_path(graph, "S", "E")) - 1
    print(min_path)

    for i in range(rows):
        for j in range(cols):
            char_current = char_value(data[i][j])
            if char_current == ord("a"):
                try:
                    current = get_coordinate(i, j, data[i][j])
                    path_to_end = len(nx.dijkstra_path(graph, current, "E")) - 1
                    if path_to_end < min_path:
                        min_path = path_to_end
                except:
                    pass
    print(min_path)

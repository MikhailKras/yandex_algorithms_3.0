def get_sort_list_vertex(adj_list, start):
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in adj_list[vertex]:
            stack.append(neighbor)

    return len(path), sorted(path)


if __name__ == '__main__':
    n_inp, m_inp = tuple(map(int, input().split()))
    adj_list_inp = [[] for _ in range(n_inp + 1)]


    class Edge:
        def __init__(self, two_vertexes: tuple):
            self.two_vertexes = two_vertexes

        def get_first_vertex(self) -> int:
            return self.two_vertexes[0]

        def get_second_vertex(self) -> int:
            return self.two_vertexes[1]

    for _ in range(m_inp):
        edge: Edge = Edge(tuple(map(int, input().split())))
        adj_list_inp[edge.get_first_vertex()].append(edge.get_second_vertex())
        adj_list_inp[edge.get_second_vertex()].append(edge.get_first_vertex())

    res = get_sort_list_vertex(adj_list_inp, 1)
    print(res[0])
    print(*res[1])




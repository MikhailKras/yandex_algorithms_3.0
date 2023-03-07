import time
cur_time_while = 0
cur_time_extend_append = 0
cur_time_if = 0


def get_components(n, adj_list):
    global cur_time_while
    global cur_time_extend_append
    global cur_time_if
    vertexes = set(range(1, n + 1))
    visited = {vert: False for vert in vertexes}
    components = []
    for vertex in vertexes:

        start_time_if = time.process_time()
        if not visited[vertex]:
            stack = [vertex]
            path = []
            cur_time_if += time.process_time() - start_time_if

            start_time_while = time.process_time()
            while stack:
                vertex = stack.pop()
                if vertex in path:
                    continue
                visited[vertex] = True
                path.append(vertex)
                for neighbor in adj_list[vertex]:
                    stack.append(neighbor)
            cur_time_while += time.process_time() - start_time_while

            start_time_extend_append = time.process_time()
            components.append([len(path), path])
            cur_time_extend_append += time.process_time() - start_time_extend_append

    print(f'{cur_time_while = }, {cur_time_extend_append = }, {cur_time_if = }')
    return len(components), components


if __name__ == '__main__':
    n_inp, m_inp = tuple(map(int, input().split()))
    adj_list_inp = [[] for _ in range(n_inp + 1)]


    class Edge:
        def __init__(self, two_vertexes: tuple):
            self.first_vertex = two_vertexes[0]
            self.second_vertex = two_vertexes[1]

    for _ in range(m_inp):
        edge: Edge = Edge(tuple(map(int, input().split())))
        adj_list_inp[edge.first_vertex].append(edge.second_vertex)
        adj_list_inp[edge.second_vertex].append(edge.first_vertex)
    res = get_components(n_inp, adj_list_inp)
    print(res[0])
    for amount_vertex, component in res[1]:
        print(amount_vertex)
        print(*component)




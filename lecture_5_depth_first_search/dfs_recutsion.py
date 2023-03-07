path = []


def get_dfs_solution_with_recursion(adj_list, now, visited):
    if not visited[now]:
        visited[now] = True
        for neighbor in adj_list[now]:
            get_dfs_solution_with_recursion(adj_list, neighbor, visited)
        path.append(now)


if __name__ == '__main__':
    class Edge:
        def __init__(self, two_vertexes: tuple):
            self.first_vertex = two_vertexes[0]
            self.second_vertex = two_vertexes[1]
    n_inp, m_inp = tuple(map(int, input().split()))
    adj_list_inp = [[] for _ in range(n_inp + 1)]
    for i in range(m_inp):
        edge = Edge(tuple(map(int, input().split())))
        adj_list_inp[edge.first_vertex].append(edge.second_vertex)
        adj_list_inp[edge.second_vertex].append(edge.first_vertex)
    visited_inp = {vx: False for vx in range(1, n_inp + 1)}
    get_dfs_solution_with_recursion(adj_list_inp, 1, visited_inp)
    print(path[::-1])

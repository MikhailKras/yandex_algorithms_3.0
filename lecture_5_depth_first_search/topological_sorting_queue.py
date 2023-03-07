from collections import deque


def topological_sort(adj_list):
    n = len(adj_list)
    in_degree = [0] * n
    for node in range(n):
        for neighbor in adj_list[node]:
            in_degree[neighbor] += 1

    queue = deque(node for node in range(n) if in_degree[node] == 0)
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == n:
        return result[1:]
    else:
        return [-1]


if __name__ == '__main__':
    class Edge:
        def __init__(self, two_vertexes: tuple):
            self.start_vertex = two_vertexes[0]
            self.end_vertex = two_vertexes[1]

    n_inp, m_inp = tuple(map(int, input().split()))
    adj_list_inp = [set() for _ in range(n_inp + 1)]
    for _ in range(m_inp):
        edge = Edge(tuple(map(int, input().split())))
        adj_list_inp[edge.start_vertex].add(edge.end_vertex)
    print(*topological_sort(adj_list_inp))

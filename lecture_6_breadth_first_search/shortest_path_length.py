from collections import deque


def get_min_length(adj_matrix, start_vertex, end_vertex):
    start_vertex -= 1
    end_vertex -= 1
    visited = {vertex: -1 for vertex in range(len(adj_matrix))}
    queue_vertexes = deque((start_vertex, ))
    visited[start_vertex] = 0
    while queue_vertexes:
        cur_vertex = queue_vertexes.popleft()
        if cur_vertex == end_vertex:
            return visited[end_vertex]
        for neighbor, is_adj in enumerate(adj_matrix[cur_vertex]):
            if is_adj and visited[neighbor] == -1:
                queue_vertexes.append(neighbor)
                visited[neighbor] = visited[cur_vertex] + 1
    return -1


if __name__ == '__main__':
    n_inp = int(input())
    adj_matrix_inp = []
    for i in range(n_inp):
        adj_matrix_inp.append(list(map(int, input().split())))
    start_vertex_inp, end_vertex_inp = tuple(map(int, input().split()))
    print(get_min_length(adj_matrix_inp, start_vertex_inp, end_vertex_inp))

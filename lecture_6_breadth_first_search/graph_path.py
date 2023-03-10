from collections import deque


def get_min_length(adj_matrix, start_vertex, end_vertex):
    start_vertex -= 1
    end_vertex -= 1
    visited = {vertex: {'length': -1, 'parent': -1} for vertex in range(len(adj_matrix))}
    queue_vertexes = deque((start_vertex, ))
    visited[start_vertex]['length'] = 0
    while queue_vertexes:
        cur_vertex = queue_vertexes.popleft()

        if cur_vertex == end_vertex:
            path = []
            while cur_vertex != -1:
                path.append(cur_vertex)
                cur_vertex = visited[cur_vertex]['parent']
            return visited[end_vertex]['length'], list(map(lambda x: x + 1, path[::-1]))

        for neighbor, is_adj in enumerate(adj_matrix[cur_vertex]):
            if is_adj and visited[neighbor]['length'] == -1:
                queue_vertexes.append(neighbor)
                visited[neighbor]['length'] = visited[cur_vertex]['length'] + 1
                visited[neighbor]['parent'] = cur_vertex
    return -1


if __name__ == '__main__':
    n_inp = int(input())
    adj_matrix_inp = []
    for i in range(n_inp):
        adj_matrix_inp.append(list(map(int, input().split())))
    start_vertex_inp, end_vertex_inp = tuple(map(int, input().split()))
    res = get_min_length(adj_matrix_inp, start_vertex_inp, end_vertex_inp)
    if isinstance(res, tuple):
        length = res[0]
        path = res[1]
        if len(path) == 1:
            path = []
        print(length)
        print(*path)
    else:
        print(res)

from collections import deque


def get_sum_length(n, m, s, t, start_coords):
    s -= 1
    t -= 1

    def get_all_neighbors(x, y):
        neighbors = [(x - 2, y - 1), (x - 2, y + 1), (x + 2, y - 1), (x + 2, y + 1),
                     (x - 1, y - 2), (x - 1, y + 2), (x + 1, y - 2), (x + 1, y + 2)]
        return {(nx, ny) for nx, ny in neighbors if 0 <= nx < n and 0 <= ny < m}

    visited = set()
    queue = deque([(s, t, 0)])  # (x, y, level)
    res = 0
    start_coords_visited = {start_coord: False for start_coord in start_coords}
    while queue and not all(start_coords_visited.values()):
        x, y, level = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) in start_coords_visited:
            if not start_coords_visited[(x, y)]:
                start_coords_visited[(x, y)] = True
                res += level
        queue.extend((nx, ny, level + 1) for nx, ny in get_all_neighbors(x, y))

    if not all(start_coords_visited.values()):
        return -1
    else:
        return res


if __name__ == '__main__':
    n_inp, m_inp, s_inp, t_inp, q_inp = tuple(map(int, input().split()))
    start_coords_inp = []
    for _ in range(q_inp):
        start_coords_inp.append(tuple(map(int, input().split())))
    start_coords_inp = list(map(lambda x: (x[0] - 1, x[1] - 1), start_coords_inp))
    print(get_sum_length(n_inp, m_inp, s_inp, t_inp, start_coords_inp))

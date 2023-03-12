from collections import deque


def get_min_length(blocks, start_pos, n):

    def get_all_neighbors(x, y, z):
        dx = [0, 0, -1, 1, 0, 0]
        dy = [-1, 1, 0, 0, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]
        return [(x + nx, y + ny, z + nz) for nx, ny, nz in zip(dx, dy, dz)
                if (0 <= x + nx < n and 0 <= y + ny < n and 0 <= z + nz < n) and blocks[x + nx][y + ny][z + nz] == '.']

    length = 0
    first_block = (*start_pos, length)
    queue = deque([first_block])
    visited = set()
    while queue:
        x_cur, y_cur, z_cur, length_cur = queue.popleft()
        if x_cur == 0:
            return length_cur
        neighbors = get_all_neighbors(x_cur, y_cur, z_cur)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((*neighbor, length_cur + 1))
                visited.add(neighbor)


if __name__ == '__main__':
    n_inp = int(input())
    blocks_inp = [[] for _ in range(n_inp)]
    start_pos_inp = None
    for x in range(n_inp):
        for y in range(n_inp + 1):
            line_list = list(input())
            if line_list:
                blocks_inp[x].append(line_list)
            if 'S' in line_list:
                for z in range(n_inp):
                    if blocks_inp[x][y - 1][z] == 'S':
                        start_pos_inp = (x, y - 1, z)

    print(get_min_length(blocks_inp, start_pos_inp, n_inp))

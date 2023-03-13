from typing import List

from collections import deque


def get_min_transfers(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        input_lines_list: List[str] = list(map(lambda x: x.replace('\n', ''), file.readlines()))
    n = int(input_lines_list.pop(0))
    m = int(input_lines_list.pop(0))
    metro_lines = []
    for _ in range(m):
        metro_lines.append(set(map(int, input_lines_list.pop(0).split()[1:])))
    start_station, end_station = tuple(map(int, input_lines_list.pop(0).split()))
    starts, ends = [], []
    for line_number in range(m):
        if start_station in metro_lines[line_number]:
            starts.append(line_number)
        if end_station in metro_lines[line_number]:
            ends.append(line_number)

    adj_list = [set() for _ in range(m)]
    for line_a in range(m):
        for line_b in range(line_a, m):
            if metro_lines[line_a].intersection(metro_lines[line_b]):
                adj_list[line_b].add(line_a)
                adj_list[line_a].add(line_b)

    visited = {line: -1 for line in range(m)}
    for line in visited:
        if line in starts:
            visited[line] = 0

    queue = deque(starts)
    while queue:
        cur_line = queue.popleft()
        for neighbor in adj_list[cur_line]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[cur_line] + 1
                queue.append(neighbor)

    min_end = visited[ends[0]]
    for end in ends[1:]:
        if visited[end] < min_end:
            min_end = visited[end]

    return min_end


if __name__ == '__main__':
    file_name_inp = 'input.txt'
    print(get_min_transfers(file_name_inp))

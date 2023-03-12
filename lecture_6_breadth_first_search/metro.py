from collections import deque


def get_min_transfers(adj_list, metro_line_numbers, start_station, end_station):
    transfers_list = [-1 for _ in range(len(adj_list))]
    transfers_list[start_station] = 0
    queue = deque([(start_station, metro_line_numbers[start_station])])
    visited = set()
    while queue:
        cur_station, cur_lines = queue.popleft()
        for neighbor in adj_list[cur_station]:
            neighbor_lines = set(metro_line_numbers[neighbor])
            used_lines = cur_lines.intersection(neighbor_lines)
            cur_transfers = transfers_list[cur_station]
            if not used_lines:
                cur_transfers += 1
                used_lines = neighbor_lines.intersection(metro_line_numbers[cur_station])
            if (neighbor, tuple(used_lines)) in visited:
                continue
            if transfers_list[neighbor] == -1 or (cur_transfers < transfers_list[neighbor]):
                transfers_list[neighbor] = cur_transfers
            visited.add((neighbor, tuple(used_lines)))
            queue.append((neighbor, used_lines))
    if not metro_line_numbers[start_station].intersection(metro_line_numbers[end_station]) and transfers_list[end_station] == 0:
        transfers_list[end_station] += 1
    return transfers_list[end_station]


if __name__ == '__main__':
    n_inp = int(input())
    m_inp = int(input())
    adj_list_inp = [[] for _ in range(n_inp + 1)]
    metro_line_numbers_inp = [set() for _ in range(n_inp + 1)]
    num_line = 0
    for i in range(m_inp):
        metro_line_inp = list(map(int, input().split()))[1:]
        num_line += 1
        for j in range(len(metro_line_inp)):
            if j + 1 < len(metro_line_inp):
                adj_list_inp[metro_line_inp[j]].append(metro_line_inp[j + 1])
                adj_list_inp[metro_line_inp[j + 1]].append(metro_line_inp[j])
            metro_line_numbers_inp[metro_line_inp[j]].add(num_line)
    start_station_inp, end_station_inp = tuple(map(int, input().split()))
    # print(metro_line_numbers_inp[15], metro_line_numbers_inp[start_station_inp], metro_line_numbers_inp[end_station_inp])
    print(get_min_transfers(adj_list_inp, metro_line_numbers_inp, start_station_inp, end_station_inp))



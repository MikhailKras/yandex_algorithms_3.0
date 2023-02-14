def get_sum_elem_from_rect(matrix, reqs, n, m):
    prefix_matrix = [[0] for _ in range(n)]
    for x in range(n):
        for y in range(1, m + 1):
            prefix_matrix[x].append(matrix[x][y-1] + prefix_matrix[x][y-1])
    sums = [0 for _ in range(len(reqs))]
    for i, req in enumerate(reqs):
        x1, y1, x2, y2 = list(map(lambda elem: elem-1, req))
        for row in range(x1, x2 + 1):
            sums[i] += prefix_matrix[row][y2+1] - prefix_matrix[row][y1]
    return sums


if __name__ == '__main__':
    in_n, in_m, in_k = list(map(int, input().split()))
    in_matrix = []
    for i in range(in_n):
        in_matrix.append(list(map(int, input().split())))
    in_reqs = []
    for i in range(in_k):
        in_reqs.append(list(map(int, input().split())))
    print(*get_sum_elem_from_rect(in_matrix, in_reqs, in_n, in_m), sep='\n')


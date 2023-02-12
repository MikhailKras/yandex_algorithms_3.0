def get_saper(n, m, mines_coords):
    field = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if [i, j] in mines_coords:
                field[i][j] = '*'
                if i - 1 >= 0 and j - 1 >= 0:
                    if field[i - 1][j - 1] != '*':
                        field[i-1][j-1] += 1
                if j - 1 >= 0:
                    if field[i][j-1] != '*':
                        field[i][j-1] += 1
                if i + 1 < n and j - 1 >= 0:
                    if field[i+1][j-1] != '*':
                        field[i + 1][j-1] += 1
                if i + 1 < n:
                    if field[i+1][j] != '*':
                        field[i + 1][j] += 1
                if i + 1 < n and j + 1 < m:
                    if field[i+1][j+1] != '*':
                        field[i + 1][j + 1] += 1
                if j + 1 < m:
                    if field[i][j+1] != '*':
                        field[i][j + 1] += 1
                if i - 1 >= 0 and j + 1 < m:
                    if field[i-1][j+1] != '*':
                        field[i - 1][j + 1] += 1
                if i - 1 >= 0:
                    if field[i-1][j] != '*':
                        field[i-1][j] += 1
    for item in field:
        print(*item)


if __name__ == '__main__':
    in_n, in_m, k = list(map(int, input().split()))
    in_mines_coords = []
    for _ in range(k):
        coord = list(map(lambda x: int(x) - 1, input().split()))
        in_mines_coords.append(coord)
    get_saper(in_n, in_m, in_mines_coords)

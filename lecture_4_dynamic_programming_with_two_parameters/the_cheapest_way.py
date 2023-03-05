def get_min_weight(n, m, field):
    dp = [[float('inf') if y == 0 or x == 0 else 0 for y in range(m+1)] for x in range(n+1)]
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if x == y == 1:
                dp[x][y] = field[x - 1][y - 1]
            else:
                dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + field[x - 1][y - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    n_inp, m_inp = tuple(map(int, input().split()))
    field_inp = []
    for _ in range(n_inp):
        field_inp.append(list(map(int, input().split())))
    print(get_min_weight(n_inp, m_inp, field_inp))

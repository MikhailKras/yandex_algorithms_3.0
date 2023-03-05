def get_amount_ways(n, m):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if dp[i][j] != 0:
                if i + 2 < n and j + 1 < m:
                    dp[i + 2][j + 1] += dp[i][j]
                if i + 1 < n and j + 2 < m:
                    dp[i + 1][j + 2] += dp[i][j]
    return dp[-1][-1]


if __name__ == '__main__':
    n_inp, m_inp = tuple(map(int, input().split()))
    print(get_amount_ways(n_inp, m_inp))

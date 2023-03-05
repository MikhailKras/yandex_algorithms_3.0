def get_lcs(n, first_seq_list, m, second_seq_list):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first_seq_list[i - 1] == second_seq_list[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res_seq = []
    x, y = n, m
    while x > 0 and y > 0:
        if first_seq_list[x - 1] == second_seq_list[y - 1]:
            x -= 1
            y -= 1
            res_seq.append(first_seq_list[x])
        elif dp[x][y] == dp[x - 1][y]:
            x -= 1
        else:
            y -= 1
    return res_seq[::-1]


if __name__ == '__main__':
    n_inp = int(input())
    first_seq_list_inp = input().split()
    m_inp = int(input())
    second_seq_list_inp = input().split()
    print(*get_lcs(n_inp, first_seq_list_inp, m_inp, second_seq_list_inp))

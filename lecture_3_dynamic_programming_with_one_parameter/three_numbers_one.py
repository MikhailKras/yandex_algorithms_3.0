def get_amount_seqs_without_three_numbers_one_on_row(n):
    dp = [-1] * 36
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


if __name__ == '__main__':
    input_n = int(input())
    print(get_amount_seqs_without_three_numbers_one_on_row(input_n))

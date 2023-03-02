def get_amount_path_variants_from_one_to_n(n, k):
    dp = [-1] * 31
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        n_minus_k = i - k
        if n_minus_k < 0:
            n_minus_k = 0
        dp[i] = sum(dp[n_minus_k:i])
    return dp[n - 1]


if __name__ == '__main__':
    input_n, input_k = tuple(map(int, input().split()))
    print(get_amount_path_variants_from_one_to_n(input_n, input_k))

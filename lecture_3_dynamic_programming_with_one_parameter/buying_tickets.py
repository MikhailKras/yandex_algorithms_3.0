def get_min_buying_time(n, a, b, c):
    dp = [-1] * n
    dp[0] = a[0]
    if n > 1:
        dp[1] = min(a[0] + a[1], b[0])
    if n > 2:
        dp[2] = min(a[0] + a[1] + a[2], a[0] + b[1], c[0], b[0] + a[2])
    for i in range(3, n):
        dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1], dp[i - 3] + c[i - 2])
    return dp[-1]


if __name__ == '__main__':
    input_n = int(input())
    input_a, input_b, input_c = [], [], []
    for j in range(input_n):
        abc = list(map(int, input().split()))
        input_a.append(abc[0])
        input_b.append(abc[1])
        input_c.append(abc[2])
    print(get_min_buying_time(input_n, input_a, input_b, input_c))

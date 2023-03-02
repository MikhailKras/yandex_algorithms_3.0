def get_min_length(coords):
    coords = sorted(coords)
    dp = [-1] * len(coords)
    dp[0] = 0
    dp[1] = coords[1] - coords[0]
    if len(coords) > 2:
        dp[2] = coords[2] - coords[0]
    for i in range(3, len(dp)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + coords[i] - coords[i - 1]
    return dp[-1]


if __name__ == '__main__':
    n_input = int(input())
    coords_input = list(map(int, input().split()))
    print(get_min_length(coords_input))

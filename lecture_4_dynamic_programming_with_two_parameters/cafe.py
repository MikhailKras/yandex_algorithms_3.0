def get_results(n, costs):
    if n == 0:
        return 0, 0, 0, []
    dp = [[float('inf') if x == 0 else 0 for y in range(n)] for x in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for k in range(n):
            if costs[i - 1] > 100:
                if k - 1 >= 0:
                    without_coupon = dp[i - 1][k - 1] + costs[i - 1]
                else:
                    without_coupon = dp[i - 1][k] + costs[i - 1]
            else:
                without_coupon = dp[i - 1][k] + costs[i - 1]
            if k + 1 < n:
                with_coupon = dp[i - 1][k + 1]
            else:
                with_coupon = float('inf')
            dp[i][k] = min(without_coupon, with_coupon)

    min_sum = dp[-1][n - 1]
    coupons_remains_ans = n - 1
    for coupons, sum_value in zip(range(n - 1, -1, -1), dp[-1][::-1]):
        if sum_value < min_sum:
            min_sum = sum_value
            coupons_remains_ans = coupons

    coupons_remains = coupons_remains_ans
    day_number = n
    day_numbers_with_coupons = []
    with_coupon = float('inf')
    while day_number > 0:
        if costs[day_number - 1] > 100:
            if coupons_remains + 1 < n:
                with_coupon = dp[day_number - 1][coupons_remains + 1]
            if dp[day_number][coupons_remains] == with_coupon and with_coupon != float('inf'):
                day_numbers_with_coupons.append(day_number)
                coupons_remains += 1
            else:
                if coupons_remains - 1 >= 0:
                    coupons_remains -= 1
        else:
            if coupons_remains + 1 < n:
                with_coupon = dp[day_number - 1][coupons_remains + 1]
            if dp[day_number][coupons_remains] == with_coupon and with_coupon != float('inf'):
                day_numbers_with_coupons.append(day_number)
                coupons_remains += 1
        day_number -= 1
    if len(costs) == 1 and costs[0] > 100:
        coupons_remains_ans += 1
    return min_sum, coupons_remains_ans, len(day_numbers_with_coupons), day_numbers_with_coupons[::-1]


if __name__ == '__main__':
    n_inp = int(input())
    costs_inp = []
    for _ in range(n_inp):
        costs_inp.append(int(input()))
    res = get_results(n_inp, costs_inp)
    print(res[0])
    print(*(res[1], res[2]))
    print(*res[3], sep='\n')

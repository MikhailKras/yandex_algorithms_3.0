def get_min_amount_operations_and_path(n):
    dp = [0] * (10 ** 6 + 1)
    for i in range(2, n + 1):
        list_compare = [dp[i - 1]]
        if i % 2 == 0:
            list_compare.append(dp[i // 2])
        if i % 3 == 0:
            list_compare.append(dp[i // 3])
        dp[i] = min(list_compare) + 1

    k = n
    path_num_list = [n]
    while k > 1:
        list_compare = [(dp[k - 1], k - 1)]
        if k % 2 == 0:
            list_compare.append((dp[k // 2], k // 2))
        if k % 3 == 0:
            list_compare.append((dp[k // 3], k // 3))
        min_value_tuple = min(list_compare, key=lambda x: x[0])
        path_num_list.append(min_value_tuple[1])
        k = min_value_tuple[1]

    return dp[n], path_num_list[::-1]


if __name__ == '__main__':
    input_n = int(input())
    amount_operations = get_min_amount_operations_and_path(input_n)[0]
    path_numbers_list = get_min_amount_operations_and_path(input_n)[1]
    print(amount_operations)
    print(*path_numbers_list)

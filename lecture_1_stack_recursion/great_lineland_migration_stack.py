def get_cities_list(avg_prices_list):
    avg_prices_enumerate_stack = []
    ans = [-1 for x in range(len(avg_prices_list))]
    for i, price in enumerate(avg_prices_list):
        if not avg_prices_enumerate_stack:
            avg_prices_enumerate_stack.append((i, price))
        elif price >= avg_prices_enumerate_stack[-1][1]:
            avg_prices_enumerate_stack.append((i, price))
        elif price < avg_prices_enumerate_stack[-1][1]:
            while avg_prices_enumerate_stack and price < avg_prices_enumerate_stack[-1][1]:
                ans[avg_prices_enumerate_stack[-1][0]] = i
                avg_prices_enumerate_stack.pop()
            else:
                avg_prices_enumerate_stack.append((i, price))
    return ans


if __name__ == '__main__':
    n = int(input())
    input_avg_prices_list = list(map(int, input().split()))
    print(*get_cities_list(input_avg_prices_list))

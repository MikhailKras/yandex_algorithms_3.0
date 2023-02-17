cities_list = []
num_rec = 0


def get_cities_list(avg_prices_list):
    # global cities_list
    global num_rec
    if len(avg_prices_list) == 1:
        print(-1, end=' ')
        return
    flag = 0
    for i in range(1, len(avg_prices_list)):
        if avg_prices_list[i] < avg_prices_list[0]:
            print(i + num_rec, end=' ')
            flag = 1
            break
    if not flag:
        print(-1, end=' ')
    num_rec += 1
    get_cities_list(avg_prices_list[1:])


if __name__ == '__main__':
    n = int(input())
    input_avg_prices_list = list(map(int, input().split()))
    get_cities_list(input_avg_prices_list)
    # print(*cities_list)

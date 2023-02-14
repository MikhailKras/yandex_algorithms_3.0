from datetime import datetime


def get_max_goodness(my_str, k_num):
    char_dct = {}
    max_goodness = 0
    k_cur = k_num
    end_index = 0
    for i in range(len(my_str)):
        char_dct[my_str[i]] = char_dct.get(my_str[i], 0) + 1
        if my_str[i] == my_str[0]:
            max_goodness += 1
        elif k_cur > 0:
            k_cur -= 1
            max_goodness += 1
        else:
            if i - 1 >= 0:
                end_index = i - 1
            break
    cur_goodness = 0
    for i in range(1, len(my_str)):
        char_dct[my_str[i-1]] -= 1
        cur_goodness = min(k_num + char_dct.get(my_str[i]), len(my_str) - i)

    print(char_dct, end_index)


if __name__ == '__main__':
    k = int(input())
    in_str = input()
    start = datetime.now()
    print(get_max_goodness(in_str, k))
    end = datetime.now()
    print(end - start)

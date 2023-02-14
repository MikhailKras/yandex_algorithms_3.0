from datetime import datetime


def calc_goodness(char, index, k_num, my_str):
    goodness_left = 0
    goodness_right = 0
    if index < len(my_str) // 2:
        k_cur = k_num
        for i in range(index, -1, -1):
            if my_str[i] == char:
                goodness_left += 1
            elif k_cur > 0:
                k_cur -= 1
                goodness_left += 1
            else:
                break
    elif index > len(my_str) // 2:
        k_cur = k_num
        for i in range(index, len(my_str)):
            if my_str[i] == char:
                goodness_right += 1
            elif k_cur > 0:
                k_cur -= 1
                goodness_right += 1
            else:
                break
    else:
        goodness_left = 0
        k_cur = k_num
        if index < len(my_str) // 2:
            for i in range(index, -1, -1):
                if my_str[i] == char:
                    goodness_left += 1
                elif k_cur > 0:
                    k_cur -= 1
                    goodness_left += 1
                else:
                    break
            goodness_right = 0
            k_cur = k_num
            for i in range(index, len(my_str)):
                if my_str[i] == char:
                    goodness_right += 1
                elif k_cur > 0:
                    k_cur -= 1
                    goodness_right += 1
                else:
                    break
    if goodness_left:
        return goodness_left
    else:
        return goodness_right


def get_max_goodness(my_str, k_num):
    max_goodness = 0
    for i in range(len(my_str)):
        cur_goodness = calc_goodness(my_str[i], i, k_num, my_str)
        if cur_goodness > max_goodness:
            max_goodness = cur_goodness
    return max_goodness


if __name__ == '__main__':
    k = int(input())
    in_str = input()
    start = datetime.now()
    print(get_max_goodness(in_str, k))
    end = datetime.now()
    print(end - start)

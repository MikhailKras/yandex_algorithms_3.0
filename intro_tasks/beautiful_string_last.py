def get_max_prettiness(my_str, k):
    max_prettiness = 0
    my_str_set = set(my_str)
    for cur_char in my_str_set:
        right_point = 0
        cur_k = k
        dropdown_char = cur_char
        for left_point in range(len(my_str)):
            if dropdown_char != cur_char:
                cur_k += 1
            while cur_k >= 0 and right_point < len(my_str):
                if my_str[right_point] != cur_char:
                    if cur_k == 0:
                        break
                    cur_k -= 1
                right_point += 1
            prettiness = right_point - left_point
            dropdown_char = my_str[left_point]
            if prettiness > max_prettiness:
                max_prettiness = prettiness
    return max_prettiness


if __name__ == '__main__':
    input_k = int(input())
    in_str = input()
    print(get_max_prettiness(in_str, input_k))

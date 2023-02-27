def get_vasya_place_num(n, k, petya_num_row, petya_num_col):
    petya_place_num = petya_num_row * 2
    if petya_num_col == 1:
        petya_place_num -= 1

    def place_num_to_row_col(place_num):
        if place_num % 2 == 0:
            return place_num // 2, 2
        else:
            return place_num // 2 + 1, 1

    vasya_place_num_front = petya_place_num - k
    vasya_place_num_back = petya_place_num + k
    vasya_row_col_front = place_num_to_row_col(vasya_place_num_front)
    vasya_row_col_back = place_num_to_row_col(vasya_place_num_back)
    if vasya_place_num_front >= 1 and vasya_place_num_back <= n:
        if abs(petya_num_row-vasya_row_col_back[0]) <= abs(petya_num_row-vasya_row_col_front[0]):
            return vasya_row_col_back
        else:
            return vasya_row_col_front
    elif vasya_place_num_front < 1 and vasya_place_num_back > n:
        return -1,
    elif vasya_place_num_front < 1:
        return vasya_row_col_back
    else:
        return vasya_row_col_front



if __name__ == '__main__':
    input_n = int(input())
    input_k = int(input())
    input_petya_num_row = int(input())
    input_petya_num_col = int(input())
    print(*get_vasya_place_num(input_n, input_k, input_petya_num_row, input_petya_num_col), sep=' ')

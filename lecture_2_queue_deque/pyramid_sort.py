def get_sorted_list_by_pyramid_sort(my_list, n):
    for i in range(n):
        parent_index = int((i - 1) / 2)
        if my_list[i] > my_list[parent_index]:
            cur_index = i
            while my_list[cur_index] > my_list[int((cur_index - 1) / 2)]:
                my_list[cur_index], my_list[int((cur_index - 1) / 2)] = my_list[int((cur_index - 1) / 2)], my_list[cur_index]
                cur_index = int((cur_index - 1) / 2)

    for i in range(n - 1, 0, -1):

        my_list[0], my_list[i] = my_list[i], my_list[0]

        parent_index = 0

        while True:
            left_son_index = 2 * parent_index + 1
            right_son_index = 2 * parent_index + 2
            son_index = left_son_index

            if (left_son_index < (i - 1) and
                    my_list[left_son_index] < my_list[right_son_index]):
                son_index = right_son_index

            if son_index < i and my_list[parent_index] < my_list[son_index]:
                my_list[parent_index], my_list[son_index] = my_list[son_index], my_list[parent_index]

            parent_index = son_index
            if son_index >= i:
                break


if __name__ == '__main__':
    input_n = int(input())
    input_list = list(map(int, input().split()))
    get_sorted_list_by_pyramid_sort(input_list, input_n)
    print(*input_list)

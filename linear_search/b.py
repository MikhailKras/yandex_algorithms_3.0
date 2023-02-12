def define_seq(lst):
    ans_list = ('CONSTANT', 'ASCENDING', 'WEAKLY ASCENDING', 'DESCENDING', 'WEAKLY DESCENDING', 'RANDOM')
    ans_dict = {key: 1 for key in ans_list}
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            ans_dict['ASCENDING'] -= 1
            ans_dict['DESCENDING'] -= 1
        elif lst[i] > lst[i + 1]:
            ans_dict['CONSTANT'] -= 1
            ans_dict['ASCENDING'] -= 1
            ans_dict['WEAKLY ASCENDING'] -= 1
        elif lst[i] < lst[i + 1]:
            ans_dict['CONSTANT'] -= 1
            ans_dict['DESCENDING'] -= 1
            ans_dict['WEAKLY DESCENDING'] -= 1
    for ans in ans_dict:
        if ans_dict[ans] > 0:
            return ans


if __name__ == '__main__':
    num = int(input())
    num_end = -2 * 10 ** 9
    in_list = []
    while num != num_end:
        in_list.append(num)
        num = int(input())
    print(define_seq(in_list))

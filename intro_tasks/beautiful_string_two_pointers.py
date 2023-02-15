def get_max_goodness(my_str, k_num):
    char_dict = {}
    for i, char in enumerate(my_str):
        if char not in char_dict:
            char_dict[char] = {'goodness_list': [], 'k': k_num, 'left': i, 'right': i}
            goodness = 0
        else:
            if i < char_dict[char]['right']:
                char_dict[char]['k'] += i - char_dict[char]['left'] - 2
                goodness = char_dict[char]['goodness_list'][-1] - char_dict[char]['left'] - 1
            else:
                char_dict[char]['k'] = k_num
                char_dict[char]['right'] = i
                goodness = 0
            char_dict[char]['left'] = i
        while (char_dict[char]['k'] > 0 and char_dict[char]['right'] < len(my_str)) or (char_dict[char]['k'] == 0 and char_dict[char]['right'] < len(my_str) and my_str[char_dict[char]['right']] == char):
            if my_str[char_dict[char]['right']] == char:
                goodness += 1
            else:
                goodness += 1
                char_dict[char]['k'] -= 1
            char_dict[char]['right'] += 1
        else:
            if char_dict[char]['k'] > 0 and char_dict[char]['left'] > 0:
                char_dict[char]['left'] -= 1
                while char_dict[char]['left'] > 0 and my_str[char_dict[char]['left']] != char and char_dict[char]['k'] > 0:
                    goodness += 1
                    char_dict[char]['k'] -= 1
                    char_dict[char]['left'] -= 1
        char_dict[char]['goodness_list'].append(goodness)
    max_goodness = 0
    for in_dict in char_dict.values():
        if max(in_dict['goodness_list']) > max_goodness:
            max_goodness = max(in_dict['goodness_list'])
    return max_goodness


if __name__ == '__main__':
    k = int(input())
    in_str = input()
    print(get_max_goodness(in_str, k))

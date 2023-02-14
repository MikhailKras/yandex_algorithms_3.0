def get_gistogram(chars):
    chars_dict = dict()
    for char in chars:
        chars_dict[char] = chars_dict.get(char, 0) + 1
    chars_dict_lattice = {key: ['#' for _ in range(value)] for key, value in chars_dict.items()}
    max_freq_char = max(chars_dict.values())
    for key, value in chars_dict.items():
        chars_dict_lattice[key].extend([' ' for _ in range(max_freq_char - value)])
        chars_dict_lattice[key].insert(0, key)
    sort_values = sorted(chars_dict_lattice.values())
    n = len(sort_values)
    m = len(sort_values[0])
    res = [[] for x in range(m)]
    for i in range(n):
        for j in range(m):
            res[j].append(sort_values[i][j])
    for i in res[::-1]:
        print(''.join(i))


if __name__ == '__main__':
    with open('input_gist.txt', encoding='utf-8') as file:
        lines = []
        for line in file:
            lines.append(''.join(line.strip().split()))
        all_chars = ''.join(lines)
    get_gistogram(all_chars)

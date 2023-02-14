def get_good_string(amounts):
    res = 0
    for i in range(len(amounts)-1):
        min_freq = min(amounts[i], amounts[i + 1])
        res += min_freq
    print(res)


if __name__ == '__main__':
    n = int(input())
    amounts_char = []
    for _ in range(n):
        amounts_char.append(int(input()))
    get_good_string(amounts_char)

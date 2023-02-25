def get_list_cards(diego_cards_list: list, p_list: list) -> list:
    diego_cards_sorted_set = sorted(set(diego_cards_list))
    res = []
    i = 0
    for p_card in p_list:
        i += 1
        if not i // 1000:
            print(i)
        if p_card <= diego_cards_sorted_set[0]:
            res.append(0)
            continue
        left = 0
        right = len(diego_cards_sorted_set) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if p_card > diego_cards_sorted_set[mid]:
                left = mid
            else:
                right = mid - 1
        res.append(left + 1)
    return res


if __name__ == '__main__':
    input_n = input()
    input_diego_cards_list = list(map(int, input().split()))
    input_k = input()
    input_p_list = list(map(int, input().split()))
    print(*get_list_cards(input_diego_cards_list, input_p_list), sep='\n')

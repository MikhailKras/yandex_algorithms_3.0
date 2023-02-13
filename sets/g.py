def get_amount_true_torts(tort_infos, n):
    tort_true_set = set()
    for info in tort_infos:
        if sum(info) == n - 1 and info[0] >= 0 and info[1] >= 0:
            tort_true_set.add(info)
    return len(tort_true_set)


if __name__ == '__main__':
    in_n = int(input())
    in_tort_infos = []
    for i in range(in_n):
        in_tort_infos.append(tuple(map(int, input().split())))
    print(get_amount_true_torts(in_tort_infos, in_n))

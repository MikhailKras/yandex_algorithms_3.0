def get_intersection(a, b):
    return sorted(set(a).intersection(set(b)))


if __name__ == '__main__':
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    print(*get_intersection(a_list, b_list))

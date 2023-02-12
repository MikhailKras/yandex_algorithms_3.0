def check_increasing(lst):
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    in_list = list(map(int, input().split()))
    print(check_increasing(in_list))

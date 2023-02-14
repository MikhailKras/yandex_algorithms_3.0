def get_amount_work_sys(my_sectors):
    works_sys = []
    for sys in my_sectors:
        for k in range(len(works_sys)):
            if works_sys[k][0][0] <= sys[0][0] <= works_sys[k][0][1] or works_sys[k][0][0] <= sys[0][1] <= works_sys[k][0][1] or sys[0][0] \
                    <= works_sys[k][0][0] <= sys[0][1] or sys[0][0] <= works_sys[k][0][1] <= sys[0][1]:
                works_sys[k][1] = -1
        works_sys.append(sys)
    return len(list(filter(lambda x: x[-1] != -1, works_sys)))


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    sectors = []
    for i in range(n):
        sector = tuple(map(int, input().split()))
        sectors.append([sector, i])
    print(get_amount_work_sys(sectors))

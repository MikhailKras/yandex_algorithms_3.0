def get_min_rectangle(coords):
    min_x = min_y = 10**9
    max_x = max_y = 0
    for x, y in coords:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

    print(*(min_x, min_y, max_x, max_y))


if __name__ == '__main__':
    k = int(input())
    in_coords = []
    for _ in range(k):
        in_coords.append(tuple(map(int, input().split())))
    get_min_rectangle(in_coords)

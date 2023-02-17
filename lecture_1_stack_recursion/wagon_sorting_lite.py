def check_wagon_seq(wagon_numbers):
    route_2 = []
    dead_end_stack = []
    while wagon_numbers:
        if not dead_end_stack:
            dead_end_stack.append(wagon_numbers.pop(0))
        elif wagon_numbers[0] < dead_end_stack[-1]:
            dead_end_stack.append(wagon_numbers.pop(0))
        else:
            while dead_end_stack and dead_end_stack[-1] < wagon_numbers[0]:
                if route_2 and dead_end_stack[-1] - route_2[-1] != 1:
                    return 'NO'
                route_2.append(dead_end_stack.pop())
    else:
        while dead_end_stack:
            if route_2 and dead_end_stack[-1] - route_2[-1] != 1:
                return 'NO'
            route_2.append(dead_end_stack.pop())
    return 'YES'


if __name__ == '__main__':
    n = int(input())
    input_wagon_numbers = list(map(int, input().split()))
    print(check_wagon_seq(input_wagon_numbers))

def get_client_time(a, b, c):
    time_to_seconds = lambda lst: lst[0] * 3600 + lst[1] * 60 + lst[2]
    a_sec, b_sec, c_sec = time_to_seconds(a), time_to_seconds(b), time_to_seconds(c)
    if a_sec > c_sec:
        c_sec += 24 * 60 * 60
    time_signal = (c_sec - a_sec + 1) // 2
    client_time_sec = b_sec + time_signal
    if client_time_sec >= 24 * 60 * 60:
        client_time_sec -= 24 * 60 * 60
    client_time_hour = client_time_sec // 3600
    client_time_min = (client_time_sec - client_time_hour * 3600) // 60
    client_time_seconds = client_time_sec - client_time_hour * 3600 - client_time_min * 60
    if len(str(client_time_hour)) == 1:
        client_time_hour = '0' + str(client_time_hour)
    if len(str(client_time_min)) == 1:
        client_time_min = '0' + str(client_time_min)
    if len(str(client_time_seconds)) == 1:
        client_time_seconds = '0' + str(client_time_seconds)
    return f'{client_time_hour}:{client_time_min}:{client_time_seconds}'


if __name__ == '__main__':
    in_a = list(map(int, input().split(':')))
    in_b = list(map(int, input().split(':')))
    in_c = list(map(int, input().split(':')))
    print(get_client_time(in_a, in_b, in_c))

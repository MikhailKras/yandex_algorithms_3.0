def get_responses_from_commands(commands: list[str]) -> list:
    heap_list = []
    responses = []
    for command in commands:
        if command == '1':
            ans = heap_list[0]
            heap_list[0] = heap_list[-1]
            item_index = 0
            while item_index * 2 + 2 < len(heap_list):
                max_son_index = item_index * 2 + 1
                if heap_list[item_index * 2 + 2] > heap_list[max_son_index]:
                    max_son_index = item_index * 2 + 2
                if heap_list[item_index] < heap_list[max_son_index]:
                    heap_list[item_index], heap_list[max_son_index] = heap_list[max_son_index], heap_list[item_index]
                    item_index = max_son_index
                else:
                    break
            heap_list.pop()
            responses.append(ans)
        else:
            heap_list.append(int(command.split()[-1]))
            item_index = len(heap_list) - 1
            while item_index > 0 and heap_list[item_index] > heap_list[(item_index - 1)//2]:
                heap_list[item_index], heap_list[(item_index - 1)//2] = heap_list[(item_index - 1)//2], heap_list[item_index]
                item_index = (item_index - 1)//2
    return responses


if __name__ == '__main__':
    n = int(input())
    input_commands = []
    for i in range(n):
        input_commands.append(input())
    print(*get_responses_from_commands(input_commands), sep='\n')

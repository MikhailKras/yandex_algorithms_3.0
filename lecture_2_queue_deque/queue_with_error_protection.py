def get_responses_from_commands(commands: list[str]):
    my_queue = []
    responses = []
    for command in commands:
        if 'push' in command:
            my_queue.append(command.split()[-1])
            responses.append('ok')
        elif command == 'pop':
            if my_queue:
                responses.append(my_queue.pop(0))
            else:
                responses.append('error')
        elif command == 'front':
            if my_queue:
                responses.append(my_queue[0])
            else:
                responses.append('error')
        elif command == 'size':
            responses.append(len(my_queue))
        elif command == 'clear':
            my_queue.clear()
            responses.append('ok')
        elif command == 'exit':
            responses.append('bye')
            return responses
    return responses


if __name__ == '__main__':
    with open('input.txt', encoding='utf-8') as file:
        input_commands = []
        for line in file.readlines():
            input_commands.append(line.replace('\n', ''))
    print(*get_responses_from_commands(input_commands), sep='\n')

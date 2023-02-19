def get_responses_from_commands(commands: list[str]):
    my_deque = []
    responses = []
    for command in commands:
        if 'push_front' in command:
            my_deque.insert(0, command.split()[-1])
            responses.append('ok')
        elif 'push_back' in command:
            my_deque.append(command.split()[-1])
            responses.append('ok')
        elif command == 'pop_front':
            if my_deque:
                responses.append(my_deque.pop(0))
            else:
                responses.append('error')
        elif command == 'pop_back':
            if my_deque:
                responses.append(my_deque.pop())
            else:
                responses.append('error')
        elif command == 'front':
            if my_deque:
                responses.append(my_deque[0])
            else:
                responses.append('error')
        elif command == 'back':
            if my_deque:
                responses.append(my_deque[-1])
            else:
                responses.append('error')
        elif command == 'size':
            responses.append(len(my_deque))
        elif command == 'clear':
            my_deque.clear()
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

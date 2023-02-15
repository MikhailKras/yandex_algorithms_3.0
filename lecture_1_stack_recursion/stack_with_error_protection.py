def get_responses_from_commands(commands):
    stack = []
    responses = []
    for command in commands:
        if 'push' in command:
            stack.append(command.split()[-1])
            responses.append('ok')
        elif command == 'pop':
            if stack:
                responses.append(stack.pop())
            else:
                responses.append('error')
        elif command == 'back':
            if stack:
                responses.append(stack[-1])
            else:
                responses.append('error')
        elif command == 'size':
            responses.append(len(stack))
        elif command == 'clear':
            stack.clear()
            responses.append('ok')
        elif command == 'exit':
            responses.append('bye')
            return responses
    return responses


if __name__ == '__main__':
    with open('input.txt', encoding='utf-8') as file:
        input_commands = []
        for input_command in file.readlines():
            input_commands.append(input_command.replace('\n', ''))
    print(*get_responses_from_commands(input_commands), sep='\n')

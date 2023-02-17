def check_bracket_seq(brackets):
    stack = []
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    opened = brackets_dict.values()
    closed = brackets_dict.keys()
    for bracket in brackets:
        if bracket in opened:
            stack.append(bracket)
        elif bracket in closed:
            if stack:
                if brackets_dict[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return 'no'
            else:
                return 'no'
    if stack:
        return 'no'
    return 'yes'


if __name__ == '__main__':
    input_brackets = input()
    print(check_bracket_seq(input_brackets))

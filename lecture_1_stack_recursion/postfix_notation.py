def get_result_from_expression(expression_list):
    stack = []
    for item in expression_list:
        if item.isdigit():
            stack.append(item)
        else:
            new_item = eval(f'{stack[-2]}{item}{stack[-1]}')
            stack.pop()
            stack.pop()
            stack.append(new_item)
    return stack[-1]


if __name__ == '__main__':
    input_expression_list = input().split()
    print(get_result_from_expression(input_expression_list))

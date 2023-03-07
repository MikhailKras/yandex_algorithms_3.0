def get_graph_cycle(adj_matrix):
    visited = {vx: {'color': 'white', 'parent': -1} for vx in range(len(adj_matrix))}
    vertexes_in_cycle = []
    cycle_found = False

    for start_vertex in range(len(adj_matrix)):
        if visited[start_vertex]['color'] == 'white' and not cycle_found:
            stack = [(start_vertex, -1)]
            while stack and not cycle_found:
                node, parent = stack.pop()
                visited[node]['color'] = 'grey'
                visited[node]['parent'] = parent
                for i in range(len(adj_matrix[node])):
                    if adj_matrix[node][i] == 1:
                        if visited[i]['color'] == 'white':
                            stack.append((i, node))
                        elif visited[i]['color'] == 'grey' and visited[node]['parent'] != i:
                            vertexes_in_cycle.append(i)
                            cur_vertex = node
                            while cur_vertex != i:
                                vertexes_in_cycle.append(cur_vertex)
                                cur_vertex = visited[cur_vertex]['parent']
                            cycle_found = True
                            break

        if cycle_found:
            break

    if cycle_found:
        return 'YES', list(map(lambda x: x + 1, vertexes_in_cycle))
    else:
        return 'NO', []


if __name__ == '__main__':
    n_inp = int(input())
    adj_matrix_inp = []
    for i in range(n_inp):
        adj_matrix_inp.append(list(map(int, input().split())))
    res = get_graph_cycle(adj_matrix_inp)
    ans = res[0]
    print(ans)
    if res[1]:
        len_cycle = len(res[1])
        cycle = res[1]
        print(len_cycle)
        print(*cycle)

from typing import List, Dict


def get_answer(adj_list: List[Dict], n: int) -> str:
    visited = {vertex: False for vertex in range(n + 1)}

    for start_vertex in visited.keys():
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            if visited[vertex]:
                continue
            visited[vertex] = True
            if adj_list[vertex]['color'] == 0:
                adj_list[vertex]['color'] = 1
            parent_color = adj_list[vertex]['color']
            for neighbor in adj_list[vertex]['neighbors']:
                if adj_list[neighbor]['color'] == parent_color:
                    return 'NO'
                if parent_color in (0, 1):
                    adj_list[neighbor]['color'] = 2
                else:
                    adj_list[neighbor]['color'] = 1
                stack.append(neighbor)

    return 'YES'


if __name__ == '__main__':
    n_inp, m_inp = tuple(map(int, input().split()))
    adj_list_inp: List[Dict] = [{'color': 0, 'neighbors': []} for _ in range(n_inp + 1)]


    class Edge:
        def __init__(self, two_vertexes: tuple):
            self.first_vertex = two_vertexes[0]
            self.second_vertex = two_vertexes[1]


    for _ in range(m_inp):
        edge: Edge = Edge(tuple(map(int, input().split())))
        adj_list_inp[edge.first_vertex]['neighbors'].append(edge.second_vertex)
        adj_list_inp[edge.second_vertex]['neighbors'].append(edge.first_vertex)
    print(get_answer(adj_list_inp, n_inp))

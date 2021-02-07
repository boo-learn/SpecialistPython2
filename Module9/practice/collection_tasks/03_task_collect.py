import collections
graph = [
    # список смежности
    [1, 3],  # 0
    [4, 5],  # 1
    [],  # 2
    [0, 1, 5],  # 3
    [1, 2],  # 4
    [1, 2, 3],  # 5
    [7], # 6
    [6] # 7
]

start = 0
lengths = [None] * (len(graph))
lengths[start] = 0
# queue = [start]
queue = collections.deque()
queue.append(start)
while queue:
    cur_vertex = queue.popleft()
    for vertex in graph[cur_vertex]:
        if lengths[vertex] is None:
            lengths[vertex] = lengths[cur_vertex] + 1
            queue.append(vertex)

print(lengths)

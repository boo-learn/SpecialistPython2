# "Лабиринт"
# см. Картинку на гугло-диске в Модуле-7
# P-1, P-2 … - точки старта
# Определите: Из каких точек можно дойти до выхода(F), а из каких нет

# Сюда отправляем полное решение
graph = [
    # список смежности
    [1, 6, 7],  # 0
    [0],  # 1
    [14],  # 2
    [10],  # 3
    [5, 7, 15],  # 4
    [4],  # 5
    [0],  # 6
    [0, 4, 8, 9],  # 7
    [7], # 8
    [7, 10, 12, 13],  # 9
    [3, 9, 11],  # 10
    [10],  # 11
    [9],  # 12
    [9],  # 13
    [2],  # 14
    [4], # 15
]


# visited = [False] * (len(graph))
# prev = [None] * (len(graph))
#start = 2


def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:  # посещён ли текущий сосед?
            dfs(w)


#dfs(start)

#print(visited)

for st in range(len(graph)):
    visited = [False] * (len(graph))
    prev = [None] * (len(graph))
    #print(st)
    dfs(st)
    #print(visited)
    #print("=========")
    if visited[13]:
        print(f"exit could be found from start point {st}")
    else:
        print(f"no exit from start point {st} :(")

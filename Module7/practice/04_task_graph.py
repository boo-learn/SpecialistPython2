import json #подключили библиотеку для работы с json
 
dict = {}
graph = []
list = []

with open(r'c:\temp\peoples.json', "r", encoding = "utf-16") as read_file:
    data = json.load(read_file)
    read_file.close()
    

for txt in data: #создали цикл, который будет работать построчно
        list = []
        dict[txt['name'] + ' ' + txt['surname']] = 0
        print(txt['name'], ':' , txt['surname'])

        for txt2 in txt['friends']:
            print('--------',txt2['name'], ':' , txt2['surname'])
            flag = 0
            for name1, ver1 in dict.items():
                if txt2['name'] + ' ' + txt2['surname'] == name1:flag = 1
            if flag == 0: dict[txt2['name'] + ' ' + txt2['surname']] = 0
            list.append(txt2['name'] + ' ' + txt2['surname'])
            
        dict[txt['name'] + ' ' + txt['surname']] = list

listname = []

for name, ver in dict.items():

        listname.append(name)
        print(name)
        
        if ver == 0:
            list = []
        else:
            list = ver
            
        for name1, ver1 in dict.items():
            if ver1 != 0 and name in ver1:
                list.append(name1)
        dict[name] = list

graph = []

for name2, ver2 in dict.items():
    
    otvet = []
    
    print(name2,':',ver2)
    
    for c in ver2:
        if c in listname:
            i = listname.index(c)
            otvet.append(i)

    graph.append(otvet)


def dfs(start_point, graph):
    visited = [False] * (len(graph))
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)
    _dfs(start_point)
    return visited

a=str( input('Введит ФИО: ') )

visited = dfs(listname.index(c), graph)

k = 1
for x in visited:
    if x: k += 1
    
print(f'Придет {k} человек')    

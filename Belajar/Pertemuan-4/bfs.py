# Cara 1
# graphs = {
#     0 : [1,2],
#     1 : [0,3],
#     2 : [0,4,5],
#     3 : [1],
#     4 : [2,6],
#     5 : [2],
#     6 : [4],
# }

# def bfs(graphs, start):
#   visitedList = []
#   queue = [start]
  
#   while queue:
#     current = queue.pop(0)
    
#     if current not in visitedList:
#       visitedList.append(current)
#       neighbor = graphs[current]
#       for x in neighbor:
#         queue.append(x)
#   return visitedList

# # #memanggil fungsi
# print(bfs(graphs, 3))

# Cara 2
# membuat daftar node (vertex list)
vertexList = [0, 1, 2, 3, 4, 5, 6]
edgeList = [ (0,1), (0,2), (1,0), (1,3), (2,0), (2,4), (2,5), (3,1), (4,2), (4,6), (5,2), (6,4)]
graphs = vertexList, edgeList

def bfs(graphs, start):
    vertexList, edgeList = graphs
    visitedList = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]
    # print(adjacencyList)

    # fill adjacencyList from graph
    for edge in edgeList:
        # print(edge)
        adjacencyList[edge[0]].append(edge[1])

        # print("adjacent : ",adjacencyList)
    # bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs, 0))
# Contoh graf angka
# graph1 = {
#     '0' : ['1','2'],
#     '1' : ['3','0'],
#     '2' : ['4','5', '0'],
#     '3' : ['1'],
#     '4' : ['2','6'],
#     '5' : ['2'],
#     '6' : ['4']
# }

# def dfs(graph1, node, visited):
#     if node not in visited:
#         visited.append(node)
#         for n in graph1[node]:
#             dfs(graph1, n, visited)
#     return visited

# visited = dfs(graph1,'3', [])
# print(visited)

# Contoh graf huruf
graph1 = {
    'A' : ['B','C','D'],
    'B' : ['E','F','A'],
    'E' : ['B'],
    'F' : ['B'],
    'C' : ['A'],
    'D' : ['A'],
 
}

def dfs(graph1, node, visited):
    print(visited)
    if node not in visited:
        visited.append(node)
        for n in graph1[node]:
            dfs(graph1, n, visited)
    return visited

visited = dfs(graph1,'A', [])
print(visited)
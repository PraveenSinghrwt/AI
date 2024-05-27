graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

visited = set()

def DFS(graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbour in graph[node]:
            DFS(graph, neighbour)
                
print('Depth First Seach: ')
DFS(graph, '1')
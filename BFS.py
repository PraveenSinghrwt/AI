graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

closed_list = []
open_list = []

def BFS(graph, node):
    closed_list.append(node)
    open_list.append(node)
    
    while open_list:
        explored_node = open_list.pop(0)
        print(explored_node, end=" ")
        
        for neighbour in graph[explored_node]:
            if neighbour not in closed_list:
                closed_list.append(neighbour)
                open_list.append(neighbour)
                
print('Breadth First Seach: ')
BFS(graph, '1')
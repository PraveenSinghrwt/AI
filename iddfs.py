graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

def DLS(node, goal, depth):
    if node == goal:
        return True
    elif depth > 0:
        for neighbour in graph[node]:
            if DLS(neighbour, goal, depth - 1):
                return True
    return False
    
def IDDFS(start, goal, max_depth):
    for depth in range(max_depth):
        if DLS(start, goal, depth):
            return True
    return False

    
start_node = '1'
goal_node = '6'
max_depth = 3

if IDDFS(start_node, goal_node, max_depth):
    print('Goal node found')
else:
    print('Goal node not found')




# graph = {
#     '1': ['2', '3'],
#     '2': ['4', '5'],
#     '3': ['6', '7'],
#     '4': [],
#     '5': [],
#     '6': [],
#     '7': []
# }

# def DLS(node, goal, depth, current_path):
#     current_path.append(node)  # Append the current node to the current path
    
#     if node == goal:
#         return True, current_path  # Return True and the current path if goal is found
    
#     elif depth > 0:
#         for neighbour in graph[node]:
#             found, path = DLS(neighbour, goal, depth - 1, current_path.copy())  # Pass a copy of current path
#             if found:
#                 return True, path
    
#     return False, None

# def IDDFS(start, goal, max_depth):
#     for depth in range(max_depth):
#         current_path = []
#         found, path = DLS(start, goal, depth, current_path)
        
#         if found:
#             print(f'Goal node found at depth {depth}: {path}')
#             return True
    
#         print(f'Exploring at depth {depth}: {current_path}')
    
#     return False

# start_node = '1'
# goal_node = '6'
# max_depth = 3

# if IDDFS(start_node, goal_node, max_depth):
#     print('Goal node found')
# else:
#     print('Goal node not found')

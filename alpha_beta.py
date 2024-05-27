terminal_nodes = {
    'H': -1,
    'I': 4,
    'J': 2,
    'K': 6,
    'L': -3,
    'M': -5,
    'N': 0,
    'O': 7
}

# Define the tree structure
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O']
}

# Define the minimax algorithm with alpha-beta pruning
def alphabeta(node, depth, alpha, beta, is_maximizing_player):
    if node in terminal_nodes:
        return terminal_nodes[node]

    if is_maximizing_player:
        best_value = float('-inf')
        for child in tree[node]:
            value = alphabeta(child, depth + 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Beta cut-off
        return best_value
    else:
        best_value = float('inf')
        for child in tree[node]:
            value = alphabeta(child, depth + 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break  # Alpha cut-off
        return best_value

# Define a function to find the optimal path using alpha-beta pruning
def find_optimal_path(node, is_maximizing_player):
    optimal_value = alphabeta(node, 0, float('-inf'), float('inf'), is_maximizing_player)
    path = [node]

    while node in tree:
        if is_maximizing_player:
            best_value = float('-inf')
            best_node = None
            for child in tree[node]:
                value = alphabeta(child, 0, float('-inf'), float('inf'), not is_maximizing_player)
                if value > best_value:
                    best_value = value
                    best_node = child
        else:
            best_value = float('inf')
            best_node = None
            for child in tree[node]:
                value = alphabeta(child, 0, float('-inf'), float('inf'), not is_maximizing_player)
                if value < best_value:
                    best_value = value
                    best_node = child
        path.append(best_node)
        node = best_node
        is_maximizing_player = not is_maximizing_player

    return optimal_value, path

# Find the optimal value and path for the root node 'A'
optimal_value, optimal_path = find_optimal_path('A', True)

# Print the optimal value and path
print(f"The optimal value is {optimal_value} and the optimal path is {' -> '.join(optimal_path)}")

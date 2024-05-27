def a_star_search(graph, start, goal, heuristic):
    open_set = [(0, start)]  # Priority queue as a list of tuples (f_cost, node)
    g_cost = {start: 0}
    came_from = {start: None}

    while open_set:
        # Find the node with the smallest f_cost
        open_set.sort()
        current = open_set.pop(0)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            cost = graph[current][neighbor]
            tentative_g_cost = g_cost[current] + cost

            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                open_set.append((f_cost, neighbor))
                came_from[neighbor] = current

    return []

def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# Example graph as a dictionary
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Simple heuristic function
def heuristic(node, goal):
    heuristic_values = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1
    }
    return heuristic_values[node]

# Perform A* search from 'A' to 'D'
start_node = 'A'
goal_node = 'D'
path = a_star_search(graph, start_node, goal_node, heuristic)
print("Path from", start_node, "to", goal_node, ":", path)

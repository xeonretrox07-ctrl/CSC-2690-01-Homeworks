#Kayleb "Xeon" Gonzalez
#CSC 3690 01 Chapter 2 Homework 2.2
import heapq

def a_star_search(g, h, start_state, goal_state): #g = graph and h = heuristics
    priority_queue = []
    heapq.heappush(priority_queue, (h[start_state], start_state))

    g_score = {node: float('inf') for node in g}
    g_score[start_state] = 0

    came_from = {}

    while priority_queue:
        current_f, current_node = heapq.heappop(priority_queue)

        if current_node == goal_state:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start_state)
            path.reverse()
            return path, g_score[goal_state]

        for neighbor, weight in g[current_node].items():
            tentative_g_score = g_score[current_node] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                heapq.heappush(priority_queue, (f_score, neighbor))
    return None, float('inf')

#Nodes of the graph
g = {
    'S': {'A': 3, 'B': 2, 'C': 5}, #Start of the graph
    'A': {'C': 3, 'G': 2},
    'B': {'D': 6},
    'C': {'B': 4, 'H': 3},
    'D': {'E': 2, 'F': 3},
    'E': {'F': 5},
    'F': {}, #Goal of the graph
    'G': {'D': 4, 'E': 5},
    'H': {'A': 4, 'D': 4}
}

#Nodes of the heuristic
h = {
    'S': 10, #Start of the heuristic
    'A': 8,
    'B': 9,
    'C': 7,
    'D': 4,
    'E': 3,
    'F': 0, #Goal of the heuristic
    'G': 6,
    'H': 6
}

path, total_cost = a_star_search(g, h, start_state='S', goal_state='F')

print(f"Path Found: {path}")
print(f"Total Cost: {total_cost}")
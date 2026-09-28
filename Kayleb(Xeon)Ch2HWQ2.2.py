#Kayleb "Xeon" Gonzalez
#CSC 3690 01 Chapter 2 Homework 2.2
from collections import deque

def bfs_search(start_state, goal_state):
    queue = deque([(start_state, [start_state])])
    visited_order = []

    while queue:
        current, path = queue.popleft()
        visited_order.append(current)

        if current == goal_state:
            return visited_order, path

        left_child = 2 * current
        right_child = 2 * current + 1

        queue.append((left_child, path + [left_child]))
        queue.append((right_child, path + [right_child]))

    return visited_order, []

start = 1
goal = 11
visited, final_path = bfs_search(start, goal)

print(f"Order of the nodes: {visited}")
print(f"Path to goal: {final_path}")
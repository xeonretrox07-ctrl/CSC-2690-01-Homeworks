#Kayleb "Xeon" Gonzalez
# CSC 3690 01 Chapter 2 Homework 2.6

g = { # g = graph
    'A': ['B', 'C', 'U'],
    'B': ['E', 'G'],
    'C': ['G', 'I', 'J'],
    'U': ['K', 'Y'],
    'E': ['G', 'M'],
    'G': ['M'],
    'I': ['M'],
    'J': ['K'],
    'K': ['J'],
    'Y': ['M'],
    'M': []
}

h = { # h = heuristic
    'A': 7, 'B': 5, 'C': 3, 'U': 4, 'E': 2, 'G': 3,
    'I': 6, 'J': 4, 'K': 1, 'Y': 2, 'M': 0
}

def best_neighbor(node):
    neighbors = g[node]
    if not neighbors:
        return None

    return min(neighbors, key=lambda n: h[n])

def hill_climbing(start, goal):
    current = start
    path = [current]
    print(f"Start at {current} (h={h[current]})")

    while current != goal:
        nxt = best_neighbor(current)

        if nxt is None:
            print("No neighbors found")
            break

        current = nxt
        path.append(nxt)
        path.append(current)
        print(f"Current {current} (h={h[current]})")

    if current == goal:
        print("Goal found")
    else:
        print("Goal not found")

    return path

print("Basic Hill Climbing:")
result = hill_climbing('A', 'M')
print("Path:", "->".join(result))

def hill_climbing_sideways(start, goal):
    current = start
    path = [current]
    visited = {current}

    while current != goal:
        nxt = best_neighbor(current)
        if nxt is None:
            print("No neighbors found")
            break
        if h[nxt] < h[current] or (
            h[nxt] == h[current] and nxt not in visited
        ):
            current = nxt
            visited.add(current)
            path.append(current)
            print(f"Move to {current} (h={h[current]})")
        else:
            print(f"Stuck at {current} (h={h[current]})")
            break

    if current == goal:
        print("Goal found")
    else:
        print("Goal not found")

    return path

print("Hill Climbing with Sideways:")
result = hill_climbing_sideways('A', 'M')
print("Path:", "->".join(result))
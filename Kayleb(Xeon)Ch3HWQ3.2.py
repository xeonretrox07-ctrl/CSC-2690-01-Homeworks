# Kayleb "Xeon" Gonzalez
# CSC 3960 01 Chapter 3 Homework 3.2

import math

TREE = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['D1', 'D2'],
    'E': ['E1', 'E2'],
    'F': ['F1', 'F2'],
    'G': ['G1', 'G2']
}

LEAF = {
    'D1': 3, 'D2': 5,
    'E1': 17, 'E2': 8,
    'F1': -2, 'F2': 5,
    'G1': -1, 'G2': 7
}

visited = []

def alphabeta(node, alpha, beta, is_max, depth=0):
    pad = ' ' * depth

    if node in LEAF:
        visited.append(node)
        print(f"{pad}{node} = {LEAF[node]}")
        return LEAF[node]

    kind = 'MAX' if is_max else 'MIN'
    print(f"{pad}{node} ({kind}) alpha={alpha}, beta={beta}")
    kids = TREE[node]

    if is_max:
        value = -math.inf
        for i, child in enumerate(kids):
            child_value = alphabeta(child, alpha, beta, False, depth + 1)

            value = max(value, child_value)
            alpha = max(alpha, value)

            if alpha >= beta:
                print(f"{pad} PRUNE {kids[i+1]} (alpha={alpha} >= beta={beta})")
                break

    else:
        value = math.inf
        for i, child in enumerate(kids):
            child_value = alphabeta(child, alpha, beta, True, depth + 1)

            value = min(value, child_value)
            beta = min(beta, value)
            if alpha >= beta:
                print(f"{pad} PRUNE {kids[i+1]} (alpha={alpha} >= beta={beta})")
                break

    print(f"{pad}{node} returns {value}")
    return value

result = alphabeta('A', -math.inf, math.inf, True)
print("Root value:", result)
print("Leaves evaluated:", visited)
print("Leaves pruned:", [leaf for leaf in LEAF if leaf not in visited])

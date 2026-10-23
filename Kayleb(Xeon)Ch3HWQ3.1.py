# Kayleb "Xeon" Gonzalez
# CSC 3960 01 Chapter 3 Homework 3.1
def minimax(values, is_max):
    if len(values) == 1:
        return values[0]

    next_level = []

    for i in range(0, len(values), 2):
        if is_max:
            next_level.append(max(values[i], values[i + 1]))
        else:
            next_level.append(min(values[i], values[i + 1]))

    return minimax(next_level, not is_max)

values = [3, 5, 17, 8, -2, 5, -1, 7]
result = minimax(values, True)
print("Minimax value is: ", result)

def is_valid(assignment, region, color, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment

    unassigned = [region for region in regions if region not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(assignment, region, color, neighbors):
            assignment[region] = color
            result = backtrack(assignment, regions, colors, neighbors)
            if result:
                return result
            del assignment[region]

    return None

def map_coloring(regions, colors, neighbors):
    assignment = {}
    return backtrack(assignment, regions, colors, neighbors)

# Example usage
regions = ['A', 'B', 'C', 'D', 'E']
colors = ['Red', 'Green', 'Blue']
neighbors = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['B', 'D']
}

solution = map_coloring(regions, colors, neighbors)
print("Color assignment:", solution)

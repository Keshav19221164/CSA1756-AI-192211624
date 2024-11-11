import sys

def tsp_dp(distances):
    n = len(distances)
    dp = [[None] * (1 << n) for _ in range(n)]
    
    def visit(city, visited):
        if visited == (1 << n) - 1:  # All cities have been visited
            return distances[city][0]  # Return to the starting city
        
        if dp[city][visited] is not None:
            return dp[city][visited]
        
        min_cost = sys.maxsize
        for next_city in range(n):
            if visited & (1 << next_city) == 0:  # If next_city hasn't been visited
                cost = distances[city][next_city] + visit(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, cost)
        
        dp[city][visited] = min_cost
        return min_cost
    
    return visit(0, 1)  # Start from city 0 with only that city visited

# Example usage
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum traveling cost:", tsp_dp(distances))

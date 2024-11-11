import math

# Alpha-Beta Pruning algorithm
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta, target_depth):
    # Base case: Leaf node is reached
    if depth == target_depth:
        return values[node_index]

    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, target_depth)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval

    else:
        min_eval = math.inf
        for i in range(2):
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, target_depth)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Example usage
if __name__ == "__main__":
    # Example game tree leaf nodes (values)
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    # Set the target depth for the game tree
    target_depth = math.log2(len(values))

    # Call the alpha-beta pruning function
    optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf, int(target_depth))
    print("The optimal value is:", optimal_value)

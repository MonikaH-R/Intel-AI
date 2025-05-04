import random
def objective_function(x):
    """The function to maximize."""
    return -x**2 + 4*x
def get_neighbors(x, step_size=0.1):
    """Generates neighboring values of x."""
    return [x - step_size, x + step_size]
def hill_climbing_function_max(start_x, max_iterations=100):
    """Finds the maximum of a function using Hill Climbing."""
    current_x = start_x
    current_value = objective_function(current_x)

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_x)
        best_neighbor = current_x
        best_value = current_value

        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            if neighbor_value > best_value:
                best_value = neighbor_value
                best_neighbor = neighbor

        if best_value > current_value:
            current_x = best_neighbor
            current_value = best_value
        else:
            break  # Local optimum reached

    return current_x, current_value
if __name__ == "__main__":
    start_x = random.uniform(0, 5)  # Start with a random value
    max_x, max_value = hill_climbing_function_max(start_x)
    print(f"Starting x: {start_x}")
    print(f"Maximum found at x = {max_x:.4f} with value f(x) = {max_value:.4f}")
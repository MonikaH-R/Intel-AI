import random
import math
def complex_function(x, y):
    """A complex mathematical function with multiple local optima."""
    return (1 - x/2 + x**5 + y**3) * math.exp(-x**2 - y**2)
def get_neighbor(x, y, step_size=0.1):
    """Generates neighboring (x, y) values."""
    dx = random.uniform(-step_size, step_size)
    dy = random.uniform(-step_size, step_size)
    return x + dx, y + dy
def simulated_annealing_function_max(start_x, start_y, initial_temperature=100, cooling_rate=0.99, iterations_per_temp=500):
    """Finds the global maximum of a function using Simulated Annealing."""
    current_x = start_x
    current_y = start_y
    current_value = complex_function(current_x, current_y)
    best_x = current_x
    best_y = current_y
    best_value = current_value
    temperature = initial_temperature

    while temperature > 1e-8:
        for _ in range(iterations_per_temp):
            neighbor_x, neighbor_y = get_neighbor(current_x, current_y)
            neighbor_value = complex_function(neighbor_x, neighbor_y)
            delta_value = neighbor_value - current_value

            if delta_value > 0 or random.random() < math.exp(delta_value / temperature):
                current_x = neighbor_x
                current_y = neighbor_y
                current_value = neighbor_value

                if current_value > best_value:
                    best_value = current_value
                    best_x = current_x
                    best_y = current_y

        temperature *= cooling_rate

    return best_x, best_y, best_value
if __name__ == "__main__":
    start_x = random.uniform(-3, 3)
    start_y = random.uniform(-3, 3)
    max_x, max_y, max_value = simulated_annealing_function_max(start_x, start_y)
    print(f"Starting point: x = {start_x:.4f}, y = {start_y:.4f}")
    print(f"Global maximum found at x = {max_x:.4f}, y = {max_y:.4f} with value f(x, y) = {max_value:.4f}")
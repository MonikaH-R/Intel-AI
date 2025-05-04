import random
import math

def calculate_distance(city1, city2):
    """Calculates the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(path, cities):
    """Calculates the total distance of a path."""
    total_distance = 0
    for i in range(len(path)):
        city1_index = path[i]
        city2_index = path[(i + 1) % len(path)]  # Wrap around to the start
        total_distance += calculate_distance(cities[city1_index], cities[city2_index])
    return total_distance

def get_neighbor(path):
    """Generates a neighboring path by swapping two cities."""
    i, j = random.sample(range(len(path)), 2)
    neighbor = list(path)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def simulated_annealing_tsp(cities, initial_temperature=1000, cooling_rate=0.99, iterations_per_temp=100):
    """Solves the TSP using Simulated Annealing."""
    num_cities = len(cities)
    current_path = list(range(num_cities))
    random.shuffle(current_path)
    current_distance = calculate_total_distance(current_path, cities)
    best_path = list(current_path)
    best_distance = current_distance
    temperature = initial_temperature

    while temperature > 1e-8:
        for _ in range(iterations_per_temp):
            neighbor_path = get_neighbor(current_path)
            neighbor_distance = calculate_total_distance(neighbor_path, cities)
            delta_distance = neighbor_distance - current_distance

            if delta_distance < 0 or random.random() < math.exp(-delta_distance / temperature):
                current_path = neighbor_path
                current_distance = neighbor_distance

                if current_distance < best_distance:
                    best_distance = current_distance
                    best_path = current_path

        temperature *= cooling_rate

    return best_path, best_distance

if __name__ == "__main__":
    cities = [(0, 0), (1, 5), (5, 5), (6, 2), (3, 1)]
    best_path, best_distance = simulated_annealing_tsp(cities)
    print("Cities:", cities)
    print("Best Path (indices):", best_path)
    print("Best Distance:", best_distance)
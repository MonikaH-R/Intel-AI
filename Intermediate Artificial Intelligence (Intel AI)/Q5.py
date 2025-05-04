import random
import numpy as np
def fitness(individual, puzzle):
    """Calculates the fitness of a Sudoku board. Lower is better (fewer errors)."""
    errors = 0
    n = 9
    for row in range(n):
        errors += len(individual[row]) - len(set(individual[row]))
    for col in range(n):
        col_values = [individual[row][col] for row in range(n)]
        errors += len(col_values) - len(set(col_values))
    for block_row in range(0, n, 3):
        for block_col in range(0, n, 3):
            block_values = [individual[row][col] for row in range(block_row, block_row + 3) for col in range(block_col, block_col + 3)]
            errors += len(block_values) - len(set(block_values))

    # Penalize fixed cells that are incorrect
    for r in range(n):
        for c in range(n):
            if puzzle[r][c] != 0 and puzzle[r][c] != individual[r][c]:
                errors += 10  # High penalty

    return -errors  # We want to maximize fitness (minimize errors)
def create_individual(puzzle):
    """Creates a random Sudoku board respecting the fixed cells."""
    individual = [list(row) for row in puzzle]
    n = 9
    for row in range(n):
        empty_cells = [i for i, val in enumerate(puzzle[row]) if val == 0]
        possible_values = list(range(1, 10))
        random.shuffle(possible_values)
        for i, col in enumerate(empty_cells):
            individual[row][col] = possible_values[i % len(possible_values)]
    return individual
def crossover(parent1, parent2):
    """Performs crossover between two Sudoku boards (row-based)."""
    n = 9
    child = [list(row) for row in parent1]
    for i in range(n):
        if random.random() < 0.5:
            child[i] = list(parent2[i])
    return child
def mutate(individual, puzzle, mutation_rate=0.05):
    """Performs mutation on a Sudoku board (swaps two non-fixed cells in a row)."""
    n = 9
    row = random.randint(0, n - 1)
    empty_indices = [i for i, val in enumerate(puzzle[row]) if val == 0]
    if len(empty_indices) >= 2 and random.random() < mutation_rate:
        i, j = random.sample(empty_indices, 2)
        individual[row][i], individual[row][j] = individual[row][j], individual[row][i]
    return individual
def genetic_algorithm_sudoku(puzzle, population_size=100, generations=500):
    """Solves a Sudoku puzzle using a Genetic Algorithm."""
    population = [create_individual(puzzle) for _ in range(population_size)]

    for generation in range(generations):
        population.sort(key=lambda ind: fitness(ind, puzzle), reverse=True)
        best_individual = population[0]
        if fitness(best_individual, puzzle) == 0:
            print(f"Solution found in generation {generation + 1}:")
            return np.array(best_individual)

        next_generation = [best_individual]  # Keep the best individual

        for _ in range(population_size - 1):
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])
            child = crossover(parent1, parent2)
            child = mutate(child, puzzle)
            next_generation.append(child)

        population = next_generation

    print("Maximum generations reached. Best solution found:")
    return np.array(population[0])
if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    solution = genetic_algorithm_sudoku(puzzle)
    print(solution)
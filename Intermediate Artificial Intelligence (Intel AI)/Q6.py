import random
def evaluate_weights(weights):
    """A super simple way to 'evaluate' a set of weights."""
    # We want the weights to be close to [1, 0] in this example
    error = abs(weights[0] - 1) + abs(weights[1] - 0)
    return -error  # Higher score is better
def mutate_weights(weights, mutation_rate=0.1):
    """Randomly change some weights slightly."""
    mutated_weights = list(weights)
    for i in range(len(mutated_weights)):
        if random.random() < mutation_rate:
            mutated_weights[i] += random.uniform(-0.2, 0.2)
    return mutated_weights
def simple_genetic_algorithm():
    """A very basic genetic algorithm."""
    # Start with a random population of weight sets
    population = [[random.uniform(0, 1) for _ in range(2)] for _ in range(5)]

    for generation in range(10):
        # Evaluate each set of weights
        scores = [evaluate_weights(w) for w in population]

        # Select the 'best' (simplistic selection: just sort)
        ranked_population = [population[i] for i in sorted(range(len(population)), key=lambda i: scores[i], reverse=True)]
        best_weights = ranked_population[0]
        print(f"Generation {generation + 1}, Best Score: {scores[0]:.4f}, Best Weights: {best_weights}")

        # Create the next generation (very basic reproduction and mutation)
        next_generation = [best_weights[:]]  # Keep the best one

        for _ in range(len(population) - 1):
            # Simple crossover: take half from the top two
            parent1 = ranked_population[0]
            parent2 = ranked_population[1]
            child = parent1[:1] + parent2[1:]
            child = mutate_weights(child)
            next_generation.append(child)

        population = next_generation

    print("\nFinal 'optimized' weights:", population[0])
if __name__ == "__main__":
    simple_genetic_algorithm()
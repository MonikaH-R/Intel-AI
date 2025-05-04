import random
def objective_function(board):
    """Calculates the number of attacking pairs of queens on the board."""
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks
def get_neighbors(board):
    """Generates neighboring board configurations by moving one queen in its column."""
    n = len(board)
    neighbors = []
    for col in range(n):
        original_row = board[col]
        for row in range(n):
            if row != original_row:
                neighbor = list(board)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors
def hill_climbing_n_queens(n, max_iterations=1000):
    """Solves the N-Queens problem using the Hill Climbing algorithm."""
    current_board = [random.randint(0, n - 1) for _ in range(n)]
    current_attacks = objective_function(current_board)

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_board)
        best_neighbor = current_board
        best_attacks = current_attacks

        for neighbor in neighbors:
            neighbor_attacks = objective_function(neighbor)
            if neighbor_attacks < best_attacks:
                best_attacks = neighbor_attacks
                best_neighbor = neighbor

        if best_attacks < current_attacks:
            current_board = best_neighbor
            current_attacks = best_attacks
        else:
            break  # Local optimum reached

        if current_attacks == 0:
            return current_board

    return current_board
if __name__ == "__main__":
    n = 8
    solution = hill_climbing_n_queens(n)
    attacks = objective_function(solution)
    print(f"N-Queens solution for N = {n}: {solution}")
    print(f"Number of attacking pairs: {attacks}")


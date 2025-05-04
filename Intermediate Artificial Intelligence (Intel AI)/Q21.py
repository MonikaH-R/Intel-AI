import heapq
def a_star_search(grid, start_node, goal_node):
    """
    A* search algorithm to find the shortest path in a 2D grid.

    Args:
        grid: A 2D list (list of lists) representing the environment.
              0 indicates a free path, and 1 indicates an obstacle.
        start_node: A tuple (start_row, start_col) representing the starting position.
        goal_node: A tuple (goal_row, goal_col) representing the goal position.

    Returns:
        A list of tuples representing the shortest path from start to goal,
        or None if no path is found.
    """

    # Get the dimensions of the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Helper function to check if a cell is valid (within bounds and not an obstacle)
    def is_valid_cell(row, col):
        return 0 <= row < num_rows and 0 <= col < num_cols and grid[row][col] == 0

    # Helper function to calculate the heuristic (estimated distance to goal)
    def calculate_heuristic(node, goal):
        # Using Manhattan distance (sum of absolute differences in row and col)
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    # Priority queue for nodes to be evaluated, initialized with the start node
    open_set = [(calculate_heuristic(start_node, goal_node), 0, start_node)]  # (f_score, g_score, node)
    # Set to keep track of visited nodes
    closed_set = set()

    # Dictionary to store the parent of each node in the path
    parent_map = {}
    # Dictionary to store the g_score of each node
    g_score_map = {start_node: 0}

    # Main loop of the A* algorithm
    while open_set:
        # Get the node with the lowest f_score (estimated total cost)
        _, current_g_score, current_node = heapq.heappop(open_set)

        # If we've reached the goal, reconstruct the path and return it
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent_map.get(current_node)  # Use .get() to avoid KeyError
            return path[::-1]  # Reverse the path to get it from start to goal

        # If the current node has already been visited, skip it
        if current_node in closed_set:
            continue

        # Mark the current node as visited
        closed_set.add(current_node)

        # Explore the neighbors of the current node
        current_row, current_col = current_node
        # Possible movements: up, down, left, right
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move_row, move_col in possible_moves:
            neighbor_row = current_row + move_row
            neighbor_col = current_col + move_col
            neighbor_node = (neighbor_row, neighbor_col)

            # If the neighbor is a valid cell
            if is_valid_cell(neighbor_row, neighbor_col):
                # Calculate the tentative g_score (cost from start to neighbor through current)
                tentative_g_score = current_g_score + 1

                if neighbor_node not in g_score_map or tentative_g_score < g_score_map.get(neighbor_node, float('inf')):
                    # Update parent and g_score
                    parent_map[neighbor_node] = current_node
                    g_score_map[neighbor_node] = tentative_g_score
                    # Calculate the f_score (estimated total cost from start to goal through neighbor)
                    neighbor_f_score = tentative_g_score + calculate_heuristic(neighbor_node, goal_node)
                    # Add the neighbor to the open set with its scores
                    heapq.heappush(open_set, (neighbor_f_score, tentative_g_score, neighbor_node))

    # If the open set is empty and we haven't found the goal, there is no path
    return None
def main():
    # Define the grid (0: free, 1: obstacle)
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    # Define the start and goal nodes
    start_node = (0, 0)
    goal_node = (4, 4)

    # Find the path using A* search
    path = a_star_search(grid, start_node, goal_node)

    # Print the results
    if path:
        print("Shortest path found:")
        for row, col in path:
            print(f"({row}, {col})")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()


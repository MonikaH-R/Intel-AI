import numpy as np
import random
class GridWorld:
    def __init__(self, size, goal):
        self.size = size
        self.goal = goal
        self.state = (0, 0)  # Initial state
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def is_valid(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def step(self, action):
        row, col = self.state
        dr, dc = action
        new_row, new_col = row + dr, col + dc

        if self.is_valid(new_row, new_col):
            self.state = (new_row, new_col)

        reward = -1  # Small penalty for each step
        done = False
        if self.state == self.goal:
            reward = 100
            done = True

        return self.state, reward, done

    def reset(self):
        self.state = (0, 0)
        return self.state
def q_learning(env, alpha=0.1, gamma=0.9, epsilon=0.1, episodes=1000):
    q_table = np.zeros((env.size, env.size, len(env.actions)))

    for episode in range(episodes):
        state = env.reset()
        done = False

        while not done:
            row, col = state

            # Epsilon-greedy action selection
            if random.uniform(0, 1) < epsilon:
                action_index = random.choice(range(len(env.actions)))
            else:
                action_index = np.argmax(q_table[row, col, :])

            action = env.actions[action_index]
            next_state, reward, done = env.step(action)
            next_row, next_col = next_state

            # Q-table update rule
            old_value = q_table[row, col, action_index]
            next_max = np.max(q_table[next_row, next_col, :])
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[row, col, action_index] = new_value

            state = next_state

        if (episode + 1) % 100 == 0:
            print(f"Episode {episode + 1} finished.")

    return q_table
def play_game(env, q_table):
    state = env.reset()
    done = False
    path = [state]
    while not done:
        row, col = state
        action_index = np.argmax(q_table[row, col, :])
        action = env.actions[action_index]
        state, _, done = env.step(action)
        path.append(state)
    return path
# Example Usage:
grid_size = 5
goal_position = (4, 4)
env = GridWorld(grid_size, goal_position)
trained_q_table = q_learning(env, episodes=2000)
print("\nTrained Q-table:")
print(trained_q_table)

print("\nPlaying a game using the trained Q-table:")
path = play_game(env, trained_q_table)
print("Path taken:", path)
import math
import random
def create_map(width, height, num_obstacles):
    """Creates a simple 2D map with random circular obstacles."""
    obstacles = []
    for _ in range(num_obstacles):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        radius = random.uniform(0.5, 2.0)
        obstacles.append(((x, y), radius))
    return obstacles, width, height
def simulate_lidar(robot_x, robot_y, obstacles, map_width, map_height, num_rays=36):
    """Simulates 2D LIDAR sensor data with improved ray-circle intersection."""
    scan = []
    for i in range(num_rays):
        angle_rad = 2 * math.pi * i / num_rays  # Evenly spaced angles
        end_x = robot_x + 20 * math.cos(angle_rad)  # Max sensor range
        end_y = robot_y + 20 * math.sin(angle_rad)

        min_distance = float('inf')
        detected_obstacle = None

        # Check for intersections with obstacles
        for (obs_x, obs_y), obs_radius in obstacles:
            # Ray-circle intersection using the quadratic formula
            dx = end_x - robot_x
            dy = end_y - robot_y
            a = dx**2 + dy**2
            b = 2 * (dx * (robot_x - obs_x) + dy * (robot_y - obs_y))
            c = (robot_x - obs_x)**2 + (robot_y - obs_y)**2 - obs_radius**2

            if a == 0:
                continue  # Ray starts at circle center, handle separately if needed

            discriminant = b**2 - 4 * a * c
            if discriminant >= 0:
                t1 = (-b - math.sqrt(discriminant)) / (2 * a)
                t2 = (-b + math.sqrt(discriminant)) / (2 * a)

                # Consider only intersections within the ray's range (0 <= t <= 1)
                for t in [t1, t2]:
                    if 0 <= t <= 1:
                        intersection_x = robot_x + t * dx
                        intersection_y = robot_y + t * dy
                        distance = math.sqrt((intersection_x - robot_x)**2 + (intersection_y - robot_y)**2)
                        if distance < min_distance:
                            min_distance = distance
                            detected_obstacle = (obs_x, obs_y)

        if detected_obstacle:
            scan.append((angle_rad, min_distance))
        else:
            scan.append((angle_rad, float('inf')))  # No obstacle detected

    return scan
if __name__ == "__main__":
    # Create a 2D map with obstacles
    obstacles, map_width, map_height = create_map(30, 30, 5)
    print("Obstacles:", obstacles)

    # Robot's position
    robot_x = 5
    robot_y = 5
    print(f"\nRobot Position: ({robot_x:.2f}, {robot_y:.2f})")

    # Simulate LIDAR scan
    lidar_data = simulate_lidar(robot_x, robot_y, obstacles, map_width, map_height)

    print("\nLIDAR Scan Data (angle in radians, distance):")
    for angle, distance in lidar_data:
        if distance == float('inf'):
            print(f"Angle: {angle:.2f}, Distance: Infinity (No obstacle)")
        else:
            print(f"Angle: {angle:.2f}, Distance: {distance:.2f}")

    # You could then use this 'lidar_data' to perform obstacle detection or mapping.
    # For example, points with finite distance indicate potential obstacles.

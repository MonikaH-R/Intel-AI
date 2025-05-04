import numpy as np
import math
def rotation_matrix_2d(angle_rad):
    """Creates a 2D rotation matrix."""
    return np.array([
        [math.cos(angle_rad), -math.sin(angle_rad), 0],
        [math.sin(angle_rad), math.cos(angle_rad), 0],
        [0, 0, 1]
    ])
def translation_matrix_2d(x, y):
    """Creates a 2D translation matrix."""
    return np.array([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1]
    ])
def forward_kinematics_2joint(theta1_deg, theta2_deg, link1_length, link2_length):
    """Computes the end-effector position for a 2-joint arm."""
    # Convert angles to radians
    theta1_rad = math.radians(theta1_deg)
    theta2_rad = math.radians(theta2_deg)

    # Transformation from base frame to joint 1 frame
    T_0_1 = translation_matrix_2d(link1_length, 0) @ rotation_matrix_2d(theta1_rad)

    # Transformation from joint 1 frame to joint 2 frame
    T_1_2 = translation_matrix_2d(link1_length, 0) @ rotation_matrix_2d(theta1_rad)
    T_1_2 = translation_matrix_2d(link2_length, 0) @ rotation_matrix_2d(theta2_rad)

    # Transformation from base frame to end-effector frame
    T_0_2 = T_0_1 @ T_1_2

    # End-effector position (x, y) is in the first two elements of the last column
    end_effector_x = T_0_2[0, 2]
    end_effector_y = T_0_2[1, 2]

    return end_effector_x, end_effector_y
if __name__ == "__main__":
    # Define joint angles and link lengths
    angle_joint1_deg = 45
    angle_joint2_deg = 30
    length_link1 = 1.0  # Unit length
    length_link2 = 0.8  # Unit length

    # Compute forward kinematics
    end_effector_position = forward_kinematics_2joint(angle_joint1_deg, angle_joint2_deg, length_link1, length_link2)

    print("Forward Kinematics for a 2-Joint Robotic Arm (2D):")
    print(f"Joint 1 Angle: {angle_joint1_deg} degrees")
    print(f"Joint 2 Angle: {angle_joint2_deg} degrees")
    print(f"Link 1 Length: {length_link1}")
    print(f"Link 2 Length: {length_link2}")
    print(f"End-effector Position (x, y): ({end_effector_position[0]:.4f}, {end_effector_position[1]:.4f})")

    # Example with different angles
    angle_joint1_deg = 90
    angle_joint2_deg = -45
    end_effector_position = forward_kinematics_2joint(angle_joint1_deg, angle_joint2_deg, length_link1, length_link2)
    print(f"\nJoint 1 Angle: {angle_joint1_deg} degrees")
    print(f"Joint 2 Angle: {angle_joint2_deg} degrees")
    print(f"End-effector Position (x, y): ({end_effector_position[0]:.4f}, {end_effector_position[1]:.4f})")

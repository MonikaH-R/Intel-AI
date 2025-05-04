import numpy as np
class KalmanFilter:
    def __init__(self, initial_state, initial_covariance, process_noise, measurement_noise):
        self.x = np.array(initial_state).reshape(-1, 1)  # State vector
        self.P = np.array(initial_covariance)          # Covariance matrix
        self.Q = np.array(process_noise)             # Process noise covariance
        self.R = np.array(measurement_noise)         # Measurement noise covariance
        self.H = np.eye(len(initial_state))          # Observation matrix (assuming direct measurement of state)

    def predict(self):
        # Predict the state and covariance
        self.x = self.x  # Assuming no external motion for simplicity
        self.P = self.P + self.Q

    def update(self, measurement):
        # Update the state and covariance based on the measurement
        z = np.array(measurement).reshape(-1, 1)
        y = z - np.dot(self.H, self.x)             # Measurement residual
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R  # Innovation covariance
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  # Kalman gain
        self.x = self.x + np.dot(K, y)             # Updated state estimate
        self.P = (np.eye(self.P.shape[0]) - np.dot(K, self.H)).dot(self.P) # Updated covariance
# Example Usage:
# Simulate a robot moving in 1D (just position)
initial_state = [0.0]
initial_covariance = [[1.0]]
process_noise = [[0.1]]
measurement_noise = [[0.5]]
kf = KalmanFilter(initial_state, initial_covariance, process_noise, measurement_noise)
# Simulate sensor readings
measurements = [0.2, 0.5, 0.8, 1.1, 1.5]
print("Initial State Estimate:", kf.x.flatten())
print("Initial Covariance:\n", kf.P)
for i, measurement in enumerate(measurements):
    kf.predict()
    kf.update([measurement])
    print(f"\nStep {i+1}:")
    print("Measurement:", measurement)
    print("Estimated State:", kf.x.flatten())
    print("Estimated Covariance:\n", kf.P)
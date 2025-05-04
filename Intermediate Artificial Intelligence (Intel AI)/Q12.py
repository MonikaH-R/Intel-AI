import random
import numpy as np
def convolution(input_image, kernel):
    """Simplified 2D convolution operation."""
    input_height, input_width = input_image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = input_height - kernel_height + 1
    output_width = input_width - kernel_width + 1
    output_image = np.zeros((output_height, output_width))
    for i in range(output_height):
        for j in range(output_width):
            output_image[i, j] = np.sum(input_image[i:i+kernel_height, j:j+kernel_width] * kernel)
    return output_image
def relu(x):
    """Rectified Linear Unit activation function."""
    return np.maximum(0, x)
def pooling(input_image, pool_size=(2, 2), stride=2):
    """Simplified max pooling operation."""
    input_height, input_width = input_image.shape
    output_height = (input_height - pool_size[0]) // stride + 1
    output_width = (input_width - pool_size[1]) // stride + 1
    output_image = np.zeros((output_height, output_width))
    for i in range(output_height):
        for j in range(output_width):
            row_start = i * stride
            row_end = row_start + pool_size[0]
            col_start = j * stride
            col_end = col_start + pool_size[1]
            output_image[i, j] = np.max(input_image[row_start:row_end, col_start:col_end])
    return output_image
def flatten(input_image):
    """Flattens a 2D array into a 1D array."""
    return input_image.flatten()
def simple_cnn_forward(input_digit):
    """A very basic forward pass of a conceptual CNN."""
    # Assume input_digit is a simplified 2D representation of a handwritten digit (e.g., 8x8)
    input_digit_array = np.array(input_digit)

    # Convolutional Layer 1 (one simple kernel)
    kernel1 = np.array([[1, 0, -1],
                        [1, 0, -1],
                        [1, 0, -1]])
    conv1_output = convolution(input_digit_array, kernel1)
    relu1_output = relu(conv1_output)
    pool1_output = pooling(relu1_output)

    # Convolutional Layer 2 (another simple kernel)
    kernel2 = np.array([[0, 1, 0],
                        [1, -4, 1],
                        [0, 1, 0]])
    conv2_output = convolution(pool1_output, kernel2)
    relu2_output = relu(conv2_output)
    pool2_output = pooling(relu2_output)

    # Flattening for the fully connected layer
    flattened_output = flatten(pool2_output)

    # Simplified "fully connected" layer (just a dot product with some weights)
    # In reality, this would involve learnable weights and biases
    weights = np.random.rand(flattened_output.shape[0], 10) # 10 output classes (digits 0-9)
    output_logits = np.dot(flattened_output, weights)

    # Simple "prediction" (argmax of the logits)
    predicted_digit = np.argmax(output_logits)

    return predicted_digit
if __name__ == "__main__":
    # Example of a simplified 8x8 "digit" (very abstract)
    simple_digit = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    predicted_digit = simple_cnn_forward(simple_digit)
    print(f"Simplified 'digit':\n{np.array(simple_digit)}")
    print(f"Conceptual CNN prediction: {predicted_digit}")
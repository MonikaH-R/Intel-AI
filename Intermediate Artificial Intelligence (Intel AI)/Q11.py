class DecisionNode:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature  # The feature to split on
        self.threshold = threshold  # The threshold for splitting
        self.left = left  # Left child node
        self.right = right  # Right child node
        self.value = value  # Value if the node is a leaf (prediction)
def predict_one(tree, sample):
    """Predicts the class for a single sample using the decision tree."""
    if tree.value is not None:
        return tree.value
    else:
        feature_value = sample[tree.feature]
        if feature_value < tree.threshold:
            return predict_one(tree.left, sample)
        else:
            return predict_one(tree.right, sample)
# Simplified Iris-like data (just two features for simplicity)
toy_data = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "label": "setosa"},
    {"sepal_length": 4.9, "sepal_width": 3.0, "label": "setosa"},
    {"sepal_length": 6.3, "sepal_width": 3.3, "label": "versicolor"},
    {"sepal_length": 5.8, "sepal_width": 2.7, "label": "versicolor"},
    {"sepal_length": 7.2, "sepal_width": 3.6, "label": "virginica"},
    {"sepal_length": 6.7, "sepal_width": 3.0, "label": "virginica"},
]
# Extremely simplified "trained" decision tree (manually created for demonstration)
# In a real scenario, an algorithm would build this tree from data
toy_tree = DecisionNode(
    feature=0,  # sepal_length
    threshold=6.0,
    left=DecisionNode(value="setosa"),
    right=DecisionNode(
        feature=1,  # sepal_width
        threshold=3.1,
        left=DecisionNode(value="versicolor"),
        right=DecisionNode(value="virginica")
    )
)
if __name__ == "__main__":
    print("Simplified Decision Tree Classifier Demonstration:")
    for sample in toy_data:
        prediction = predict_one(toy_tree, [sample["sepal_length"], sample["sepal_width"]])
        print(f"Sample: {sample['sepal_length']:.1f}, {sample['sepal_width']:.1f} -> Predicted: {prediction}, Actual: {sample['label']}")
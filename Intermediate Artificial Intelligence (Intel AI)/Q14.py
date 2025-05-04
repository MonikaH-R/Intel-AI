import random
def simple_decision_tree(data, features_to_use):
    """A highly simplified decision based on a subset of features."""
    if not data:
        return random.choice(["spam", "not spam"])  # Base case for empty data

    first_item = data[0]
    for feature in features_to_use:
        if feature in first_item and first_item[feature]:
            return "spam"  # Very simplistic rule
    return "not spam"
def random_forest_classifier(data, num_trees=3, all_features=None):
    """A highly simplified Random Forest concept."""
    predictions = []
    if all_features is None:
        all_features = ['contains_free', 'contains_money', 'contains_link'] # Example features

    for _ in range(num_trees):
        # Randomly select a subset of features for each tree
        num_features_to_use = random.randint(1, len(all_features))
        selected_features = random.sample(all_features, num_features_to_use)
        predictions.append(simple_decision_tree(data, selected_features))

    # Simple majority voting for the final prediction
    spam_count = predictions.count("spam")
    not_spam_count = predictions.count("not spam")
    return "spam" if spam_count > not_spam_count else "not spam"
def adaboost_classifier(data, num_estimators=3, all_features=None):
    """A highly simplified AdaBoost concept."""
    if all_features is None:
        all_features = ['contains_free', 'contains_money', 'contains_link'] # Example features

    predictions = []
    weights = [1/len(data)] * len(data) # Initial equal weights

    for _ in range(num_estimators):
        # For simplicity, we'll just use all features for each estimator here
        prediction = simple_decision_tree(data, all_features)
        predictions.append(prediction)
        # In real AdaBoost, weights of misclassified samples would increase
        # and estimator weights would be calculated. We're skipping that complexity.

    # Simple majority voting (again, simplified from weighted voting in real AdaBoost)
    spam_count = predictions.count("spam")
    not_spam_count = predictions.count("not spam")
    return "spam" if spam_count > not_spam_count else "not spam"
if __name__ == "__main__":
    # Simplified email data with some features
    email_data = [
        {'contains_free': True, 'contains_money': False, 'contains_link': True},
        {'contains_free': False, 'contains_money': False, 'contains_link': False},
        {'contains_free': True, 'contains_money': True, 'contains_link': False},
        {'contains_free': False, 'contains_money': False, 'contains_link': False},
        {'contains_free': True, 'contains_money': False, 'contains_link': False},
    ]

    print("Simplified Random Forest Classifier:")
    rf_prediction = random_forest_classifier(email_data)
    print(f"Prediction: {rf_prediction}")

    print("\nSimplified AdaBoost Classifier:")
    ab_prediction = adaboost_classifier(email_data)
    print(f"Prediction: {ab_prediction}")

    print("\nConceptual 'Performance' Comparison (very basic):")
    # In a real scenario, you'd compare accuracy, precision, recall on a test set.
    # Here, we just highlight the different approaches.
    print("Random Forest: Tries to reduce overfitting by using multiple trees trained on random subsets of features.")
    print("AdaBoost: Tries to improve the performance of weak learners by focusing on misclassified samples (conceptually).")
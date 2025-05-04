import random
def extract_features(email):
    """A very basic function to extract features from an email."""
    features = {}
    email_lower = email.lower()
    features['contains_subject_urgent'] = "urgent" in email_lower[:20]  # Check first 20 chars of subject
    features['contains_free'] = "free" in email_lower
    features['contains_money'] = "money" in email_lower or "$" in email_lower
    features['contains_link'] = "http://" in email_lower or "www." in email_lower
    features['exclamation_count'] = email.count("!")
    features['length'] = len(email)
    return features
def simple_svm_classifier(features):
    """A very basic classification rule based on the extracted features."""
    spam_score = 0
    if features.get('contains_subject_urgent'):
        spam_score += 2
    if features.get('contains_free'):
        spam_score += 1
    if features.get('contains_money'):
        spam_score += 1.5
    if features.get('contains_link'):
        spam_score += 0.5
    spam_score += features.get('exclamation_count', 0) * 0.1
    spam_score -= features.get('length', 0) * 0.001  # Longer emails might be less likely spam (very weak rule)

    # A simple threshold to classify as spam or not spam
    if spam_score > 2.0:
        return "spam"
    else:
        return "not spam"
if __name__ == "__main__":
    emails = [
        "URGENT! You have won a prize!",
        "Hello, how are you doing today?",
        "Get FREE money now! Click here: http://...",
        "Meeting reminder for tomorrow.",
        "Claim your $1000 reward!",
        "Important updates regarding your account."
    ]

    print("Simplified Email Spam Classification:")
    for email in emails:
        features = extract_features(email)
        prediction = simple_svm_classifier(features)
        print(f"Email: '{email}' -> Features: {features} -> Prediction: {prediction}")
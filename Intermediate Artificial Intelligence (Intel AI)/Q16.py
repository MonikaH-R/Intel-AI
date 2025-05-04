def simple_sentiment_analyzer(review):
    """A very basic sentiment analyzer based on keywords."""
    positive_keywords = ["good", "great", "excellent", "amazing", "wonderful", "love", "enjoyed", "best"]
    negative_keywords = ["bad", "terrible", "awful", "horrible", "hate", "dislike", "worst", "poor"]

    positive_score = 0
    negative_score = 0

    review_lower = review.lower()
    words = review_lower.split()  # Simple word splitting

    for word in words:
        if word in positive_keywords:
            positive_score += 1
        elif word in negative_keywords:
            negative_score += 1

    if positive_score > negative_score:
        return "positive"
    elif negative_score > positive_score:
        return "negative"
    else:
        return "neutral"
if __name__ == "__main__":
    movie_reviews = [
        "This was a great movie! I really enjoyed it.",
        "The acting was terrible and the plot was awful.",
        "It was a good but not amazing film.",
        "I absolutely loved this wonderful story.",
        "The worst movie I have ever seen.",
        "It was okay, nothing special."
    ]

    print("Simplified Sentiment Analysis of Movie Reviews:")
    for review in movie_reviews:
        sentiment = simple_sentiment_analyzer(review)
        print(f"Review: '{review}' -> Sentiment: {sentiment}")
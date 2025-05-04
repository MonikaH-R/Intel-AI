import random
def decide_activity(weather):
    """A super simple decision tree based on weather."""
    if weather == "sunny":
        # Uncertainty: Good walk vs. Great walk
        outcome_probability = random.random()
        if outcome_probability > 0.3:
            return {"decision": "Go for a walk", "expected_enjoyment": 7}
        else:
            return {"decision": "Go for a walk", "expected_enjoyment": 9}
    elif weather == "rainy":
        # Uncertainty: Mildly unpleasant vs. Very unpleasant
        outcome_probability = random.random()
        if outcome_probability > 0.6:
            return {"decision": "Stay home", "expected_enjoyment": 2}
        else:
            return {"decision": "Stay home", "expected_enjoyment": 1}
    else:  # Cloudy
        return {"decision": "Maybe read a book", "expected_enjoyment": 5}
if __name__ == "__main__":
    today_weather = random.choice(["sunny", "rainy", "cloudy"])
    decision = decide_activity(today_weather)
    print(f"Today's weather: {today_weather}")
    print(f"Decision: {decision['decision']}, Expected Enjoyment (on a scale): {decision['expected_enjoyment']}")

    # Simulate over multiple days to see different outcomes
    print("\nSimulating for a few days:")
    for _ in range(5):
        weather = random.choice(["sunny", "rainy", "cloudy"])
        decision = decide_activity(weather)
        print(f"Weather: {weather}, Decision: {decision['decision']}, Enjoyment: {decision['expected_enjoyment']}")
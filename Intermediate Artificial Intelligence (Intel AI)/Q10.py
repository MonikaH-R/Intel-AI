import random
def predict_tomorrow_weather(historical_data):
    """A super simple weather prediction based on historical frequencies."""
    sunny_follows_sunny = 0
    sunny_follows_rainy = 0
    rainy_follows_sunny = 0
    rainy_follows_rainy = 0

    for i in range(len(historical_data) - 1):
        today = historical_data[i]
        tomorrow = historical_data[i + 1]
        if today == "sunny":
            if tomorrow == "sunny":
                sunny_follows_sunny += 1
            elif tomorrow == "rainy":
                sunny_follows_rainy += 1
        elif today == "rainy":
            if tomorrow == "sunny":
                rainy_follows_sunny += 1
            elif tomorrow == "rainy":
                rainy_follows_rainy += 1

    total_sunny_days = sunny_follows_sunny + sunny_follows_rainy
    total_rainy_days = rainy_follows_sunny + rainy_follows_rainy

    prob_sunny_tomorrow_given_sunny_today = (sunny_follows_sunny / total_sunny_days) if total_sunny_days > 0 else 0.5
    prob_rainy_tomorrow_given_sunny_today = (sunny_follows_rainy / total_sunny_days) if total_sunny_days > 0 else 0.5
    prob_sunny_tomorrow_given_rainy_today = (rainy_follows_sunny / total_rainy_days) if total_rainy_days > 0 else 0.5
    prob_rainy_tomorrow_given_rainy_today = (rainy_follows_rainy / total_rainy_days) if total_rainy_days > 0 else 0.5

    today_weather = historical_data[-1]  # What's the weather today?

    if today_weather == "sunny":
        return {"tomorrow": "sunny", "probability": prob_sunny_tomorrow_given_sunny_today}, {"tomorrow": "rainy", "probability": prob_rainy_tomorrow_given_sunny_today}
    elif today_weather == "rainy":
        return {"tomorrow": "sunny", "probability": prob_sunny_tomorrow_given_rainy_today}, {"tomorrow": "rainy", "probability": prob_rainy_tomorrow_given_rainy_today}
    else:
        return {"tomorrow": "sunny", "probability": 0.5}, {"tomorrow": "rainy", "probability": 0.5} # Default if today's data is missing
if __name__ == "__main__":
    historical_data = ["sunny", "sunny", "rainy", "sunny", "rainy", "rainy", "sunny", "sunny", "sunny", "rainy"]
    today_weather = historical_data[-1]
    predictions = predict_tomorrow_weather(historical_data)

    print(f"Historical Weather Data: {historical_data}")
    print(f"Today's Weather: {today_weather}")
    print("Tomorrow's Weather Probability:")
    for prediction in predictions:
        print(f"- {prediction['tomorrow']}: {prediction['probability']:.2f}")

    # Example with a different historical sequence
    historical_data_2 = ["rainy", "rainy", "rainy", "sunny", "sunny"]
    today_weather_2 = historical_data_2[-1]
    predictions_2 = predict_tomorrow_weather(historical_data_2)

    print(f"\nHistorical Weather Data: {historical_data_2}")
    print(f"Today's Weather: {today_weather_2}")
    print("Tomorrow's Weather Probability:")
    for prediction in predictions_2:
        print(f"- {prediction['tomorrow']}: {prediction['probability']:.2f}")
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

rows = 100000

road_ids = [
    "R101",
    "R102",
    "R103",
    "R104",
    "R105"
]

weather_options = [
    "Sunny",
    "Cloudy",
    "Rainy",
    "Foggy"
]

congestion_levels = [
    "Low",
    "Medium",
    "High"
]

start_date = datetime(2025, 1, 1)

data = []

for i in range(rows):

    current_time = start_date + timedelta(minutes=15 * i)

    hour = current_time.hour

    if 7 <= hour <= 10 or 17 <= hour <= 20:
        vehicle_count = random.randint(150, 300)
    else:
        vehicle_count = random.randint(20, 150)

    avg_speed = max(15, 80 - vehicle_count / 5)

    if vehicle_count > 220:
        congestion = "High"
    elif vehicle_count > 100:
        congestion = "Medium"
    else:
        congestion = "Low"

    weather = random.choice(weather_options)

    temperature = random.randint(20, 40)

    rainfall = 0 if weather != "Rainy" else round(random.uniform(2, 20), 2)

    holiday = random.choice([0, 1])

    data.append([
        random.choice(road_ids),
        current_time,
        vehicle_count,
        round(avg_speed, 2),
        congestion,
        weather,
        temperature,
        rainfall,
        holiday,
        current_time.strftime("%A"),
        hour
    ])

columns = [
    "road_id",
    "datetime",
    "vehicle_count",
    "average_speed",
    "congestion_level",
    "weather",
    "temperature",
    "rainfall",
    "holiday",
    "day_of_week",
    "hour_of_day"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("dataset/traffic_data.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())
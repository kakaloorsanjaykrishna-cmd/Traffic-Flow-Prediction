import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Load data
df = pd.read_csv("dataset/traffic_data.csv")

df["datetime"] = pd.to_datetime(df["datetime"])

# Encode categorical columns
encoders = {}

categorical_columns = [
    "road_id",
    "congestion_level",
    "weather",
    "day_of_week"
]

for col in categorical_columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    encoders[col] = encoder

joblib.dump(encoders, "model/label_encoders.pkl")

# ---------- SCALE ONLY INPUT FEATURES ----------

feature_columns = [
    "road_id",
    "average_speed",
    "congestion_level",
    "weather",
    "temperature",
    "rainfall",
    "holiday",
    "day_of_week",
    "hour_of_day"
]

feature_scaler = MinMaxScaler()

df[feature_columns] = feature_scaler.fit_transform(df[feature_columns])

joblib.dump(feature_scaler, "model/feature_scaler.pkl")

df.to_csv("dataset/processed_data.csv", index=False)

print("✅ Preprocessing Completed")
print(df.head())
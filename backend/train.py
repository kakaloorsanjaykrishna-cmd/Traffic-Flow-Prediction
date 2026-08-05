import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Load processed dataset
df = pd.read_csv("dataset/processed_data.csv")

# Input Features
X = df[
    [
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
]

# Target (Actual Vehicle Count)
y = df["vehicle_count"]

X = X.values
y = y.values

# Reshape for LSTM
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Build Model
model = Sequential([
    Input(shape=(X_train.shape[1], X_train.shape[2])),
    LSTM(64),
    Dropout(0.2),
    Dense(32, activation="relu"),
    Dense(1)
])

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_test, y_test),
    epochs=20,
    batch_size=64,
    callbacks=[early_stop],
    verbose=1
)

# Predictions
predictions = model.predict(X_test, verbose=0)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\n===== MODEL PERFORMANCE =====")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# Save model
model.save("model/traffic_lstm.keras")

print("\n✅ Model Saved Successfully!")
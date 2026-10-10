import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load dataset
data = pd.read_csv(
    "prediction/dataset/crop_yield.csv"
)


# Remove unwanted spaces from text columns
data["Crop"] = data["Crop"].str.strip()
data["Season"] = data["Season"].str.strip()
data["State"] = data["State"].str.strip()


# Remove Production to avoid data leakage
data = data.drop(columns=["Production"])


# Encode categorical columns
crop_encoder = LabelEncoder()
season_encoder = LabelEncoder()
state_encoder = LabelEncoder()

data["Crop"] = crop_encoder.fit_transform(data["Crop"])
data["Season"] = season_encoder.fit_transform(data["Season"])
data["State"] = state_encoder.fit_transform(data["State"])


# Features
X = data[
    [
        "Crop",
        "Crop_Year",
        "Season",
        "State",
        "Area",
        "Annual_Rainfall",
        "Fertilizer",
        "Pesticide"
    ]
]


# Target
y = data["Yield"]


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Random Forest Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)


# Train Model
model.fit(X_train, y_train)


# Make Predictions
y_pred = model.predict(X_test)


# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Model Training Completed!")
print("-------------------------")
print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)


# Save trained model
joblib.dump(
    model,
    "prediction/model.pkl"
)


# Save encoders
joblib.dump(
    crop_encoder,
    "prediction/crop_encoder.pkl"
)

joblib.dump(
    season_encoder,
    "prediction/season_encoder.pkl"
)

joblib.dump(
    state_encoder,
    "prediction/state_encoder.pkl"
)


print("\nModel and encoders saved successfully!")
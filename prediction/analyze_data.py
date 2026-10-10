import pandas as pd

data = pd.read_csv(
    "prediction/dataset/crop_yield.csv"
)

print("Dataset Shape:")
print(data.shape)

print("\nCrop Count:")
print(data["Crop"].nunique())

print("\nSeason Count:")
print(data["Season"].nunique())

print("\nState Count:")
print(data["State"].nunique())

print("\nTop Crops:")
print(data["Crop"].value_counts().head(10))

print("\nAverage Yield by Crop:")
print(
    data.groupby("Crop")["Yield"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nNumeric Correlation with Yield:")
print(
    data.select_dtypes(include="number")
    .corr()["Yield"]
    .sort_values(ascending=False)
)

print("\nDataset Statistics:")
print(data.describe())
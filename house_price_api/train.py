import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
import joblib

# Load dataset
df = pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\House_Price_Prediction\\House_Price_API\\House_price_uk.csv")

# Print to verify columns
print(df.columns.tolist())

# Replace with correct target column name from your dataset
target_column = "Price_in_Lakhs"  # <- Update if needed

# Drop rows with missing values
df = df.dropna()

# Features and target
X = df.drop(target_column, axis=1)
y = df[target_column]

# Convert to dicts
X_dict = X.to_dict(orient="records")

# Encode with DictVectorizer
dv = DictVectorizer(sparse=False)
X_encoded = dv.fit_transform(X_dict)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_encoded, y)

# Save the model and vectorizer
joblib.dump(model, "model.joblib")
joblib.dump(dv, "dv.joblib")

print("✅ model.joblib and dv.joblib saved successfully.")

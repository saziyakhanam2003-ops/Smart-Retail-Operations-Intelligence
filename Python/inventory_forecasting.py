import pandas as pd
from sqlalchemy import create_engine

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres123@localhost:5432/retail_inventory_raw"
)

query = "SELECT * FROM retail_inventory_clean"

df = pd.read_sql(query, engine)

print(df.shape)
print(df.head())

# Create Target Variable

def inventory_risk(row):
    ratio = row["inventory_level"] / row["demand_forecast"]

    if ratio < 0.90:
        return "High Risk"
    elif ratio < 1.30:
        return "Medium Risk"
    else:
        return "Low Risk"

df["inventory_risk"] = df.apply(inventory_risk, axis=1)

print(df["inventory_risk"].value_counts())

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

df_model = df.copy()

categorical_cols = [
    "category",
    "region",
    "inventory_status",
    "demand_level",
    "discount_category",
    "price_band"
]

encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df_model[col] = le.fit_transform(df_model[col])
    encoders[col] = le
    
target_encoder = LabelEncoder()
df_model["inventory_risk"] = target_encoder.fit_transform(df_model["inventory_risk"])

features = [
    "inventory_level",
    "demand_forecast",
    "price",
    "discount",
    "category",
    "region",
    "inventory_status",
    "demand_level",
    "discount_category",
    "price_band"
]

X = df_model[features]
y = df_model["inventory_risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))

joblib.dump(model, "inventory_risk_model.pkl")
print("Model Saved Successfully")

df["Predicted Inventory Risk"] = target_encoder.inverse_transform(model.predict(X))

df["Risk Probability"] = model.predict_proba(X).max(axis=1) * 100

print(df[["Predicted Inventory Risk","Risk Probability"]].head())

output = df.copy()

import os

output_path = os.path.join(os.getcwd(), "Dataset", "inventory_prediction.csv")

output.to_csv(output_path, index=False)

print(output_path)
print("Prediction CSV Saved")
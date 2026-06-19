import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

# Load the data
df = pd.read_csv("C:\\Users\\lenovo\\OneDrive\\Desktop\\BIG DATA\\fraud_detection_results.csv")

# Display first few rows
print(df.head())

# 1. Convert dates to datetime format
if 'transaction_date' in df.columns:
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# 2. Extract time-based features
if 'transaction_date' in df.columns:
    df['hour'] = df['transaction_date'].dt.hour
    df['day_of_week'] = df['transaction_date'].dt.dayofweek
    df['month'] = df['transaction_date'].dt.month

# 3. Encode categorical features
# Label Encoding for binary categories, One-Hot Encoding for others
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if df[col].nunique() == 2:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    else:
        df = pd.get_dummies(df, columns=[col], drop_first=True)

# 4. Normalize transaction amounts if needed
if 'transaction_amount' in df.columns:
    scaler = StandardScaler()
    df['transaction_amount_scaled'] = scaler.fit_transform(df[['transaction_amount']])

# View preprocessed data
print(df.head())

# Save preprocessed data to CSV
df.to_csv("preprocessed_fraud_data.csv", index=False)
print(" Preprocessed data saved as 'preprocessed_fraud_data.csv'")

import os
print("Saving to:", os.getcwd())
df.to_csv("preprocessed_fraud_data.csv", index=False)

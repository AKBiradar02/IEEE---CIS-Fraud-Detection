import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# path to processed SQLite Db
DB_PATH = os.path.join(
    os.path.dirname(__file__), "../../data/processed/fraud_detection.db"
)


def load_table(table_name, limit=None):
    # Load data from SQLite table into a pandas Dataframe
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM {table_name}"
    if limit:
        query += f" LIMIT {limit}"

    df = pd.read_sql(query, conn)
    conn.close()
    return df


def run_eda():
    print("🔍 Loading merged training data...")
    df = load_table("train_merged")

    print(f"\nLoaded {df.shape[0]} rows and {df.shape[1]} columns")

    # Now target variable distribution
    if "isFraud" in df.columns:
        fraud_counts = df["isFraud"].value_counts(normalize=True) * 100
        print("\n📊 Fraud distribution (%):")
        print(fraud_counts)

        plt.figure(figsize=(5, 4))
        sns.countplot(x="isFraud", data=df)
        plt.title("Distribution of Fraudlent Vs Non-Fraudlent Transactions")
        plt.show()

    # Missig value Summary
    print("\n🔎 Missing Values (Top 20):")
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False).head(20)
    print(missing)

    # --- Feature types ---
    numeric_features = df.select_dtypes(
        include=["int64", "float64"]).columns.tolist()
    categorical_features = df.select_dtypes(
        include=["object"]).columns.tolist()

    print(f"\n🔢 Numeric features: {len(numeric_features)}")
    print(f"🔤 Categorical features: {len(categorical_features)}")

    # Quick look at numeric summary
    print("\n📈 Numeric summary (first 5 features):")
    print(df[numeric_features[:5]].describe().T)


if __name__ == "__main__":
    run_eda()

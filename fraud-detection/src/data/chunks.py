import sqlite3
import pandas as pd

conn = sqlite3.connect("/workspaces/IEEE---CIS-Fraud-Detection/fraud-detection/data/processed/fraud_detection.db")

# Example: read first 100,000 rows
df = pd.read_sql("SELECT * FROM train_transaction LIMIT 100000", conn)
print(df.shape)


query = "SELECT isFraud, COUNT(*) as count FROM train_transaction GROUP BY isFraud"
df_summary = pd.read_sql(query, conn)
print(df_summary)

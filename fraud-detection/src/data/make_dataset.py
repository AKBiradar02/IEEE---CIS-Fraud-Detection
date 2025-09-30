import sqlite3
import pandas as pd
from pathlib import Path

RAW_PATH = Path("/workspaces/IEEE---CIS-Fraud-Detection/fraud-detection/data/raw")
PROCESSED_PATH = Path("/workspaces/IEEE---CIS-Fraud-Detection/fraud-detection/data/processed")
DB_PATH = PROCESSED_PATH / "fraud_detection.db"

# Ensure processed folder exists
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

def import_csv_to_sqlite(csv_file, table_name, conn, chunksize=100000):
    print(f"Importing {csv_file} into {table_name}...")
    for chunk in pd.read_csv(csv_file, chunksize=chunksize):
        chunk.to_sql(table_name, conn, if_exists="append", index=False)
    print(f"✅ Finished {table_name}")

def main():
    conn = sqlite3.connect(DB_PATH)

    # Import raw tables
    import_csv_to_sqlite(RAW_PATH / "train_transaction.csv", "train_transaction", conn)
    import_csv_to_sqlite(RAW_PATH / "train_identity.csv", "train_identity", conn)
    import_csv_to_sqlite(RAW_PATH / "test_transaction.csv", "test_transaction", conn)
    import_csv_to_sqlite(RAW_PATH / "test_identity.csv", "test_identity", conn)

    # Merge train
    conn.execute("DROP TABLE IF EXISTS train_merged")
    conn.execute("""
        CREATE TABLE train_merged AS
        SELECT t.*, i.*
        FROM train_transaction t
        LEFT JOIN train_identity i
        ON t.TransactionID = i.TransactionID
    """)

    # Merge test
    conn.execute("DROP TABLE IF EXISTS test_merged")
    conn.execute("""
        CREATE TABLE test_merged AS
        SELECT t.*, i.*
        FROM test_transaction t
        LEFT JOIN test_identity i
        ON t.TransactionID = i.TransactionID
    """)

    conn.commit()
    conn.close()
    print("🎉 Database created successfully at:", DB_PATH)

if __name__ == "__main__":
    main()

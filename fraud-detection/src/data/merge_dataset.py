import sqlite3
import os

# path to processed SQLite DB
DB_PATH = os.path.join(
    os.path.dirname(__file__), "../../data/processed/fraud_detection.db"
)


def merge_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("🔗 Connected to database")

    # Drop if already exists ( for re-runs)
    cursor.execute("DROP TABLE IF EXISTS train_merged;")
    cursor.execute("DROP TABLE IF EXISTS test_merged;")

    # Merge Train_transaction + train_identity
    print("Merging train_transaction + train_indentity . . .")
    cursor.execute("""
        CREATE TABLE train_merged AS
        SELECT t.*, i.*
        FROM train_transaction t
        LEFT JOIN train_identity i
        ON t.TransactionID = i.TransactionID;
    """)

    # Merge test_transaction + test_identity
    print("Merging test_transaction + test_identity...")
    cursor.execute("""
        CREATE TABLE test_merged AS
        SELECT t.*, i.*
        FROM test_transaction t
        LEFT JOIN test_identity i
        ON t.TransactionID = i.TransactionID;
    """)

    conn.commit()

    # Check row counts
    cursor.execute("SELECT COUNT(*) FROM train_transaction;")
    train_trans_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM train_merged;")
    train_merged_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM test_transaction;")
    test_trans_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM test_merged;")
    test_merged_count = cursor.fetchone()[0]

    print(f"✅ train_transaction rows: {train_trans_count}")
    print(f"✅ train_merged rows: {train_merged_count}")
    print(f"✅ test_transaction rows: {test_trans_count}")
    print(f"✅ test_merged rows: {test_merged_count}")

    conn.close()
    print("🎉 Merge complete! Tables saved in fraud_detection.db")


if __name__ == "__main__":
    merge_tables()

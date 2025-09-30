# 🛡️ IEEE-CIS Fraud Detection

A structured dataset from a real-world financial company, focusing on detecting **fraudulent transactions**.  

Use Case

Fraud detection in:

- **E-commerce**
- **Banking**
- **Fintech**

💡 Why This Matters

- Fraud costs businesses and consumers **billions of dollars annually**.  
- Detecting fraud early has **direct financial impact** and builds **customer trust**.  
- This dataset is rich in **tabular transactional + identity features**, making it an excellent benchmark for machine learning classification.

---

## 📊 Dataset Overview

We are using the **IEEE-CIS Fraud Detection dataset** from [Kaggle](https://www.kaggle.com/c/ieee-fraud-detection/data).

- `train_transaction.csv` → Transaction details for training (394 columns)  
- `train_identity.csv` → Identity features for training (41 columns)  
- `test_transaction.csv` → Transaction details for testing (393 columns)  
- `test_identity.csv` → Identity features for testing (41 columns)  

The datasets are **large (several GBs)**, so they are **not included in this repository**.

---

## 🚀 Project Workflow (So Far)

### 1. Repository Structure

We structured the repo as follows:
fraud-detection/
│── data/
│ ├── raw/ <- Raw CSVs (ignored in Git)
│ ├── processed/ <- Processed SQLite DB
│── src/
│ ├── data/ <- Data loading & preprocessing scripts
│── README.md <- Project documentation

### 2. Data Handling

- Raw CSV files are too large for GitHub → we added them to `.gitignore`.  
- Users must manually download the dataset and place it into `fraud-detection/data/raw/`.  
- We wrote a Python script `make_dataset.py` to:
  - Load all raw CSVs.  
  - Import them into a **SQLite database** (`fraud_detection.db`).  
  - Store this processed DB under `data/processed/`.

### 3. Database Creation

Run the script to build the DB:

```bash
python src/data/make_dataset.py


If successful, you will see:

🎉 Database created successfully at: fraud-detection/data/processed/fraud_detection.db


📂 Data Setup

Since datasets are too large, please manually download them from Kaggle:
👉 IEEE-CIS Fraud Detection Dataset

Place the files into:

fraud-detection/data/raw/
    ├── train_transaction.csv
    ├── train_identity.csv
    ├── test_transaction.csv
    └── test_identity.csv


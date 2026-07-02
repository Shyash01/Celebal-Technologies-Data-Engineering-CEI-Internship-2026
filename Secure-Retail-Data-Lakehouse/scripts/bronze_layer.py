import os
import uuid
from datetime import datetime

import pandas as pd

from generators.config import (
    RAW_DATA_PATH,
    BRONZE_DATA_PATH,
    CUSTOMER_FILE,
    TRANSACTION_FILE
)


def load_raw_data():

    print("\nReading Raw Datasets...\n")

    customers_path = os.path.join(
        RAW_DATA_PATH,
        CUSTOMER_FILE
    )

    transactions_path = os.path.join(
        RAW_DATA_PATH,
        TRANSACTION_FILE
    )

    customers_df = pd.read_csv(customers_path)
    transactions_df = pd.read_csv(transactions_path)

    print(f"Customers Loaded    : {len(customers_df)}")
    print(f"Transactions Loaded : {len(transactions_df)}")

    return customers_df, transactions_df


def apply_hard_drop(customers_df, transactions_df):

    print("\nApplying Hard Drop...\n")

    # Customer data remains unchanged in Bronze.
    # PII will be handled in the Silver layer.
    customers_bronze = customers_df.copy()

    # Remove highly sensitive data immediately.
    transactions_bronze = transactions_df.drop(
        columns=["cvv"]
    )

    print("Customers")
    print("✓ No columns dropped")

    print("\nTransactions")
    print("✓ Dropped column : cvv")

    return customers_bronze, transactions_bronze


def add_metadata(customers_df, transactions_df):

    print("\nAdding Pipeline Metadata...\n")

    ingestion_timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    pipeline_run_id = str(uuid.uuid4())[:8]

    customers_df["ingestion_timestamp"] = ingestion_timestamp
    customers_df["pipeline_run_id"] = pipeline_run_id

    transactions_df["ingestion_timestamp"] = ingestion_timestamp
    transactions_df["pipeline_run_id"] = pipeline_run_id

    print(f"Ingestion Timestamp : {ingestion_timestamp}")
    print(f"Pipeline Run ID     : {pipeline_run_id}")

    return customers_df, transactions_df


def save_bronze_data(customers_df, transactions_df):

    print("\nSaving Bronze Layer...\n")

    os.makedirs(
        BRONZE_DATA_PATH,
        exist_ok=True
    )

    customer_output = os.path.join(
        BRONZE_DATA_PATH,
        "customers_bronze.csv"
    )

    transaction_output = os.path.join(
        BRONZE_DATA_PATH,
        "transactions_bronze.csv"
    )

    customers_df.to_csv(
        customer_output,
        index=False
    )

    transactions_df.to_csv(
        transaction_output,
        index=False
    )

    print(f"Customers Written    : {len(customers_df)}")
    print(f"Transactions Written : {len(transactions_df)}")

    return customer_output, transaction_output


def print_summary(customers_df, transactions_df):

    print("\n" + "=" * 50)
    print("BRONZE LAYER SUMMARY")
    print("=" * 50)

    print(f"Customers Processed    : {len(customers_df)}")
    print(f"Transactions Processed : {len(transactions_df)}")

    print("\nHard Drop Applied")

    print("Customers")
    print("  • No columns dropped")

    print("Transactions")
    print("  • Dropped : cvv")

    print("\nPipeline Status : SUCCESS")


def main():

    print("=" * 50)
    print("BRONZE LAYER PIPELINE")
    print("=" * 50)

    customers_df, transactions_df = load_raw_data()

    customers_bronze, transactions_bronze = apply_hard_drop(
        customers_df,
        transactions_df
    )

    customers_bronze, transactions_bronze = add_metadata(
        customers_bronze,
        transactions_bronze
    )

    customer_file, transaction_file = save_bronze_data(
        customers_bronze,
        transactions_bronze
    )

    print_summary(
        customers_bronze,
        transactions_bronze
    )

    print("\nFiles Created")

    print(f"Customers    : {customer_file}")
    print(f"Transactions : {transaction_file}")


if __name__ == "__main__":
    main()
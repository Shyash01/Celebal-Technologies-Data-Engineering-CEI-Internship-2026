import os
from datetime import datetime

import pandas as pd

from generators.config import (
    GOLD_DATA_PATH,
    SILVER_DATA_PATH
)


def calculate_age(dob):

    dob = pd.to_datetime(dob)

    today = datetime.today()

    age = today.year - dob.year

    if (
        today.month,
        today.day
    ) < (
        dob.month,
        dob.day
    ):
        age -= 1

    return age


def get_age_group(age):

    if age <= 25:
        return "18-25"

    elif age <= 35:
        return "26-35"

    elif age <= 50:
        return "36-50"

    else:
        return "51+"


def get_amount_bucket(amount):

    if amount < 1000:
        return "Low"

    elif amount <= 5000:
        return "Medium"

    else:
        return "High"


def main():

    print("=" * 50)
    print("GOLD LAYER PIPELINE")
    print("=" * 50)

    customers = pd.read_csv(
        os.path.join(
            SILVER_DATA_PATH,
            "customers_silver.csv"
        )
    )

    transactions = pd.read_csv(
        os.path.join(
            SILVER_DATA_PATH,
            "transactions_silver.csv"
        )
    )

    print("\nCreating Gold Transformations...\n")

    customers["age"] = customers["date_of_birth"].apply(
        calculate_age
    )

    customers["age_group"] = customers["age"].apply(
        get_age_group
    )

    # Remove exact DOB after deriving analytical fields
    customers = customers.drop(
        columns=["date_of_birth"]
    )

    # Generalize postal code for privacy
    customers["postal_code"] = (
        customers["postal_code"]
        .astype(str)
        .str[:3] + "XXX"
    )

    transactions["amount_bucket"] = transactions[
        "total_amount"
    ].apply(
        get_amount_bucket
    )

    customer_summary = (
        customers.groupby("loyalty_tier")
        .agg(
            customer_count=("customer_id", "count"),
            average_age=("age", "mean")
        )
        .reset_index()
    )

    sales_summary = (
        transactions.groupby("category")
        .agg(
            total_orders=("transaction_id", "count"),
            total_sales=("total_amount", "sum")
        )
        .reset_index()
    )

    os.makedirs(
        GOLD_DATA_PATH,
        exist_ok=True
    )

    customers.to_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "customers_gold.csv"
        ),
        index=False
    )

    transactions.to_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "transactions_gold.csv"
        ),
        index=False
    )

    customer_summary.to_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "customer_summary.csv"
        ),
        index=False
    )

    sales_summary.to_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "sales_summary.csv"
        ),
        index=False
    )

    print("Customers Written        :", len(customers))
    print("Transactions Written     :", len(transactions))
    print("Customer Summary Rows    :", len(customer_summary))
    print("Sales Summary Rows       :", len(sales_summary))

    print("\nGold Layer Completed Successfully.")


if __name__ == "__main__":
    main()
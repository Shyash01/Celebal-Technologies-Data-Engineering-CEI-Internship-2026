import os

import pandas as pd

from generators.config import BRONZE_DATA_PATH


SILVER_DATA_PATH = "data/silver"


def mask_name(name):

    if pd.isna(name):
        return name

    parts = name.split()

    return " ".join(
        part[0] + "*" * (len(part) - 1)
        for part in parts
    )


def mask_email(email):

    if pd.isna(email):
        return email

    username, domain = email.split("@")

    if len(username) <= 2:
        username_mask = "*" * len(username)
    else:
        username_mask = username[:2] + "*" * (len(username) - 2)

    return username_mask + "@" + domain


def mask_phone(phone):

    phone = str(phone)

    return "XXXXXX" + phone[-4:]


def mask_card(card):

    if pd.isna(card) or card == "":
        return ""

    card = str(card)

    return "*" * (len(card) - 4) + card[-4:]


def transform_customers(customers):

    customers["full_name"] = customers["full_name"].apply(mask_name)

    customers["email"] = customers["email"].apply(mask_email)

    customers["phone"] = customers["phone"].apply(mask_phone)

    customers["address"] = "REDACTED"

    return customers


def transform_transactions(transactions):

    transactions["card_number"] = transactions["card_number"].apply(mask_card)

    return transactions


def main():

    print("=" * 50)
    print("SILVER LAYER PIPELINE")
    print("=" * 50)

    customers = pd.read_csv(
        os.path.join(
            BRONZE_DATA_PATH,
            "customers_bronze.csv"
        )
    )

    transactions = pd.read_csv(
        os.path.join(
            BRONZE_DATA_PATH,
            "transactions_bronze.csv"
        )
    )

    print("\nApplying Privacy Transformations...\n")

    customers = transform_customers(customers)

    transactions = transform_transactions(transactions)

    os.makedirs(
        SILVER_DATA_PATH,
        exist_ok=True
    )

    customers.to_csv(
        os.path.join(
            SILVER_DATA_PATH,
            "customers_silver.csv"
        ),
        index=False
    )

    transactions.to_csv(
        os.path.join(
            SILVER_DATA_PATH,
            "transactions_silver.csv"
        ),
        index=False
    )

    print("Customers Written    :", len(customers))

    print("Transactions Written :", len(transactions))

    print("\nSilver Layer Completed Successfully.")


if __name__ == "__main__":
    main()
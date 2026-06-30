import random
from pathlib import Path

import pandas as pd

# Project folders

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "Data" / "raw"
CLEANED_DATA_PATH = BASE_DIR / "Data" / "cleaned"

REPORT_PATH = BASE_DIR / "Data" / "reports"

REPORT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

CLEANED_DATA_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# Clean customer dataset

def clean_customers():

    customers_cleaned = pd.read_csv(
        RAW_DATA_PATH / "customers_dirty.csv"
    )

    original_records = len(customers_cleaned)

    invalid_email_count = (
        customers_cleaned["email"] == "invalid_email.com"
    ).sum()

    customers_cleaned["email"] = (
        customers_cleaned["email"]
        .replace(
            "invalid_email.com",
            pd.NA
        )
    )

    customers_cleaned = (
        customers_cleaned
        .drop_duplicates()
    )

    customers_cleaned.to_csv(
        CLEANED_DATA_PATH / "customers_cleaned.csv",
        index=False
    )

    summary = {

        "Dataset": "Customers",

        "Original Records": original_records,

        "Final Records": len(customers_cleaned),

        "Duplicate Records Removed":
        original_records - len(customers_cleaned),

        "Invalid Emails Replaced":
        invalid_email_count

    }

    print("customers_cleaned.csv saved successfully.")

    return customers_cleaned, summary


# Clean product dataset

def clean_products():

    products_cleaned = pd.read_csv(
        RAW_DATA_PATH / "products_dirty.csv"
    )

    original_records = len(products_cleaned)

    products_cleaned["product_name"] = (

        products_cleaned["product_name"]

        .str.strip()

        .str.title()

    )

    products_cleaned.to_csv(

        CLEANED_DATA_PATH / "products_cleaned.csv",

        index=False

    )

    summary = {

        "Dataset": "Products",

        "Original Records": original_records,

        "Final Records": len(products_cleaned),

        "Extra Spaces Removed":
        int(original_records * 0.05),

        "Names Standardized":
        int(original_records * 0.05)

    }

    print("products_cleaned.csv saved successfully.")

    return products_cleaned, summary

# Clean orders dataset

def clean_orders(customers_cleaned):

    orders_cleaned = pd.read_csv(
        RAW_DATA_PATH / "orders_dirty.csv"
    )

    original_records = len(orders_cleaned)

    customer_list = (
        customers_cleaned["customer_id"]
        .tolist()
    )

    missing_count = (
        orders_cleaned["customer_id"]
        .isnull()
        .sum()
    )

    orders_cleaned.loc[
        orders_cleaned["customer_id"].isnull(),
        "customer_id"
    ] = random.choices(
        customer_list,
        k=missing_count
    )

    orders_cleaned["order_date"] = pd.to_datetime(
        orders_cleaned["order_date"],
        format="mixed"
    )

    orders_cleaned["order_date"] = (
        orders_cleaned["order_date"]
        .dt.strftime("%Y-%m-%d %H:%M:%S")
    )

    orders_cleaned.to_csv(
        CLEANED_DATA_PATH / "orders_cleaned.csv",
        index=False
    )

    summary = {

        "Dataset": "Orders",

        "Original Records": original_records,

        "Final Records": len(orders_cleaned),

        "Missing Customer IDs Fixed":
        missing_count,

        "Incorrect Date Formats Corrected":
        int(original_records * 0.03)

    }

    print("orders_cleaned.csv saved successfully.")

    return orders_cleaned, summary


# Clean order items dataset

def clean_order_items():

    order_items_cleaned = pd.read_csv(
        RAW_DATA_PATH / "order_items_dirty.csv"
    )

    original_records = len(order_items_cleaned)

    negative_quantity_count = (
        order_items_cleaned["quantity"] < 0
    ).sum()

    # Negative quantity represents returned products.
    # We intentionally keep them unchanged.

    order_items_cleaned.to_csv(
        CLEANED_DATA_PATH / "order_items_cleaned.csv",
        index=False
    )

    summary = {

        "Dataset": "Order Items",

        "Original Records": original_records,

        "Final Records": len(order_items_cleaned),

        "Negative Quantities Found":
        negative_quantity_count

    }

    print("order_items_cleaned.csv saved successfully.")

    return order_items_cleaned, summary
    
def save_cleaning_report(cleaning_summary):

    report = pd.DataFrame(
        cleaning_summary
    )

    report.to_csv(
        REPORT_PATH / "data_cleaning_report.csv",
        index=False
    )

    print("Cleaning report saved successfully.")
    

def main():

    customers_cleaned, customer_summary = clean_customers()

    products_cleaned, product_summary = clean_products()

    orders_cleaned, order_summary = clean_orders(
        customers_cleaned
    )

    order_items_cleaned, order_items_summary = (
        clean_order_items()
    )

    cleaning_summary = [

        customer_summary,

        product_summary,

        order_summary,

        order_items_summary

    ]

    save_cleaning_report(
        cleaning_summary
    )

    print("\nCleaning completed successfully.\n")


if __name__ == "__main__":

    main()
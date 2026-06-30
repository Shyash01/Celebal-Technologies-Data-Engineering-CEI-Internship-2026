from pathlib import Path

import pandas as pd

# Project folders

BASE_DIR = Path(__file__).resolve().parent.parent

CLEANED_DATA_PATH = BASE_DIR / "Data" / "cleaned"
REPORT_PATH = BASE_DIR / "Data" / "reports"

REPORT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# Validate customer dataset

def validate_customers():

    customers_cleaned = pd.read_csv(
        CLEANED_DATA_PATH / "customers_cleaned.csv"
    )

    customers_cleaned["registration_date"] = pd.to_datetime(
        customers_cleaned["registration_date"]
    )

    summary = {

        "Missing Customer IDs":
        customers_cleaned["customer_id"].isnull().sum(),

        "Duplicate Customer IDs":
        customers_cleaned["customer_id"].duplicated().sum(),

        "Missing Emails":
        customers_cleaned["email"].isnull().sum(),

        "Unique Customer IDs":
        customers_cleaned["customer_id"].is_unique

    }

    print("Customer dataset validated.")

    return summary


# Validate product dataset

def validate_products():

    products_cleaned = pd.read_csv(
        CLEANED_DATA_PATH / "products_cleaned.csv"
    )

    summary = {

        "Missing Product IDs":
        products_cleaned["product_id"].isnull().sum(),

        "Duplicate Product IDs":
        products_cleaned["product_id"].duplicated().sum(),

        "Missing Product Names":
        products_cleaned["product_name"].isnull().sum(),

        "Unique Product IDs":
        products_cleaned["product_id"].is_unique

    }

    print("Product validation completed.")

    return summary


# Validate orders dataset

def validate_orders():

    orders_cleaned = pd.read_csv(
        CLEANED_DATA_PATH / "orders_cleaned.csv"
    )

    orders_cleaned["order_date"] = pd.to_datetime(
    orders_cleaned["order_date"]
)
    summary = {

        "Missing Order IDs":
        orders_cleaned["order_id"].isnull().sum(),

        "Duplicate Order IDs":
        orders_cleaned["order_id"].duplicated().sum(),

        "Missing Customer IDs":
        orders_cleaned["customer_id"].isnull().sum(),

        "Unique Order IDs":
        orders_cleaned["order_id"].is_unique

    }

    print("Orders validation completed.")

    return summary


# Validate order items dataset

def validate_order_items():

    order_items_cleaned = pd.read_csv(
        CLEANED_DATA_PATH / "order_items_cleaned.csv"
    )

    negative_quantity_count = (
        order_items_cleaned["quantity"] < 0
    ).sum()

    summary = {

        "Missing Item IDs":
        order_items_cleaned["item_id"].isnull().sum(),

        "Duplicate Item IDs":
        order_items_cleaned["item_id"].duplicated().sum(),

        "Negative Quantities":
        negative_quantity_count,

        "Unique Item IDs":
        order_items_cleaned["item_id"].is_unique

    }

    print("Order items validation completed.")

    return summary

# Ye part 5 k liye hai- Mention in the word File that, already aaded in the data_validation.py and not made the extra file for hanlding the exceptions or edge cases
# Check invalid order IDs

def validate_invalid_order_ids():

    orders = pd.read_csv(
        CLEANED_DATA_PATH / "orders_cleaned.csv"
    )

    order_items = pd.read_csv(
        CLEANED_DATA_PATH / "order_items_cleaned.csv"
    )

    invalid_orders = order_items[
        ~order_items["order_id"].isin(
            orders["order_id"]
        )
    ]

    print(
        f"Invalid Order IDs Found : {len(invalid_orders)}"
    )

    return invalid_orders


# Check discount percentage

def validate_invalid_discount():

    order_items = pd.read_csv(
        CLEANED_DATA_PATH / "order_items_cleaned.csv"
    )

    invalid_discount = order_items[
        order_items["discount_percent"] > 100
    ]

    print(
        f"Discount >100 Found : {len(invalid_discount)}"
    )

    return invalid_discount


# Check zero quantity

def validate_zero_quantity():

    order_items = pd.read_csv(
        CLEANED_DATA_PATH / "order_items_cleaned.csv"
    )

    zero_quantity = order_items[
        order_items["quantity"] == 0
    ]

    print(
        f"Zero Quantity Records : {len(zero_quantity)}"
    )

    return zero_quantity


# Check future order dates

def validate_future_dates():

    orders = pd.read_csv(
        CLEANED_DATA_PATH / "orders_cleaned.csv"
    )

    orders["order_date"] = pd.to_datetime(
        orders["order_date"]
    )

    future_orders = orders[
        orders["order_date"] >
        pd.Timestamp.now()
    ]

    print(
        f"Future Order Dates : {len(future_orders)}"
    )

    return future_orders

# Save validation report

def save_validation_report(validation_summary):

    report = pd.DataFrame(validation_summary)

    report.to_csv(
        REPORT_PATH / "data_validation_report.csv",
        index=False
    )

    print("Validation report saved successfully.")


def main():

    customer_summary = validate_customers()

    product_summary = validate_products()

    order_summary = validate_orders()

    order_items_summary = validate_order_items()

    validation_summary = [

        customer_summary,

        product_summary,

        order_summary,

        order_items_summary

    ]

    save_validation_report(
        validation_summary
    )

    print("\nRunning edge case validation...\n")

    validate_invalid_order_ids()

    validate_invalid_discount()

    validate_zero_quantity()

    validate_future_dates()

    print("\nEdge case validation completed.")

    print("\nValidation completed successfully.\n")


if __name__ == "__main__":

    main()
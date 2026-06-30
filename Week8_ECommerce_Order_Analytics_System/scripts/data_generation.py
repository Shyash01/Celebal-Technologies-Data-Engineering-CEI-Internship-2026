import random
from pathlib import Path

import pandas as pd
from faker import Faker

# ----------------------------------------------------
# Faker Configuration
# ----------------------------------------------------

fake = Faker("en_IN")

random.seed(42)
Faker.seed(42)

# ----------------------------------------------------
# Project Configuration
# ----------------------------------------------------

NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 250
NUM_ORDERS = 5000
NUM_ORDER_ITEMS = 15000

# ----------------------------------------------------
# Project Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "Data" / "raw"
CLEANED_DATA_PATH = BASE_DIR / "Data" / "cleaned"
REPORT_PATH = BASE_DIR / "Data" / "reports"

RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)
REPORT_PATH.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------
# Product Categories
# ----------------------------------------------------

categories = {
    "Electronics": [
        "Mobile",
        "Laptop",
        "Accessories"
    ],

    "Clothing": [
        "Men",
        "Women",
        "Kids"
    ],

    "Home": [
        "Furniture",
        "Kitchen",
        "Decor"
    ],

    "Books": [
        "Fiction",
        "Academic",
        "Self Help"
    ],

    "Sports": [
        "Fitness",
        "Outdoor",
        "Indoor"
    ],

    "Beauty": [
        "Skincare",
        "Haircare",
        "Makeup"
    ]
}

brands = [
    "Samsung",
    "Apple",
    "Dell",
    "HP",
    "Nike",
    "Adidas",
    "Puma",
    "Boat",
    "Prestige",
    "Philips",
    "Lakme",
    "Mamaearth",
    "Sony",
    "Lenovo",
    "LG"
]

order_status = [
    "PLACED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED",
    "RETURNED"
]

regions = [
    "NORTH",
    "SOUTH",
    "EAST",
    "WEST",
    "CENTRAL"
]

# ----------------------------------------------------
# Customer Dataset
# ----------------------------------------------------

def generate_customers(num_customers):

    customers = []

    customer_types = [
        "REGULAR",
        "PREMIUM",
        "VIP"
    ]

    for i in range(1, num_customers + 1):

        customer = {

            "customer_id": f"CUST{i:05d}",

            "customer_name": fake.name(),

            "email": fake.email(),

            "registration_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            ),

            "customer_type": random.choice(customer_types)

        }

        customers.append(customer)

    return pd.DataFrame(customers)

# ----------------------------------------------------
# Product Dataset
# ----------------------------------------------------

def generate_products(num_products):

    products = []

    for i in range(1, num_products + 1):

        category = random.choice(list(categories.keys()))

        subcategory = random.choice(
            categories[category]
        )

        brand = random.choice(brands)

        product = {

            "product_id": f"PROD{i:05d}",

            "product_name": f"{brand} {subcategory}",

            "category": category,

            "subcategory": subcategory,

            "cost_price": random.randint(
                200,
                50000
            )

        }

        products.append(product)

    return pd.DataFrame(products)


# Generate orders dataset

def generate_orders(num_orders, customer_ids):

    orders = []

    for i in range(1, num_orders + 1):

        order = {

            "order_id": f"ORD{i:06d}",

            "customer_id": random.choice(customer_ids),

            "order_date": fake.date_time_between(
                start_date="-3y",
                end_date="now"
            ),

            "status": random.choice(order_status),

            "region_code": random.choice(regions)

        }

        orders.append(order)

    return pd.DataFrame(orders)


# Generate order items dataset

def generate_order_items(num_order_items, order_ids, product_ids):

    order_items = []

    for i in range(1, num_order_items + 1):

        quantity = random.randint(1, 5)

        unit_price = random.randint(300, 60000)

        discount = random.choice(
            [0, 5, 10, 15, 20, 25, 30]
        )

        item = {

            "item_id": f"ITEM{i:06d}",

            "order_id": random.choice(order_ids),

            "product_id": random.choice(product_ids),

            "quantity": quantity,

            "unit_price": unit_price,

            "discount_percent": discount

        }

        order_items.append(item)

    return pd.DataFrame(order_items)


# Save all raw datasets

def save_raw_datasets(
    customers_df,
    products_df,
    orders_df,
    order_items_df
):

    customers_df.to_csv(
        RAW_DATA_PATH / "customers.csv",
        index=False
    )

    products_df.to_csv(
        RAW_DATA_PATH / "products.csv",
        index=False
    )

    orders_df.to_csv(
        RAW_DATA_PATH / "orders.csv",
        index=False
    )

    order_items_df.to_csv(
        RAW_DATA_PATH / "order_items.csv",
        index=False
    )

    print("Raw datasets saved successfully.")


    # Create dirty datasets

def create_dirty_datasets(
    customers_df,
    products_df,
    orders_df,
    order_items_df
):

    customers_dirty = customers_df.copy()
    products_dirty = products_df.copy()
    orders_dirty = orders_df.copy()
    order_items_dirty = order_items_df.copy()

    # Invalid emails

    num_invalid_emails = int(len(customers_dirty) * 0.02)

    random_rows = random.sample(
        range(len(customers_dirty)),
        num_invalid_emails
    )

    for row in random_rows:
        customers_dirty.loc[row, "email"] = "invalid_email.com"

    # Duplicate customer records

    duplicate_customers = customers_dirty.sample(
        frac=0.01,
        random_state=42
    )

    customers_dirty = pd.concat(
        [customers_dirty, duplicate_customers],
        ignore_index=True
    )

    # Product names with extra spaces and upper case

    num_products = int(len(products_dirty) * 0.05)

    rows = random.sample(
        range(len(products_dirty)),
        num_products
    )

    for row in rows:

        products_dirty.loc[row, "product_name"] = (
            "  "
            + products_dirty.loc[row, "product_name"].upper()
            + "   "
        )

    # Missing customer ids

    num_null_customer = int(len(orders_dirty) * 0.05)

    rows = random.sample(
        range(len(orders_dirty)),
        num_null_customer
    )

    orders_dirty.loc[
        rows,
        "customer_id"
    ] = None

    # Wrong date format

    num_wrong_dates = int(len(orders_dirty) * 0.03)

    rows = random.sample(
        range(len(orders_dirty)),
        num_wrong_dates
    )

    for row in rows:

        current_date = pd.to_datetime(
            orders_dirty.loc[row, "order_date"]
        )

        orders_dirty.loc[row, "order_date"] = (
            current_date.strftime("%d-%m-%Y")
        )

    # Negative quantity (returns)

    num_negative = int(len(order_items_dirty) * 0.03)

    rows = random.sample(
        range(len(order_items_dirty)),
        num_negative
    )

    order_items_dirty.loc[
        rows,
        "quantity"
    ] *= -1

    return (
        customers_dirty,
        products_dirty,
        orders_dirty,
        order_items_dirty
    )


# Save dirty datasets

def save_dirty_datasets(
    customers_dirty,
    products_dirty,
    orders_dirty,
    order_items_dirty
):

    customers_dirty.to_csv(
        RAW_DATA_PATH / "customers_dirty.csv",
        index=False
    )

    products_dirty.to_csv(
        RAW_DATA_PATH / "products_dirty.csv",
        index=False
    )

    orders_dirty.to_csv(
        RAW_DATA_PATH / "orders_dirty.csv",
        index=False
    )

    order_items_dirty.to_csv(
        RAW_DATA_PATH / "order_items_dirty.csv",
        index=False
    )

    print("Dirty datasets saved successfully.")


def main():

    print("Generating datasets...")

    customers_df = generate_customers(
        NUM_CUSTOMERS
    )

    products_df = generate_products(
        NUM_PRODUCTS
    )

    orders_df = generate_orders(
        NUM_ORDERS,
        customers_df["customer_id"].tolist()
    )

    order_items_df = generate_order_items(
        NUM_ORDER_ITEMS,
        orders_df["order_id"].tolist(),
        products_df["product_id"].tolist()
    )

    save_raw_datasets(
        customers_df,
        products_df,
        orders_df,
        order_items_df
    )

    (
        customers_dirty,
        products_dirty,
        orders_dirty,
        order_items_dirty

    ) = create_dirty_datasets(

        customers_df,
        products_df,
        orders_df,
        order_items_df

    )

    save_dirty_datasets(
        customers_dirty,
        products_dirty,
        orders_dirty,
        order_items_dirty
    )

    print("Data generation completed successfully.")


if __name__ == "__main__":

    main()
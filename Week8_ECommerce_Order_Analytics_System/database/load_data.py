import os
from pathlib import Path
import pandas as pd

from dotenv import load_dotenv

from sqlalchemy import create_engine

# For loading Load environment variables

#project rooot
BASE_DIR = Path(__file__).resolve().parent.parent

# load .env file with the BASE resolved adderss
load_dotenv(BASE_DIR / ".env")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_HOST = os.getenv("DB_HOST")

DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Temporarily To be ADDED
print(DB_USER)
print(DB_HOST)
print(DB_PORT)
print(DB_NAME)

# Remove above when this file works


engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

try:
    with engine.connect() as connection:
        print("Database connected successfully!")

except Exception as e:
    print("Connection Failed!")
    print(e)

# For Testing the connection although not necessary, remove when once connection success


BASE_DIR = Path(__file__).resolve().parent.parent
CLEANED_DATA_PATH = BASE_DIR / "Data" / "cleaned"

customers = pd.read_csv(CLEANED_DATA_PATH / "customers_cleaned.csv")
products = pd.read_csv(CLEANED_DATA_PATH / "products_cleaned.csv")

orders = pd.read_csv(CLEANED_DATA_PATH / "orders_cleaned.csv")

order_items = pd.read_csv(CLEANED_DATA_PATH / "order_items_cleaned.csv")

print("Dataset loaded successfully.")

try: 
    customers.to_sql(
        "customers",
        engine,
        if_exists="append",
        index=False
    )
    products.to_sql(
        "products",
        engine,
        if_exists="append",
        index=False
    )
    orders.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False
    )

    order_items.to_sql(
        "order_items",
        engine,
        if_exists="append",
        index=False
    )
    print("Order Items imported successfully!")
    # print("All datasets imported successfully.")

except Exception as e:
    print("Some error has ocurred while loading..")
    print(e)

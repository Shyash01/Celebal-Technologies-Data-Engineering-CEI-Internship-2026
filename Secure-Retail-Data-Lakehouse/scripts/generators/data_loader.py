import os
import pandas as pd

from config import (
    MASTER_DATA_PATH,
    RAW_DATA_PATH,
    CUSTOMER_FILE,
    PRODUCT_FILE
)


def load_customers():
    path = os.path.join(RAW_DATA_PATH, CUSTOMER_FILE)
    return pd.read_csv(path)


def load_products():
    path = os.path.join(MASTER_DATA_PATH, PRODUCT_FILE)
    return pd.read_csv(path)


def print_dataset_info(dataset_name, dataframe):
    print(f"\n{dataset_name} loaded successfully.")
    print(f"Total Records : {len(dataframe)}")
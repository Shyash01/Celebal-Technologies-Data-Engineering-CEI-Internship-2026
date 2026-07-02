import os

from dotenv import load_dotenv
from faker import Faker

# Load environment variables from .env
load_dotenv()

# Faker instance
fake = Faker("en_IN")

# Dataset size
NUMBER_OF_CUSTOMERS = 750
NUMBER_OF_TRANSACTIONS = 8000

# Loyalty tiers
LOYALTY_TIERS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]

LOYALTY_WEIGHTS = [
    45,
    30,
    18,
    7
]

# Gender values
GENDERS = [
    "Male",
    "Female",
    "Other"
]

# Indian cities and states
LOCATIONS = {
    "Delhi": "Delhi",
    "Mumbai": "Maharashtra",
    "Bengaluru": "Karnataka",
    "Hyderabad": "Telangana",
    "Chennai": "Tamil Nadu",
    "Kolkata": "West Bengal",
    "Pune": "Maharashtra",
    "Ahmedabad": "Gujarat",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh"
}

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Cash",
    "Net Banking"
]

PAYMENT_METHOD_WEIGHTS = [
    25,
    20,
    40,
    10,
    5
]

ORDER_STATUS = [
    "Completed",
    "Returned",
    "Cancelled"
]

ORDER_STATUS_WEIGHTS = [
    90,
    7,
    3
]

STORES = [
    {"store_id": "STR001", "store_city": "Delhi"},
    {"store_id": "STR002", "store_city": "Mumbai"},
    {"store_id": "STR003", "store_city": "Bengaluru"},
    {"store_id": "STR004", "store_city": "Hyderabad"},
    {"store_id": "STR005", "store_city": "Chennai"},
    {"store_id": "STR006", "store_city": "Kolkata"},
    {"store_id": "STR007", "store_city": "Pune"},
    {"store_id": "STR008", "store_city": "Ahmedabad"},
    {"store_id": "STR009", "store_city": "Jaipur"},
    {"store_id": "STR010", "store_city": "Lucknow"},
]

HARD_DROP_COLUMNS = {
    "customers": [],
    "transactions": ["cvv"]
}

# Folder paths
RAW_DATA_PATH = "data/raw"
MASTER_DATA_PATH = "master_data"
BRONZE_DATA_PATH = "data/bronze"
SILVER_DATA_PATH = "data/silver"
GOLD_DATA_PATH = "data/gold"
REPORTS_PATH = "reports"

# File names
CUSTOMER_FILE = "customers.csv"
PRODUCT_FILE = "product_master.csv"
PAYMENT_METHOD_FILE = "payment_methods.csv"
ORDER_STATUS_FILE = "order_status.csv"
TRANSACTION_FILE = "transactions.csv"

# PostgreSQL Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5433")
DB_NAME = os.getenv("DB_NAME", "secure_retail_lakehouse")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
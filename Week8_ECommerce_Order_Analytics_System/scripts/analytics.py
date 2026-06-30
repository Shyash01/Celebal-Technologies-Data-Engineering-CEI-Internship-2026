import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Load environment variables

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(
    BASE_DIR / ".env"
)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# Create database connection

def get_connection():

    return engine


# Total Orders

def get_total_orders(start_date, end_date):

    query = f"""

    SELECT COUNT(*) AS total_orders

    FROM orders

    WHERE order_date
    BETWEEN '{start_date}'
    AND '{end_date}'

    """

    result = pd.read_sql(
        query,
        engine
    )

    return result


# Total Revenue

def get_total_revenue(start_date, end_date):

    query = f"""

    SELECT

    SUM(

        oi.quantity
        * oi.unit_price
        * (1 - oi.discount_percent / 100.0)

    ) AS total_revenue

    FROM orders o

    JOIN order_items oi

    ON o.order_id = oi.order_id

    WHERE o.order_date
    BETWEEN '{start_date}'
    AND '{end_date}'

    """

    result = pd.read_sql(
        query,
        engine
    )

    return result


# Unique Customers

def get_unique_customers(start_date, end_date):

    query = f"""

    SELECT COUNT(
        DISTINCT customer_id
    ) AS unique_customers

    FROM orders

    WHERE order_date
    BETWEEN '{start_date}'
    AND '{end_date}'

    """

    result = pd.read_sql(
        query,
        engine
    )

    return result

# Top 3 products by revenue

def get_top_products(start_date, end_date):

    query = f"""

    SELECT

        p.product_name,

        SUM(

            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)

        ) AS total_revenue

    FROM orders o

    JOIN order_items oi
        ON o.order_id = oi.order_id

    JOIN products p
        ON oi.product_id = p.product_id

    WHERE o.order_date
    BETWEEN '{start_date}'
    AND '{end_date}'

    GROUP BY
        p.product_name

    ORDER BY
        total_revenue DESC

    LIMIT 3

    """

    result = pd.read_sql(
        query,
        engine
    )

    return result


# Compare current period with previous period

def compare_previous_period(
    current_start,
    current_end,
    previous_start,
    previous_end
):

    current_query = f"""

    SELECT

        SUM(

            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)

        ) AS revenue

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    WHERE o.order_date
    BETWEEN '{current_start}'
    AND '{current_end}'

    """

    previous_query = f"""

    SELECT

        SUM(

            oi.quantity
            * oi.unit_price
            * (1 - oi.discount_percent / 100.0)

        ) AS revenue

    FROM orders o

    JOIN order_items oi

        ON o.order_id = oi.order_id

    WHERE o.order_date
    BETWEEN '{previous_start}'
    AND '{previous_end}'

    """

    current_revenue = pd.read_sql(
        current_query,
        engine
    )

    previous_revenue = pd.read_sql(
        previous_query,
        engine
    )

    current_value = current_revenue.iloc[0, 0]
    previous_value = previous_revenue.iloc[0, 0]

    if pd.isna(current_value):
        current_value = 0

    if pd.isna(previous_value):
        previous_value = 0

    if previous_value == 0:

        percent_change = None

    else:

        percent_change = (
            (current_value - previous_value)
            / previous_value
        ) * 100

    comparison = pd.DataFrame({

        "current_revenue": [current_value],

        "previous_revenue": [previous_value],

        "percent_change": [percent_change]

    })

    return comparison
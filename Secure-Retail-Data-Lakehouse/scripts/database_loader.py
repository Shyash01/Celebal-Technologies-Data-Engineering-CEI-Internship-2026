import os

import pandas as pd
from sqlalchemy import create_engine, text

from generators.config import (
    GOLD_DATA_PATH,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def create_connection():

    connection_string = (
        f"postgresql+psycopg2://"
        f"{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/"
        f"{DB_NAME}"
    )

    return create_engine(connection_string)


def load_csv_files():

    customers = pd.read_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "customers_gold.csv"
        )
    )

    transactions = pd.read_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "transactions_gold.csv"
        )
    )

    customer_summary = pd.read_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "customer_summary.csv"
        )
    )

    sales_summary = pd.read_csv(
        os.path.join(
            GOLD_DATA_PATH,
            "sales_summary.csv"
        )
    )

    return (
        customers,
        transactions,
        customer_summary,
        sales_summary
    )


def load_to_database(engine):

    (
        customers,
        transactions,
        customer_summary,
        sales_summary
    ) = load_csv_files()

    print("\nLoading tables...\n")

    customers.to_sql(
        "customers_gold",
        engine,
        if_exists="replace",
        index=False
    )

    transactions.to_sql(
        "transactions_gold",
        engine,
        if_exists="replace",
        index=False
    )

    customer_summary.to_sql(
        "customer_summary",
        engine,
        if_exists="replace",
        index=False
    )

    sales_summary.to_sql(
        "sales_summary",
        engine,
        if_exists="replace",
        index=False
    )

    print("All tables loaded successfully.")


def verify_tables(engine):

    print("\nVerifying tables...\n")

    tables = [
        "customers_gold",
        "transactions_gold",
        "customer_summary",
        "sales_summary"
    ]

    with engine.connect() as connection:

        for table in tables:

            count = connection.execute(
                text(f"SELECT COUNT(*) FROM {table}")
            ).scalar()

            print(f"{table:<22} {count}")


def main():

    print("=" * 50)
    print("POSTGRESQL DATA LOADER")
    print("=" * 50)

    engine = create_connection()

    load_to_database(engine)

    verify_tables(engine)

    print("\nDatabase Loading Completed Successfully.")


if __name__ == "__main__":
    main()
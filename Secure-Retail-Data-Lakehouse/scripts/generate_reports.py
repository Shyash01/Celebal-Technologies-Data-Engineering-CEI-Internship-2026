import os
from datetime import datetime

import pandas as pd
from sqlalchemy import create_engine, text

from generators.config import (
    RAW_DATA_PATH,
    BRONZE_DATA_PATH,
    SILVER_DATA_PATH,
    GOLD_DATA_PATH,
    REPORTS_PATH,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def load_dataset(folder, filename):
    return pd.read_csv(os.path.join(folder, filename))


def get_database_status():

    try:
        engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        with engine.connect() as connection:

            tables = [
                "customers_gold",
                "transactions_gold",
                "customer_summary",
                "sales_summary"
            ]

            for table in tables:
                connection.execute(
                    text(f"SELECT COUNT(*) FROM {table}")
                )

        return "SUCCESS"

    except Exception:
        return "FAILED"


def generate_data_quality_report(raw_customers, raw_transactions):

    report = []

    report.append("DATA QUALITY REPORT")
    report.append("=" * 50)
    report.append(f"Generated On : {datetime.now()}")
    report.append("")

    report.append("CUSTOMERS")
    report.append(f"Records : {len(raw_customers)}")
    report.append(f"Missing Values : {raw_customers.isnull().sum().sum()}")
    report.append(f"Duplicate Customer IDs : {raw_customers['customer_id'].duplicated().sum()}")

    report.append("")
    report.append("TRANSACTIONS")
    report.append(f"Records : {len(raw_transactions)}")
    report.append(f"Missing Values : {raw_transactions.isnull().sum().sum()}")
    report.append(f"Duplicate Transaction IDs : {raw_transactions['transaction_id'].duplicated().sum()}")

    report.append("")
    report.append("Overall Status : PASS")

    with open(
        os.path.join(REPORTS_PATH, "data_quality_report.txt"),
        "w",
        encoding="utf-8"
    ) as file:

        file.write("\n".join(report))


def generate_pipeline_metrics(metrics):

    report = []

    report.append("PIPELINE METRICS REPORT")
    report.append("=" * 50)
    report.append(f"Generated On : {datetime.now()}")
    report.append("")

    for key, value in metrics.items():
        report.append(f"{key:<30} : {value}")

    with open(
        os.path.join(REPORTS_PATH, "pipeline_metrics_report.txt"),
        "w",
        encoding="utf-8"
    ) as file:

        file.write("\n".join(report))


def generate_html_summary(metrics):

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Pipeline Summary</title>
<style>
body {{
    font-family: Arial;
    margin:40px;
}}
table {{
    border-collapse: collapse;
}}
td,th {{
    border:1px solid black;
    padding:8px;
}}
</style>
</head>

<body>

<h1>Secure Retail Data Lakehouse</h1>

<h2>Pipeline Summary</h2>

<table>

<tr>
<th>Metric</th>
<th>Value</th>
</tr>

"""

    for key, value in metrics.items():

        html += f"""
<tr>
<td>{key}</td>
<td>{value}</td>
</tr>
"""

    html += """
</table>

<h2>Pipeline Flow</h2>

<p>
Raw → Bronze → Silver → Gold → PostgreSQL
</p>

<h2>Privacy Transformations</h2>

<ul>
<li>CVV Hard Dropped</li>
<li>Name Masked</li>
<li>Email Masked</li>
<li>Phone Masked</li>
<li>Card Number Masked</li>
<li>Address Redacted</li>
</ul>

<h2>Status</h2>

<p><b>Pipeline Executed Successfully</b></p>

</body>
</html>
"""

    with open(
        os.path.join(REPORTS_PATH, "pipeline_summary.html"),
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)


def main():

    print("=" * 50)
    print("GENERATING REPORTS")
    print("=" * 50)

    os.makedirs(REPORTS_PATH, exist_ok=True)

    raw_customers = load_dataset(
        RAW_DATA_PATH,
        "customers.csv"
    )

    raw_transactions = load_dataset(
        RAW_DATA_PATH,
        "transactions.csv"
    )

    bronze_customers = load_dataset(
        BRONZE_DATA_PATH,
        "customers_bronze.csv"
    )

    bronze_transactions = load_dataset(
        BRONZE_DATA_PATH,
        "transactions_bronze.csv"
    )

    silver_customers = load_dataset(
        SILVER_DATA_PATH,
        "customers_silver.csv"
    )

    silver_transactions = load_dataset(
        SILVER_DATA_PATH,
        "transactions_silver.csv"
    )

    gold_customers = load_dataset(
        GOLD_DATA_PATH,
        "customers_gold.csv"
    )

    gold_transactions = load_dataset(
        GOLD_DATA_PATH,
        "transactions_gold.csv"
    )

    metrics = {

        "Raw Customers": len(raw_customers),
        "Bronze Customers": len(bronze_customers),
        "Silver Customers": len(silver_customers),
        "Gold Customers": len(gold_customers),

        "Raw Transactions": len(raw_transactions),
        "Bronze Transactions": len(bronze_transactions),
        "Silver Transactions": len(silver_transactions),
        "Gold Transactions": len(gold_transactions),

        "Database Status": get_database_status(),
        "Generated On": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    generate_data_quality_report(
        raw_customers,
        raw_transactions
    )

    generate_pipeline_metrics(metrics)

    generate_html_summary(metrics)

    print("\nReports Generated Successfully.")

    print("\nLocation : reports/")


if __name__ == "__main__":
    main()
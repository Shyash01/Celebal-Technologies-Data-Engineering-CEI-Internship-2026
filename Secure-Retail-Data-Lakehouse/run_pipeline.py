import subprocess
import sys


PIPELINE_STEPS = [

    (
        "Generating Product Master",
        "scripts/generators/generate_product_master.py"
    ),

    (
        "Generating Customers",
        "scripts/generators/generate_customers.py"
    ),

    (
        "Generating Transactions",
        "scripts/generators/generate_transactions.py"
    ),

    (
        "Validating Generated Data",
        "scripts/generators/validate_generated_data.py"
    ),

    (
        "Executing Bronze Layer",
        "scripts/bronze_layer.py"
    ),

    (
        "Executing Silver Layer",
        "scripts/silver_layer.py"
    ),

    (
        "Executing Gold Layer",
        "scripts/gold_layer.py"
    ),

    (
        "Loading PostgreSQL",
        "scripts/database_loader.py"
    ),

    (
        "Generating Reports",
        "scripts/generate_reports.py"
    )

]


def run_step(title, script):

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, script]
    )

    if result.returncode != 0:

        print(f"\nPipeline stopped while executing:\n{script}")

        sys.exit(1)

    print(f"\n{title} Completed Successfully")


def main():

    print("=" * 70)
    print("SECURE RETAIL DATA LAKEHOUSE")
    print("END-TO-END ETL PIPELINE")
    print("=" * 70)

    for title, script in PIPELINE_STEPS:

        run_step(title, script)

    print("\n" + "=" * 70)
    print("PIPELINE EXECUTED SUCCESSFULLY")
    print("=" * 70)

    print("\nGenerated Outputs")

    print("✓ Raw Layer")
    print("✓ Bronze Layer")
    print("✓ Silver Layer")
    print("✓ Gold Layer")
    print("✓ PostgreSQL Tables")
    print("✓ Reports")


if __name__ == "__main__":
    main()
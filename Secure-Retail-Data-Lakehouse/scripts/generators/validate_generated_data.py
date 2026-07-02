import os
import pandas as pd

from config import (
    RAW_DATA_PATH,
    TRANSACTION_FILE,
    CUSTOMER_FILE,
    LOYALTY_TIERS,
    GENDERS
)


def validate():

    print("\nLoading datasets...\n")

    customers = pd.read_csv(
        os.path.join(RAW_DATA_PATH, CUSTOMER_FILE)
    )

    transactions = pd.read_csv(
        os.path.join(RAW_DATA_PATH, TRANSACTION_FILE)
    )

    validation_results = []

    # ------------------------
    # Customer Validations
    # ------------------------

    validation_results.append((
        "Customer Count",
        len(customers) == 750
    ))

    validation_results.append((
        "Unique Customer IDs",
        customers["customer_id"].is_unique
    ))

    validation_results.append((
        "Missing Customer IDs",
        customers["customer_id"].isnull().sum() == 0
    ))

    validation_results.append((
        "Valid Loyalty Tiers",
        customers["loyalty_tier"].isin(LOYALTY_TIERS).all()
    ))

    validation_results.append((
        "Valid Genders",
        customers["gender"].isin(GENDERS).all()
    ))

    # ------------------------
    # Transaction Validations
    # ------------------------

    validation_results.append((
        "Transaction Count",
        len(transactions) == 8000
    ))

    validation_results.append((
        "Unique Transaction IDs",
        transactions["transaction_id"].is_unique
    ))

    validation_results.append((
        "Valid Customer References",
        transactions["customer_id"].isin(
            customers["customer_id"]
        ).all()
    ))

    validation_results.append((
        "Quantity > 0",
        (transactions["quantity"] > 0).all()
    ))

    validation_results.append((
        "Unit Price > 0",
        (transactions["unit_price"] > 0).all()
    ))

    validation_results.append((
        "Correct Total Amount",
        (
            transactions["quantity"] *
            transactions["unit_price"]
            ==
            transactions["total_amount"]
        ).all()
    ))

    card_payments = transactions[
        transactions["payment_method"].isin(
            ["Credit Card", "Debit Card"]
        )
    ]

    validation_results.append((
        "Card Numbers Present",
        card_payments["card_number"].notna().all()
    ))

    validation_results.append((
        "CVV Present",
        card_payments["cvv"].notna().all()
    ))

    print("\nValidation Results\n")

    passed = True

    report_lines = []

    report_lines.append("DATA VALIDATION REPORT")
    report_lines.append("=" * 40)

    for check, result in validation_results:

        status = "PASS" if result else "FAIL"

        if not result:
            passed = False

        print(f"{check:<35} {status}")

        report_lines.append(
            f"{check:<35} {status}"
        )

    report_lines.append("=" * 40)

    report_lines.append(
        f"Overall Status : {'PASS' if passed else 'FAIL'}"
    )

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/validation_report.txt",
        "w"
    ) as file:

        file.write("\n".join(report_lines))

    print("\nValidation report generated.")
    print("Location : reports/validation_report.txt")


if __name__ == "__main__":
    validate()
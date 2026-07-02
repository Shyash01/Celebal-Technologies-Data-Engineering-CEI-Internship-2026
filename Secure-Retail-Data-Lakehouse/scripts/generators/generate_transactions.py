import os
import random

import pandas as pd

from config import (
    fake,
    PAYMENT_METHODS,
    PAYMENT_METHOD_WEIGHTS,
    ORDER_STATUS,
    ORDER_STATUS_WEIGHTS,
    STORES,
    RAW_DATA_PATH,
    TRANSACTION_FILE
)

from data_loader import (
    load_customers,
    load_products,
    print_dataset_info
)

from transaction_allocator import allocate_transactions


def generate_transactions():

    print("\nLoading datasets...\n")

    customers_df = load_customers()
    products_df = load_products()

    print_dataset_info("Customers", customers_df)
    print_dataset_info("Products", products_df)

    allocation = allocate_transactions()

    print("\nTransaction allocation loaded.")
    print(f"Customers in allocation : {len(allocation)}")
    print(f"Total transactions : {sum(allocation.values())}")

    transactions = []
    transaction_counter = 1

    for customer_id, transaction_count in allocation.items():

        customer = customers_df[
            customers_df["customer_id"] == customer_id
        ].iloc[0]

        for _ in range(transaction_count):

            product = products_df.sample(1).iloc[0]

            quantity = random.randint(1, 5)

            unit_price = random.randint(
                int(product["min_price"]),
                int(product["max_price"])
            )

            total_amount = quantity * unit_price

            payment_method = random.choices(
                PAYMENT_METHODS,
                weights=PAYMENT_METHOD_WEIGHTS,
                k=1
            )[0]

            order_status = random.choices(
                ORDER_STATUS,
                weights=ORDER_STATUS_WEIGHTS,
                k=1
            )[0]

            store = random.choice(STORES)

            transaction_timestamp = fake.date_time_between(
                start_date="-2y",
                end_date="now"
            )

            card_number = ""
            cvv = ""

            if payment_method in ["Credit Card", "Debit Card"]:
                card_number = fake.credit_card_number()
                cvv = fake.credit_card_security_code()

            transaction = {
                "transaction_id": f"TXN{transaction_counter:06}",
                "customer_id": customer_id,
                "transaction_timestamp": transaction_timestamp,
                "product_id": product["product_id"],
                "product_name": product["product_name"],
                "category": product["category"],
                "quantity": quantity,
                "unit_price": unit_price,
                "total_amount": total_amount,
                "payment_method": payment_method,
                "card_number": card_number,
                "cvv": cvv,
                "store_id": store["store_id"],
                "store_city": store["store_city"],
                "order_status": order_status
            }

            transactions.append(transaction)
            transaction_counter += 1

    transaction_df = pd.DataFrame(transactions)

    print("\nTransaction generation completed.")
    print(f"Total Transactions : {len(transaction_df)}")

    print("\nFirst Five Records:\n")
    print(transaction_df.head())

    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    output_path = os.path.join(
        RAW_DATA_PATH,
        TRANSACTION_FILE
    )

    transaction_df.to_csv(
        output_path,
        index=False
    )

    print(f"\nTransactions saved successfully.")
    print(f"Location : {output_path}")


if __name__ == "__main__":
    generate_transactions()
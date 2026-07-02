import random

from config import (
    NUMBER_OF_CUSTOMERS,
    NUMBER_OF_TRANSACTIONS
)


def allocate_transactions():

    customer_ids = [
        f"CUST{i:04}"
        for i in range(1, NUMBER_OF_CUSTOMERS + 1)
    ]

    random.shuffle(customer_ids)

    frequent_count = int(NUMBER_OF_CUSTOMERS * 0.15)
    regular_count = int(NUMBER_OF_CUSTOMERS * 0.60)

    frequent_customers = customer_ids[:frequent_count]
    regular_customers = customer_ids[
        frequent_count:frequent_count + regular_count
    ]
    occasional_customers = customer_ids[
        frequent_count + regular_count:
    ]

    allocation = {}

    total_transactions = 0

    # Frequent buyers
    for customer in frequent_customers:
        transactions = random.randint(20, 40)
        allocation[customer] = transactions
        total_transactions += transactions

    # Regular buyers
    for customer in regular_customers:
        transactions = random.randint(8, 15)
        allocation[customer] = transactions
        total_transactions += transactions

    # Occasional buyers
    for customer in occasional_customers:
        transactions = random.randint(1, 7)
        allocation[customer] = transactions
        total_transactions += transactions

    difference = NUMBER_OF_TRANSACTIONS - total_transactions

    while difference != 0:

        customer = random.choice(customer_ids)

        if difference > 0:
            allocation[customer] += 1
            difference -= 1

        else:
            if allocation[customer] > 1:
                allocation[customer] -= 1
                difference += 1

    allocation = dict(sorted(allocation.items()))

    return allocation

if __name__ == "__main__":

    allocation = allocate_transactions()

    print("Transaction Allocation Completed")

    print(f"Customers : {len(allocation)}")

    print(f"Transactions : {sum(allocation.values())}")

    print("\nSample Allocation:\n")

    for customer, count in list(allocation.items())[:10]:
        print(customer, "->", count)
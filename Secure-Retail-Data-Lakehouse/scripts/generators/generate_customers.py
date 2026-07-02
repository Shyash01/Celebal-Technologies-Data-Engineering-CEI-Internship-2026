import os
import random
from datetime import date

import pandas as pd

from config import (
    fake,
    NUMBER_OF_CUSTOMERS,
    LOYALTY_TIERS,
    LOYALTY_WEIGHTS,
    GENDERS,
    LOCATIONS
)

customers = []

cities = list(LOCATIONS.keys())

for i in range(1, NUMBER_OF_CUSTOMERS + 1):

    city = random.choice(cities)
    state = LOCATIONS[city]

    dob = fake.date_of_birth(
        minimum_age=18,
        maximum_age=80
    )

    registration_date = fake.date_between(
        start_date="-5y",
        end_date="today"
    )

    customer = {
        "customer_id": f"CUST{i:04}",
        "full_name": fake.name(),
        "email": fake.email(),
        "phone": fake.msisdn()[-10:],
        "address": fake.street_address().replace("\n", ", ").replace("\r", ""),
        "city": city,
        "state": state,
        "postal_code": fake.postcode(),
        "date_of_birth": dob,
        "gender": random.choice(GENDERS),
        "registration_date": registration_date,
        "loyalty_tier": random.choices(
            LOYALTY_TIERS,
            weights=LOYALTY_WEIGHTS,
            k=1
        )[0]
    }

    customers.append(customer)

customer_df = pd.DataFrame(customers)

os.makedirs("data/raw", exist_ok=True)

output_file = os.path.join(
    "data",
    "raw",
    "customers.csv"
)

customer_df.to_csv(
    output_file,
    index=False
)

print("Customer dataset generated successfully.")
print(f"Location : {output_file}")
print(f"Total Customers : {len(customer_df)}")
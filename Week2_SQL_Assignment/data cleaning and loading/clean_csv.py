import pandas as pd
import csv

df = pd.read_csv(
    "data/SampleSuperstore.csv",
    encoding="utf-8",
    engine="python",
    on_bad_lines="skip"
)

# Save cleaned dataset
df.to_csv(
    "data/final_cleaned_superstore.csv",
    index=False,
    quoting=csv.QUOTE_ALL
)

print("Corrupted rows removed successfully.")
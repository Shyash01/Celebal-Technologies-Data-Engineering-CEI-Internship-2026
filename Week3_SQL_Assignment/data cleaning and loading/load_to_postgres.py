import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV file
df = pd.read_csv("../data/final_cleaned_superstore.csv")

# PostgreSQL connection
username = "postgres"
password = "Yash%40123"
host = "localhost"
port = "5433"
database = "week3_sql_assignment"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Load data into PostgreSQL
df.to_sql(
    "superstore_raw",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into superstore_raw table.")
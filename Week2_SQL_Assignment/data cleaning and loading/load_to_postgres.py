import pandas as pd
from sqlalchemy import create_engine

# Load dataset safely
df = pd.read_csv(
    "data/SampleSuperstore.csv",
    engine="python",
    on_bad_lines="skip"
)

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:Yash%40123@localhost:5433/superstore_db"
)

# Upload dataframe to PostgreSQL
df.to_sql(
    "superstore",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into PostgreSQL.")
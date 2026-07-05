import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres123@localhost:5432/retail_inventory_raw"
)

query = "SELECT * FROM retail_inventory_clean"

df = pd.read_sql(query, engine)

print(df.head())
print(df.shape)
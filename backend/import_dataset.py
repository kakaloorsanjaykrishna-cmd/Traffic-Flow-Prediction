import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from config import *

encoded_password = quote_plus(DB_PASSWORD)

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

df = pd.read_csv("dataset/traffic_data.csv")

df.to_sql(
    name="traffic_data",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=5000,
    method="multi"
)

print("✅ Dataset Imported Successfully!")
print(f"Total Records Imported: {len(df)}")
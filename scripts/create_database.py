import pandas as pd
import sqlite3
import os

conn = sqlite3.connect(
    "database/bluestock_mf.db"
)

processed_folder = "data/processed"

for file in os.listdir(processed_folder):

    if file.endswith(".csv"):

        table_name = file.replace(".csv", "")

        df = pd.read_csv(
            os.path.join(processed_folder, file)
        )

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"Loaded: {table_name}")

conn.close()

print("Database created successfully.")
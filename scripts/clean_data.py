import pandas as pd
import os

raw_folder = "data/raw"
processed_folder = "data/processed"

os.makedirs(processed_folder, exist_ok=True)

for file in os.listdir(raw_folder):
    if file.endswith(".csv"):

        filepath = os.path.join(raw_folder, file)

        df = pd.read_csv(filepath)

        # Convert date
        df["date"] = pd.to_datetime(
            df["date"],
            dayfirst=True,
            errors="coerce"
        )

        # Remove duplicates
        df = df.drop_duplicates()

        # Remove invalid NAV values
        df = df[df["nav"] > 0]

        # Sort by date
        df = df.sort_values("date")

        output = os.path.join(
            processed_folder,
            file
        )

        df.to_csv(output, index=False)

        print(f"Cleaned: {file}")

print("All files cleaned successfully.")
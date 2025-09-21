# explore.py - Part 1: Data Loading & Basic Exploration
import os
import pandas as pd

# change this if your sample file has a different name
FILE = "metadata_sample.csv"

def main():
    # 1) check file exists
    if not os.path.exists(FILE):
        print(f"ERROR: File '{FILE}' not found in this folder.")
        print("Put metadata_sample.csv in the same folder and re-run.")
        return

    # 2) load CSV
    df = pd.read_csv(FILE)

    # 3) quick preview
    print("=== First 5 rows ===")
    print(df.head(), "\n")

    # 4) shape (rows, columns)
    print("=== Shape (rows, columns) ===")
    print(df.shape, "\n")

    # 5) columns list
    print("=== Columns ===")
    print(df.columns.tolist(), "\n")

    # 6) info (data types and non-null counts)
    print("=== Info ===")
    df.info()
    print()

    # 7) missing values per column
    print("=== Missing values per column ===")
    print(df.isnull().sum(), "\n")

    # 8) basic descriptive stats (works for text & numeric)
    print("=== Basic statistics (describe) ===")
    print(df.describe(include="all"), "\n")

    # 9) try parsing publish_time to datetime and extract year (helpful for Part 2/3)
    if "publish_time" in df.columns:
        print("=== Parsing publish_time -> datetime and extracting year ===")
        df["publish_time_parsed"] = pd.to_datetime(df["publish_time"], errors="coerce")
        df["year"] = df["publish_time_parsed"].dt.year
        print("Parsed publish_time: number of missing parsed dates =", df["publish_time_parsed"].isnull().sum())
        print("Publications by year (counts):")
        print(df["year"].value_counts().sort_index(), "\n")
    else:
        print("Column 'publish_time' not found; skipping date parsing.\n")

    # 10) save a small sample output for inspection (optional)
    sample_out = "explore_head50.csv"
    df.head(50).to_csv(sample_out, index=False)
    print(f"Saved first 50 rows to '{sample_out}' for easy inspection.\n")

if __name__ == "__main__":
    main()

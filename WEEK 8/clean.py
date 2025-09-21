# clean.py - Part 2: Data Cleaning & Preparation
import pandas as pd

# load the sample
df = pd.read_csv("metadata_sample.csv")

# convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# extract year
df["year"] = df["publish_time"].dt.year

# create a new column: abstract word count
df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))

# save the cleaned version
df.to_csv("metadata_clean.csv", index=False)

print(df.head())
print("\n=== Cleaned Data Info ===")
print(df.info())

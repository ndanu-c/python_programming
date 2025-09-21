# analyze.py - Part 3: Data Analysis & Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# Load cleaned dataset
df = pd.read_csv("metadata_clean.csv")

# === 1. Publications by year ===
year_counts = df["year"].value_counts().sort_index()
plt.figure(figsize=(6,4))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.tight_layout()
plt.savefig("pubs_by_year.png")
plt.close()

# === 2. Top journals ===
top_journals = df["journal"].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, color="lightgreen")
plt.title("Top 10 Journals")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.close()

# === 3. Most frequent words in titles ===
all_words = " ".join(df["title"].astype(str).tolist()).lower().split()
word_freq = Counter(all_words)
common_words = dict(word_freq.most_common(20))

plt.figure(figsize=(8,5))
sns.barplot(y=list(common_words.keys()), x=list(common_words.values()), color="salmon")
plt.title("Most Frequent Words in Paper Titles")
plt.xlabel("Count")
plt.ylabel("Word")
plt.tight_layout()
plt.savefig("title_word_freq.png")
plt.close()

# Word cloud (optional, but nice!)
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(all_words))
wordcloud.to_file("title_wordcloud.png")

# === 4. Paper counts by source ===
source_counts = df["source_x"].value_counts()
plt.figure(figsize=(6,4))
sns.barplot(y=source_counts.index, x=source_counts.values, color="violet")
plt.title("Papers by Source")
plt.xlabel("Number of Papers")
plt.ylabel("Source")
plt.tight_layout()
plt.savefig("papers_by_source.png")
plt.close()

print("Analysis complete. Charts saved as:")
print("- pubs_by_year.png")
print("- top_journals.png")
print("- title_word_freq.png")
print("- title_wordcloud.png")
print("- papers_by_source.png")

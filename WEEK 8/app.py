# app.py - Streamlit App (extended with all charts)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load cleaned data
df = pd.read_csv("metadata_clean.csv")

# Title and description
st.title("CORD-19 Data Explorer")
st.write("Exploring COVID-19 research papers metadata (sample dataset).")

# Show data sample
st.subheader("Sample of the Data")
st.dataframe(df.head(10))

# Year range slider
year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select Year Range:", year_min, year_max, (year_min, year_max))

# Filter dataset
filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]
st.write(f"Number of papers in selected range: {len(filtered)}")

# --- Publications by year ---
st.subheader("Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, color="skyblue")
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Top journals ---
st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(5)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, color="lightgreen")
ax.set_title("Top Journals")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# --- Papers by source ---
st.subheader("Papers by Source")
source_counts = filtered["source_x"].value_counts()
fig, ax = plt.subplots()
sns.barplot(y=source_counts.index, x=source_counts.values, ax=ax, color="violet")
ax.set_title("Papers by Source")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Source")
st.pyplot(fig)

# --- Word cloud of titles ---
st.subheader("Word Cloud of Paper Titles")
all_words = " ".join(filtered["title"].astype(str).tolist())
if all_words.strip():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_words)
    st.image(wordcloud.to_array())
else:
    st.write("No titles available in the selected range.")

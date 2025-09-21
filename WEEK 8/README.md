# Frameworks Assignment - CORD-19 Data Explorer

This project is part of the **Frameworks Assignment**.  
It demonstrates the full data science workflow using a sample from the **CORD-19 metadata dataset**, which contains information about COVID-19 research papers.

---

## Objectives
By completing this assignment, I practiced:
- Loading and exploring a real-world dataset
- Performing basic data cleaning
- Creating visualizations with `matplotlib` and `seaborn`
- Building a simple interactive app with `Streamlit`
- Presenting insights and reflecting on the process

---

## Tools Used
- Python 3.10+  
- [pandas](https://pandas.pydata.org/) (data manipulation)  
- [matplotlib](https://matplotlib.org/) & [seaborn](https://seaborn.pydata.org/) (visualizations)  
- [wordcloud](https://github.com/amueller/word_cloud) (word cloud visualization)  
- [Streamlit](https://streamlit.io/) (interactive app)  

---

## Project Structure
├── metadata_sample.csv # Original sample dataset
├── metadata_clean.csv # Cleaned dataset
├── explore.py # Part 1: Data exploration
├── clean.py # Part 2: Data cleaning
├── analyze.py # Part 3: Data analysis & visualization
├── app.py # Part 4: Streamlit interactive app
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## Steps Completed

### Part 1: Data Loading & Exploration
- Loaded dataset with Pandas  
- Checked shape, datatypes, and missing values  

### Part 2: Data Cleaning & Preparation
- Converted `publish_time` to datetime  
- Extracted `year`  
- Added `abstract_word_count` column  

### Part 3: Analysis & Visualization
- **Publications by year** (bar chart)  
- **Top journals** (bar chart)  
- **Papers by source** (bar chart)  
- **Most frequent words in titles** (bar chart + word cloud)  

### Part 4: Streamlit App
- Interactive dashboard (`app.py`)  
- Year range filter  
- Displays charts and word cloud  

### Part 5: Documentation & Reflection
- Added comments in code  
- Wrote this README  
- Reflected on learning process  

---

## How to Run

1. Clone this repo:
   git clone https://github.com/<your-username>/Frameworks_Assignment.git
   cd Frameworks_Assignment

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the exploration scripts:
python explore.py
python clean.py
python analyze.py

5. Launch the Streamlit app:
streamlit run app.py

Insights
Most papers in the dataset were published in 2020 (peak of pandemic research).

Journals like Nature, The Lancet, and Science appear often.

Common words in paper titles include COVID-19, vaccine, impact, and pandemic.

Reflection
The main challenges were:

Handling the large original CORD-19 dataset (over 20GB).

Deciding to work with a sample dataset for performance and GitHub storage limits.

Learning to use Streamlit for building an interactive dashboard.

I gained valuable experience in:

Cleaning and preparing real-world data

Creating visualizations to uncover insights

Sharing results through a web app and GitHub
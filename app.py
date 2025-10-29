import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load your dataset
#df_covid = pd.read_csv("metadata.csv",usecols=['source_x','title','abstract','publish_time','authors','journal']) #You can use this if you want to read the whole data
# for purpose of avoiding a device from crushing, use this one below
df_covid = pd.read_csv("filtered_df.csv") 
df_covid['publish_time'] = pd.to_datetime(df_covid['publish_time'], errors='coerce')

# Streamlit app layout
st.title("CORD-19 Data Explorer")
st.write("A simple exploration of COVID-19 research papers dataset.")

# Interactive filter: year range
years = df_covid['publish_time'].dt.year.dropna().astype(int)
min_year, max_year = int(years.min()), int(years.max())
year_range = st.slider("Select publication year range", min_year, max_year, (2020, 2021))

# Filter data based on selection
filtered_df = df_covid[
    (df_covid['publish_time'].dt.year >= year_range[0]) &
    (df_covid['publish_time'].dt.year <= year_range[1])
]

st.write(f"Number of papers in selected range: {filtered_df.shape[0]}")

# --- Visualization 1: Publications over time ---
st.subheader("Number of Publications Over Time")
pub_counts = filtered_df.groupby('publish_time').size()
fig, ax = plt.subplots(figsize=(12,5))
pub_counts.plot(kind='line', ax=ax)
ax.set_xlabel("Publish Date")
ax.set_ylabel("Number of Publications")
ax.set_title("Publications Over Time")
ax.grid(True)
st.pyplot(fig)

# --- Visualization 2: Top journals ---
st.subheader("Top Publishing Journals")

# Check if the dataframe is empty
if filtered_df.empty:
    st.write("No data available.")
else:
    # Check if the 'journal' column exists and contains valid data
    if 'journal' in filtered_df.columns and filtered_df['journal'].notna().sum() > 0:
        # Generate the top 10 journals
        top_journals = filtered_df['journal'].value_counts().head(10)
        
        if top_journals.empty:
            st.write("No valid journals to display.")
        else:
            # Plot the bar chart
            fig, ax = plt.subplots(figsize=(12,5))
            top_journals.plot(kind='bar', ax=ax, color='skyblue')
            ax.set_xlabel("Journal")
            ax.set_ylabel("Number of Publications")
            ax.set_title("Top 10 Journals")
            ax.tick_params(axis='x', rotation=45)
            st.pyplot(fig)
    else:
        st.write("The 'journal' column is missing or contains invalid data.")

# --- Visualization 3: Word Cloud of Paper Titles ---
st.subheader("Word Cloud of Paper Titles")

# Check for empty or invalid data in 'title' column
if filtered_df['title'].notna().sum() == 0:
    st.write("No valid titles available to generate word cloud.")
else:
    # Clean up the titles and join them into a single string
    text = " ".join(filtered_df['title'].dropna().str.strip())

    # Check if we have any valid text to create the word cloud
    if text.strip():
        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)
        # Plot the word cloud
        fig, ax = plt.subplots(figsize=(15,7))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')  # Hide axes
        st.pyplot(fig)
    else:
        st.write("No valid text to generate the word cloud.")

# --- Display a sample of the data ---
st.subheader("Sample of Papers")
st.dataframe(filtered_df.head(10))

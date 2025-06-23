import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Netflix Bar Plot", layout="centered")
st.title("🎬 Netflix Movies vs TV Shows")

# Load data
try:
    df = pd.read_csv("netflix_titles.csv")
    st.success("✅ Data loaded successfully!")

    # Count the number of Movies vs TV Shows
    type_counts = df['type'].value_counts()

    # ✅ DEBUG PRINT (optional)
    st.write("Type Counts:")
    st.write(type_counts)

    # Plot using matplotlib (not seaborn)
    fig, ax = plt.subplots()
    ax.bar(type_counts.index, type_counts.values, color=["#FF9999", "#66B3FF"])
    ax.set_title("Content Type Distribution")
    ax.set_xlabel("Type")
    ax.set_ylabel("Count")

    # ✅ Show plot
    st.pyplot(fig)

except Exception as e:
    st.error(f"❌ Error: {e}")

# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Python Assignment Question 3 (Streamlit app)")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep='\t')

    if df.empty:
        st.info("The CSV file uploaded is empty, please enter a valid CSV file")
    else:
        st.subheader("Uploaded Data:")
        st.write(df)

        if 'age' in map(str.lower, map(str.strip, df.columns)):
            # Plot Histogram
            st.subheader("Histogram")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(data=df, x='age', bins=10,  ax=ax)
            st.pyplot(fig)

        else:
            st.info("Unable to find the 'age' column in the CSV file")

else:
    st.info("Uploaded CSV file is not valid")

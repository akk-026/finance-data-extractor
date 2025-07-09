import streamlit as st
import pandas as pd
from data_extractor import extract

# Title
st.title("Financial Data Extractor")

# Input box
paragraph = st.text_area("Enter financial paragraph:")

# Button to extract data
if st.button("Extract"):
    if paragraph:
        extracted_data = extract(paragraph)

        # Debug print to see extracted data keys and values
        st.write("Extracted data:", extracted_data)

        data = {
            'Measure': ['Revenue', 'EPS'],
            'Estimated': [
                extracted_data.get('revenue_expected', '-'),
                extracted_data.get('eps_expected', '-')
            ],
            'Actual': [
                extracted_data.get('revenue_actual', '-'),
                extracted_data.get('eps_actual', '-')
            ]
        }

        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("Please enter a paragraph to extract data from.")
# streamlit_rat_map.py
import streamlit as st
import pandas as pd


# Load data
@st.cache_data
def load_data():
    data = (pd.read_csv("1.01/10_2/tdsp-template/data/raw/rats2023.csv")
            .dropna(subset=['Latitude', 'Longitude'])
            .rename(columns={"Latitude": "LAT", "Longitude": "LON"})
            )
    data['Created Date'] = pd.to_datetime(data['Created Date'])

    return data


@st.cache_data
def months():
    return {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9
    }


data = load_data()
month_label = months()

# title
st.title("Rat Sightings in NYC")

# slider
month_selected = st.select_slider("Select month of sightings",
                                  options=month_label.keys())
data = data[data['Created Date'].dt.month == month_label[month_selected]]

vc = (data["Incident Zip"]
      .value_counts()
      .reset_index()
)
merged_df = pd.merge(data, vc, on='Incident Zip')

# streamlit map visualization
st.map(merged_df, size="count")

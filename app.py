import streamlit as st
import pandas as pd
from copy import deepcopy

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

# First some Volcano Data Exploration
df_raw = load_data(path="./data/raw/volcano_ds_pop.csv")
volcano_df = deepcopy(df_raw)


# Display basic info about the dataset
# st.write("## Dataset Overview")
# st.write(df_raw.head())  # Show first few rows
# st.write("### Summary Statistics")
# st.write(df_raw.describe())  # Show summary statistics of the data

# Add title and header
st.title("Volcanic Activity")
st.header("")

#st.table(data=volcano_df)
if st.checkbox("Show source Dataframe"):

    st.subheader("Visualize Volcano dataset:")
    st.dataframe(data=volcano_df)

#left_column, right_column = st.columns(2)
left_column, middle_column, right_column = st.columns([3, 1, 1])

countries = ["All"]+sorted(pd.unique(volcano_df['Country']))
country = left_column.selectbox("Choose a country", countries)

regions = ["All"]+sorted(pd.unique(volcano_df['Region']))
region = middle_column.selectbox("Choose a region", regions)


types = ["All"]+sorted(pd.unique(volcano_df['Type']))
type = right_column.selectbox("The type of volcano", types)


# Filter the data based on the selected country
filtered_data = volcano_df[volcano_df['Country'] == country] if country != 'All' else volcano_df
if country != 'All':
    st.write(f"### Volcanoes in {country}")
    st.write(filtered_data)

# Display the distribution of volcano types
st.write("## Distribution of Volcano Types")
volcano_type_counts = filtered_data['Type'].value_counts()
st.bar_chart(volcano_type_counts)


# Sample Streamlit Map
st.subheader("Streamlit Map")

ds_geo = filtered_data[['Volcano Name', 'Latitude', 'Longitude']]
ds_geo = ds_geo.rename(columns = {"Latitude":"LAT", "Longitude":"LON"})
#st.dataframe(ds_geo.head())

st.map(ds_geo)

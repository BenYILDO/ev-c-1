import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Şarj İstasyonları Haritası")

station_data = pd.read_csv("data/charging_stations.csv")

st.sidebar.header("Filtreler")
city_options = station_data["city"].unique()
selected_city = st.sidebar.multiselect("Şehir", city_options, default=city_options)

filtered_data = station_data[station_data["city"].isin(selected_city)]

district_options = filtered_data["district"].unique()
selected_district = st.sidebar.multiselect("İlçe", district_options, default=district_options)

filtered_data = filtered_data[filtered_data["district"].isin(selected_district)]

layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_data,
    get_position="[longitude, latitude]",
    get_radius=200,
    get_fill_color=[255, 0, 0],
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=filtered_data["latitude"].mean() if not filtered_data.empty else 39.0,
    longitude=filtered_data["longitude"].mean() if not filtered_data.empty else 35.0,
    zoom=5,
)

r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name} ({location_type})"})

st.pydeck_chart(r)

st.dataframe(filtered_data)

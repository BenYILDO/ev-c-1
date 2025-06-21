import streamlit as st
import pandas as pd

st.title("KPI Analizi")

city_kpis = pd.read_csv("data/city_kpis.csv")

st.sidebar.header("Filtreler")
selected_city = st.sidebar.selectbox("Şehir", city_kpis["city"].unique())

city_data = city_kpis[city_kpis["city"] == selected_city]

st.subheader(f"{selected_city} İçin Temel Göstergeler")

population = int(city_data["population"].iloc[0])
ev_count = int(city_data["ev_count"].iloc[0])
st.metric("Nüfus", f"{population:,}")
st.metric("EV Sayısı", f"{ev_count:,}")

station_data = pd.read_csv("data/charging_stations.csv")
stations_in_city = station_data[station_data["city"] == selected_city]

station_count = len(stations_in_city)
ratio = ev_count / station_count if station_count else 0

st.metric("İstasyon Sayısı", station_count)
st.metric("EV/İstasyon Oranı", f"{ratio:.2f}")

st.dataframe(stations_in_city)

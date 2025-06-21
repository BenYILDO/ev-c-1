import streamlit as st
import pandas as pd

st.title("Yatırım Tavsiyesi")

if "city_preference" not in st.session_state:
    st.warning("Lütfen önce ana sayfada yatırım bilgilerinizi girin.")
    st.stop()

city = st.session_state.get("city_preference")
budget = st.session_state.get("budget")
name = st.session_state.get("investor_name", "Yatırımcı")

city_kpis = pd.read_csv("data/city_kpis.csv")
city_data = city_kpis[city_kpis["city"] == city]

station_data = pd.read_csv("data/charging_stations.csv")
stations_in_city = station_data[station_data["city"] == city]

st.write(f"Merhaba {name}, {city} şehrini seçtiniz.")

station_count = len(stations_in_city)
ev_count = int(city_data["ev_count"].iloc[0])
ratio = ev_count / station_count if station_count else 0

st.metric("Şehirdeki İstasyon Sayısı", station_count)
st.metric("EV/İstasyon Oranı", f"{ratio:.2f}")

if ratio > 1000:
    st.success("İstasyon yoğunluğu düşük, yatırım için uygun olabilir.")
else:
    st.info("Şehirdeki istasyon yoğunluğu yüksek, rekabeti göz önünde bulundurun.")

st.write(f"Tahmini bütçeniz: {budget:,.0f} TL")


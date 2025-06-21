import streamlit as st
import pandas as pd

st.set_page_config(page_title="EV Charge Location Analysis", layout="wide")

st.title("Elektrikli Şarj İstasyonu Yatırım Analizi")

st.markdown(
    "Bu uygulama, Türkiye'deki elektrikli araç şarj istasyonlarının konumlarını ve yatırım potansiyelini analiz etmek için örnek veriler kullanır."
)

st.header("Yatırımcı Bilgileri")
name = st.text_input("Adınız")
budget = st.number_input("Yatırım Bütçesi (TL)", min_value=0.0, step=10000.0)
city_preference = st.selectbox(
    "Yatırım Yapmak İstediğiniz Şehir",
    ["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"],
)

if st.button("Analizi Başlat"):
    st.session_state["investor_name"] = name
    st.session_state["budget"] = budget
    st.session_state["city_preference"] = city_preference
    st.success("Veriler kaydedildi. Sol menüden diğer sayfalara geçebilirsiniz.")

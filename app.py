import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")  

st.header("🚗 Análisis de vehículos usados en EE.UU.")

if st.button("Construir histograma"):
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


if st.button("Construir gráfico de dispersión"):
    st.write("Relación entre kilometraje y precio")
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
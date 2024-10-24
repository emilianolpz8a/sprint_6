import plotly.express as px
import streamlit as st
import pandas as pd

# agregar encabezado de la aplicación
st.header("Aplicación Web de Visualización de Datos de Vehiculos")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de ventas de coches')
    # crear un histograma
    fig = px.histogram(car_data, x='odometer')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear segundo botón para gráfico de dispersión
disp_button = st.button('Construir gráfico dispersión')

if disp_button:  # al hacer clic en el botón
    # escribe mensaje
    st.write(
        'Creación de una gráfica de dispersión de los anuncios de ventas de coches')
    # crea gráfico de dispersión
    fig = px.scatter(car_data, x='odometer', y='price')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
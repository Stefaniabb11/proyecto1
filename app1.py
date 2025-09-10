import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

data = pd.read_csv('Seriesss.csv')

st.title("Pulso Económico")
st.set_page_config(
    page_title="Datos Macro | PIB, Desempleo e Inflación",
    page_icon="📈",
    layout="wide")



variables = ["PIB", "DESEMPLEO", "INFLACION"]
seleccion= st.multiselect("Selecciona las variables.",
                          options=variables,
                          default=None)
if not seleccion:
    st.warning("Por favor seleccionar al menos una variable.")
    st.stop()

# Selector de rango de años
años = sorted(data['ANIO'].dropna().unique())
rango = st.slider(
    "Selecciona rango de años",
    min_value=int(años[0]),
    max_value=int(años[-1]),
    value=(int(años[0]), int(años[-1])),
    step=1
)

# Filtrar datos
data_long = data.melt(
    id_vars=["ANIO"],
    value_vars=seleccion,
    var_name="Variable",
    value_name="Valor"
)

data_long["Valor"] = pd.to_numeric(data_long["Valor"], errors="coerce")

filtered = data_long[
    (data_long["ANIO"] >= rango[0]) &
    (data_long["ANIO"] <= rango[1])
]

# Graficar
fig = px.line(
    filtered.sort_values(['ANIO', 'Variable']),
    x="ANIO",
    y="Valor",
    color="Variable",
    markers=True,
    title="Evolución de las variables seleccionadas",
    labels={"ANIO":"Año", "Valor":"Valor", "Variable":"Variable"}
)

fig.update_layout(
    hovermode='x unified',
    template='plotly_white',
    xaxis=dict(dtick=1)
)

st.plotly_chart(fig, use_container_width=True)


    








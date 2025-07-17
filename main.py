import pandas as pd
import plotly_express as px
import streamlit as st

print("¡Las librerías están funcionando! 😄")

import pandas as pd
import streamlit as st

# Cargar el archivo CSV
df = pd.read_csv("vehicles_us.csv")

# Mostrar los primeros anuncios
st.title("🚗 Anuncios de Coches en EE.UU.")
st.write("Aquí están los primeros vehículos del dataset:")
st.dataframe(df.head())
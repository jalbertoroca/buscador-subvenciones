
import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

st.title("Buscador Automatizado de Subvenciones (BDNS)")

palabra_clave = st.text_input("Buscar por palabra clave (ej. cooperativa, formación, innovación):")

if st.button("Buscar en BDNS"):
    if palabra_clave:
        url = f"https://www.subvenciones.gob.es/bdnstrans/GE/es/convocatorias?tipoBusqueda=avanzada&textoLibre={palabra_clave}"
        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            enlaces = soup.select("a[href*='/bdnstrans/GE/es/convocatoria/']")
            resultados = []
            for e in enlaces:
                texto = e.get_text(strip=True)
                link = "https://www.subvenciones.gob.es" + e.get("href")
                resultados.append({"Título": texto, "Enlace": link})
            df = pd.DataFrame(resultados).drop_duplicates()
            st.success(f"{len(df)} resultados encontrados.")
            for i, row in df.iterrows():
                st.markdown(f"- [{row['Título']}]({row['Enlace']})")
        except Exception as e:
            st.error("Error al buscar en BDNS: " + str(e))
    else:
        st.warning("Introduce una palabra clave para buscar.")

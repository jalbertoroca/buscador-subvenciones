
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Buscador Automatizado de Subvenciones (BDNS)")

st.markdown("Introduce una palabra clave y te mostraremos convocatorias reales desde la BDNS (Base de Datos Nacional de Subvenciones).")

palabra_clave = st.text_input("Buscar por palabra clave (ej. cooperativa, innovación, empleo):")

if st.button("Buscar en BDNS"):
    if palabra_clave:
        try:
            # URL de búsqueda con palabra clave
            url = f"https://www.subvenciones.gob.es/bdnstrans/GE/es/convocatorias?tipoBusqueda=avanzada&textoLibre={palabra_clave}"
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(url, headers=headers, timeout=15)

            if r.status_code != 200:
                st.error(f"No se pudo acceder a la BDNS (código {r.status_code}). Intenta más tarde.")
            else:
                soup = BeautifulSoup(r.text, 'html.parser')
                enlaces = soup.select("a[href*='/bdnstrans/GE/es/convocatoria/']")
                resultados = []
                for e in enlaces:
                    texto = e.get_text(strip=True)
                    href = e.get("href")
                    if texto and href:
                        link = "https://www.subvenciones.gob.es" + href
                        resultados.append({"Título": texto, "Enlace": link})
                df = pd.DataFrame(resultados).drop_duplicates()

                if df.empty:
                    st.warning("No se encontraron convocatorias para esa palabra clave.")
                else:
                    st.success(f"{len(df)} resultados encontrados:")
                    for _, row in df.iterrows():
                        st.markdown(f"- [{row['Título']}]({row['Enlace']})")
        except Exception as e:
            st.error("Ocurrió un error inesperado: " + str(e))
    else:
        st.warning("Introduce una palabra clave para buscar.")

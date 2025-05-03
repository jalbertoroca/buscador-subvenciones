import streamlit as st
import requests

# Título de la aplicación
st.title("Buscador Automatizado de Subvenciones (BDNS API)")

st.markdown("""
Introduce una palabra clave y te mostraremos convocatorias reales desde la BDNS (Base de Datos Nacional de Subvenciones) usando su API REST.
""")

# Input de búsqueda
palabra_clave = st.text_input("Palabra clave (ej. cooperativa, innovación, empleo):")

# Botón de búsqueda
if st.button("Buscar en BDNS"):
    if not palabra_clave:
        st.warning("Introduce una palabra clave para buscar.")
    else:
        # Llamada a la API correcta con parámetros vigentes
        url = "https://www.infosubvenciones.es/bdnstrans/api/convocatorias/busqueda"
        params = {
            "descripcion":             palabra_clave,  # tu palabra clave
            "descripcionTipoBusqueda": 1,              # 1 = todas las palabras
            "vpd":                     "GE",           # código del portal BDNS general
            "idioma":                  "es",           # español
            "page":                    0,              # primera página (0-based)
            "pageSize":                50              # hasta 50 resultados
        }
        try:
            # Petición HTTP
            r = requests.get(url, params=params, headers={"Accept": "application/json"})
            r.raise_for_status()
            data = r.json()
            convocatorias = data.get("content", [])
            
            # Mostrar resultados
            if not convocatorias:
                st.warning("No se encontraron convocatorias para esa palabra clave.")
            else:
                st.success(f"Encontradas {len(convocatorias)} convocatorias:")
                for conv in convocatorias:
                    titulo = conv.get("tituloConvocatoria", "Sin título")
                    cid    = conv.get("idConvocatoria")
                    enlace = f"https://www.subvenciones.gob.es/bdnstrans/GE/es/convocatoria/{cid}"
                    st.markdown(f"- [{titulo}]({enlace})")
        except Exception as e:
            st.error("Error al conectar con la API: " + str(e))

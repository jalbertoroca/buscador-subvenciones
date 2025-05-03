
import streamlit as st
import requests

st.title("Buscador Automatizado de Subvenciones (BDNS API REST)")

st.markdown("Busca convocatorias reales mediante la API REST del SNPSAP (BDNS). Introduce una palabra clave y pulsa buscar.")

palabra_clave = st.text_input("Palabra clave (ej. cooperativa, innovación, empleo):")

if st.button("Buscar en BDNS"):
    if not palabra_clave:
        st.warning("Introduce una palabra clave para buscar.")
    else:
        url = "https://www.infosubvenciones.es/bdnstrans/api/convocatorias"
        params = {
            "textoLibre": palabra_clave,
            "idioma": "es",
            "pagina": 1,
            "tamanioPagina": 50
        }
        try:
            r = requests.get(url, params=params, headers={"Accept": "application/json"}, timeout=15)
            r.raise_for_status()
            data = r.json()
            convocatorias = data.get("content", [])
            if not convocatorias:
                st.warning("No se encontraron convocatorias para esa palabra clave.")
            else:
                st.success(f"Encontradas {len(convocatorias)} convocatorias:")
                for conv in convocatorias:
                    titulo = conv.get("tituloConvocatoria", "Sin título")
                    cid = conv.get("idConvocatoria")
                    enlace = f"https://www.subvenciones.gob.es/bdnstrans/GE/es/convocatoria/{cid}"
                    st.markdown(f"- [{titulo}]({enlace})")
        except Exception as e:
            st.error(f"Error al conectar con la API: {e}")

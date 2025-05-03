
import streamlit as st

st.title("Buscador Automatizado de Subvenciones")

st.markdown("Esta herramienta te permite filtrar y acceder a convocatorias de subvenciones desde distintas fuentes oficiales.")

tipo_entidad = st.selectbox("Tipo de entidad", ["Cualquiera", "Cooperativa", "SL", "Autónomo", "Asociación"])
sector = st.multiselect("Sector", ["Formación", "Innovación", "Social", "Medio ambiente", "Digitalización"])
ambito = st.selectbox("Ámbito geográfico", ["Todos", "Unión Europea", "Estatal", "Autonómico", "Local"])
cofinanciacion = st.radio("¿Requiere cofinanciación?", ["Cualquiera", "Sí", "No"])
gastos = st.multiselect("Gastos elegibles", ["Personal", "Infraestructura", "Tecnología", "Viajes", "Formación"])

if st.button("Buscar subvenciones"):
    st.success("Mostrando subvenciones filtradas (modo prototipo).")
    st.write("🔗 [Subvención 1 - Horizonte Europa](https://ec.europa.eu/info/funding-tenders/opportunities/portal/)")
    st.write("🔗 [Subvención 2 - BDNS (Innovación)](https://www.subvenciones.gob.es/)")
    st.write("🔗 [Subvención 3 - Ayudas Euskadi](https://www.euskadi.eus/ayudas-subvenciones/)")

st.markdown("---")
st.markdown("Prototipo desarrollado por ChatGPT. Fuentes: BDNS, UE, Euskadi, entre otras.")

import streamlit as st

from Funciones import *

st.title("Clasificación de suelos")

col1, col2 = st.beta_columns(2)

tamiz_3p = col1.number_input("Pasante tamiz 3'' ", min_value = 0.0, max_value = 100.0, value = 100.0, step = 0.1)
tamiz_3_4p = col1.number_input("Pasante tamiz 3/4'' ", min_value = 0.0, max_value = 100.0, value = 100.0, step = 0.1)
tamiz_4 = col1.number_input("Pasante tamiz N° 4 ", min_value = 0.0, max_value = 100.0, value = 100.0, step = 0.1)
tamiz_10 = col1.number_input("Pasante tamiz N° 10 ", min_value = 0.0, max_value = 100.0, value = 100.0, step = 0.1)
tamiz_40 = col2.number_input("Pasante tamiz N° 40 ", min_value = 0.0, max_value = 100.0, value = 100.0, step = 0.1)
tamiz_200 = col2.number_input("Pasante tamiz N° 200 ", min_value = 0.0, max_value = 100.0, value = 100.0, step = 0.1)
LL = col2.number_input("Límite líquido ", min_value = 0.0, value = 100.0, step = 0.1)
LP = col2.number_input("Límite Plástico ", min_value = 0.0, value = 100.0, step = 0.1)
suelo = [tamiz_3p, tamiz_3_4p, tamiz_4, tamiz_10, tamiz_40, tamiz_200]

clasificacion = "Complete los datos y presione calcular para clasificar el suelo"

ploteo = ploteo_curva(suelo)
if st.button('Clasificar suelo'):
	if control_logico(suelo, LL, LP) == "ok":
		clasificacion = clasificar_suelo(suelo, LL, LP)
		st.write(ploteo)
	else: 
		clasificacion = clasificar_suelo(suelo, LL, LP)

st.markdown("Clasificacion del suelo: {}".format(clasificacion), unsafe_allow_html=True)


import streamlit as st
import numpy as np

def vol_tetraedro(a,b,c,aa,bb,cc):
    M = np.array([[0, a**2, b**2, c**2, 1],
                  [a**2, 0, cc**2, bb**2, 1],
                  [b**2, cc**2, 0, aa**2, 1],
                  [c**2, bb**2, aa**2, 0, 1],
                  [1, 1, 1, 1, 0]])
    D = np.linalg.det(M)
    if D>0 :
        return np.sqrt(D/288)
    elif D==0 :
        return "El volumen es 0: quedó una figura plana."
    else :
        return "No se puede armar un tetraedro con esos valores."

st.set_page_config(page_title="Volumen de un tetraedro", layout="centered")

st.title("Volumen tetraedro")

# Inputs del usuario
a = st.number_input("Valor a", value=0.0)
b = st.number_input("Valor b", value=0.0)
c = st.number_input("Valor c", value=0.0)
d = st.number_input("Valor a' (opuesto a a)", value=0.0)
e = st.number_input("Valor b' (opuesto a b)", value=0.0)
f = st.number_input("Valor c' (opuesto a c)", value=0.0)

# Botón para calcular
if st.button("Calcular"):
    resultado = vol_tetraedro(a,b,c,d,e,f)
    st.success(f"Resultado: {resultado}")

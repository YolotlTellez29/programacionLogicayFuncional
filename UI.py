import streamlit as st

st.title("Calculadora")

num1 = st.number_input("Valor 1", step=1.0)
num2 = st.number_input("Valor 2", step=1.0)

operation = st.radio("Operación", ("Sumar", "Multiplicar"))

if st.button("Calcular"):
    if operation == "Sumar":
        result = num1 + num2
    else:
        result = num1 * num2
    st.success(f"El resultado es: {result}")

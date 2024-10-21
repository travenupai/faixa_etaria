import streamlit as st
import joblib

#Salvar o modelo knn em um arquivo
ia = joblib.load('modelo_knn.pkl')

#Título
st.title("Calcular faixa etária")

# faixa = ia.predict([[10]])

idade = st.text_input("Qual a sua idade: ")

if idade:
    try:
        idade = int(idade)
        faixa = ia.predict([[idade]])
        st.write(f"Faixa etária: {faixa[0]}")  # Imprimir a faixa)
    except ValueError:
        st.error("Por favor, digite sua idade.")

if st.button("Calcular"):
    
    faixa = ia.predict([[idade]])

    st.write(faixa)
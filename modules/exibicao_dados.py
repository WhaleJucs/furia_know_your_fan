import streamlit as st

def exibir_dados_coletados(dados):
    st.subheader("Dados Coletados:")
    st.json(dados)
    st.success("Coleta de dados bem sucedida!")
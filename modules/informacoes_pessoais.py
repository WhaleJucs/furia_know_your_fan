import streamlit as st

def coletar_informacoes_pessoais():
    st.subheader("Informações Pessoais")
    nome = st.text_input("Nome Completo", key="nome")
    endereco = st.text_area("Endereço", key="endereco")
    cpf = st.text_input("CPF", key="cpf")
    idade_opcoes = ["Menos de 18", "18-24", "25-34", "35-44", "45 anos ou mais"]
    idade = st.selectbox("Faixa de idade", idade_opcoes, key="idade")
    genero_opcoes = ["Masculino", "Feminino", "Não binário", "Outro", "Prefiro não dizer"]
    genero = st.selectbox("Gênero", genero_opcoes, key="genero")
    return nome, endereco, cpf, idade, genero
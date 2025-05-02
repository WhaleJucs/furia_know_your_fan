import streamlit as st

st.title("Know Your Fan - Coleta de Dados")

st.subheader("Informações Pessoais")
nome = st.text_input("Nome Completo")
endereco = st.text_area("Endereço")
cpf = st.text_input("CPF")

st.subheader("Interesses, Atividades, Eventos e Compras no último ano")
interesses = st.text_area("Principais interesses")
atividades = st.text_area("Principais Atividades")
eventos = st.text_area("Eventos de esports que você acompanhou ou participou no último ano")
compras = st.text_area("Compras que foram feitas no último ano")

st.subheader("Próximo Passo")
st.info("upload de documentos.")

if st.button("Enviar Dados"):
    dados = {
        "Nome": nome,
        "Endereço": endereco,
        "CPF": cpf,
        "Interesses": interesses,
        "Atividades": atividades,
        "Eventos": eventos,
        "Compras": compras
    }
    st.write("Dados Coletados:")
    st.json(dados)
    st.success("Coleta de dados bem sucedida!")
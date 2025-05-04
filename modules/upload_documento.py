import streamlit as st

def upload_documento():
    st.subheader("Upload de Documento (Opcional)")
    documento = st.file_uploader("Faça o upload de um documento (ex: RG)", key="documento_upload")
    if documento:
        st.write("Documento carregado:", documento.name)
        if st.button("Simular Validação do Documento", key="validar_documento"):
            st.success("Documento validado com sucesso (simulação)!")
    return documento
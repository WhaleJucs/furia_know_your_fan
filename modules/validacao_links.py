import streamlit as st

def validar_links_furia():
    st.subheader("Validar Links de Perfis da FURIA (Simulação)")
    link_perfil = st.text_input("Link do seu perfil no site FURIA:", key="link_furia")
    if st.button("Simular Validação do Link", key="validar_link"):
        if link_perfil:
            st.info(f"Simulando a análise do link: {link_perfil}...")
            if "furia" in link_perfil.lower() or "cstrike" in link_perfil.lower():
                st.success("Link validado! Conteúdo relevante para o perfil de um fã de FURIA.")
            else:
                st.warning("Link validado (simulação), mas o conteúdo pode não ser altamente relevante para a FURIA.")
        else:
            st.warning("Por favor, cole um link de perfil.")
    return link_perfil
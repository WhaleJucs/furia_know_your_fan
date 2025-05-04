import streamlit as st
import time
import random

def validar_links_furia():
    st.subheader("Compartilhar e Validar Links de Perfis de E-sports (Simulação de IA)")
    link_perfil = st.text_input("Cole o link do seu perfil em um site de e-sports:", key="link_esports")
    if st.button("Simular Validação do Link com IA", key="validar_link_ia"):
        if link_perfil:
            st.info(f"Simulando análise do link: {link_perfil} por IA...")
            time.sleep(2)  # Simula o tempo de análise da IA

            # Simulação da análise de relevância pela IA
            if "furia" in link_perfil.lower():
                nivel_confianca = random.uniform(0.8, 0.95)
                st.success(f"Simulação de IA: Conteúdo altamente relevante para um fã da FURIA (confiança: {nivel_confianca:.2f}).")
                st.write("- A IA identificou menções diretas à FURIA, jogadores ou eventos relacionados.")
            elif any(jogo in link_perfil.lower() for jogo in ["csgo", "valorant", "lol", "dota2"]):
                nivel_confianca = random.uniform(0.6, 0.8)
                st.warning(f"Simulação de IA: Conteúdo provavelmente relevante para um fã de e-sports (confiança: {nivel_confianca:.2f}).")
                st.write("- A IA detectou menções a jogos competitivos relevantes, mas não especificamente à FURIA.")
            elif any(termo in link_perfil.lower() for termo in ["streamer", "campeonato", "liga"]):
                nivel_confianca = random.uniform(0.4, 0.6)
                st.info(f"Simulação de IA: Conteúdo com possível relevância para e-sports (confiança: {nivel_confianca:.2f}).")
                st.write("- A IA encontrou termos relacionados a e-sports, mas a relevância específica para o perfil do usuário pode variar.")
            else:
                nivel_confianca = random.uniform(0.1, 0.3)
                st.error(f"Simulação de IA: Conteúdo com baixa probabilidade de relevância (confiança: {nivel_confianca:.2f}).")
                st.write("- A IA não encontrou termos fortemente relacionados a FURIA ou e-sports no conteúdo do link (simulação).")
        else:
            st.warning("Por favor, cole um link de perfil.")
    return link_perfil
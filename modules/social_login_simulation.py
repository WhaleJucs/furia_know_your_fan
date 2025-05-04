import streamlit as st
import time

def simulate_social_login(platform, user_id_key, permission_key, token_key, data_callback):
    if st.button(f"🔗 {platform}", key=f"{platform}_auth_start"):
        st.session_state[f"{platform}_login_simulated"] = True
        st.session_state[permission_key] = False
        st.session_state[token_key] = False

    if f"{platform}_login_simulated" in st.session_state and st.session_state[f"{platform}_login_simulated"]:
        st.info(f"Simulando: Tela de login do {platform} (usuário fictício '{st.session_state[user_id_key]}').")
        if st.button(f"Simular Permitir acesso aos dados do {platform}?", key=f"{platform}_permit_button"):
            st.session_state[permission_key] = True

    if permission_key in st.session_state and st.session_state[permission_key]:
        st.info(f"Simulando: Trocando código de autorização por token de acesso do {platform}...")
        time.sleep(1.5)
        st.success(f"Simulação: Token de acesso do {platform} obtido.")
        if data_callback:
            st.info(f"Dados coletados (simulação) do {platform}:")
            data_callback()
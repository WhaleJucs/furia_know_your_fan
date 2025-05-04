import streamlit as st
import time
import random

def _simulate_social_login(platform, user_id_key, permission_key, token_key, data_shown_key, data_callback):
    if st.button(f"🔗 {platform}", key=f"{platform}_auth_start"):
        st.session_state[f"{platform}_login_simulated"] = True
        st.session_state[permission_key] = False
        st.session_state[token_key] = False
        st.session_state[data_shown_key] = False

    if f"{platform}_login_simulated" in st.session_state and st.session_state[f"{platform}_login_simulated"]:
        st.info(f"Simulando: Tela de login do {platform} (usuário fictício '{st.session_state[user_id_key]}').")
        if st.button(f"Simular Permitir acesso aos dados do {platform}?", key=f"{platform}_permit_button"):
            st.session_state[permission_key] = True

    if permission_key in st.session_state and st.session_state[permission_key]:
        st.info(f"Simulando: Trocando código de autorização por token de acesso do {platform}...")
        time.sleep(1.5)
        st.success(f"Simulação: Token de acesso do {platform} obtido.")
        st.session_state[token_key] = True

    if token_key in st.session_state and st.session_state[token_key]:
        st.info(f"Dados coletados (simulação) do {platform}:")
        data_callback()

def vincular_redes_sociais():
    st.subheader("Vincular Redes Sociais (Simulação)")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.session_state.setdefault("twitter_user", "fã_da_furia")
        _simulate_social_login(
            "Twitter",
            "twitter_user",
            "twitter_permission_requested",
            "twitter_token_obtained",
            "twitter_data_shown",
            lambda: st.write(f"- Interações recentes com a FURIA: {random.randint(5, 20)} tweets/retweets\n- Seguindo páginas relacionadas à FURIA: {random.sample(['@furiagg', '@furiacs', '@furiapubg'], random.randint(1, 3))}")
        )

    with col2:
        st.session_state.setdefault("instagram_user", "furia_lover")
        _simulate_social_login(
            "Instagram",
            "instagram_user",
            "instagram_permission_requested",
            "instagram_token_obtained",
            "instagram_data_shown",
            lambda: st.write(f"- Seguindo páginas da FURIA: {random.sample(['@furiagg', '@furiacsgo', '@furiapontoextra'], random.randint(1, 2))}\n- Curtidas recentes em posts da FURIA: {random.randint(3, 15)}")
        )

    with col3:
        st.session_state.setdefault("twitch_user", "furia_streamer_fan")
        _simulate_social_login(
            "Twitch",
            "twitch_user",
            "twitch_permission_requested",
            "twitch_token_obtained",
            "twitch_data_shown",
            lambda: st.write(f"- Canais da FURIA seguidos: {random.sample(['furiatv', 'gaules', 'alanzoka'], random.randint(1, 2))}\n- Tempo assistido em canais da FURIA (último mês): {random.randint(1, 10)} horas (simulação)")
        )

    with col4:
        st.session_state.setdefault("tiktok_user", "furia_tiktok_fan")
        _simulate_social_login(
            "TikTok",
            "tiktok_user",
            "tiktok_permission_requested",
            "tiktok_token_obtained",
            "tiktok_data_shown",
            lambda: st.write(f"- Seguindo perfis relacionados à FURIA: {random.sample(['@furia', '@furiacsgo'], random.randint(0, 2))}\n- Interações recentes com vídeos da FURIA: {random.randint(2, 8)} likes/comentários")
        )
import streamlit as st
import random
from modules.social_login_simulation import simulate_social_login

def vincular_redes_sociais():
    st.subheader("Vincular Redes Sociais (Simulação)")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.session_state.setdefault("twitter_user", "fã_da_furia")
        simulate_social_login(
            "Twitter",
            "twitter_user",
            "twitter_permission_requested",
            "twitter_token_obtained",
            lambda: st.write(f"- Interações recentes com a FURIA: {random.randint(5, 20)} tweets/retweets\n- Seguindo páginas relacionadas à FURIA: {random.sample(['@furiagg', '@furiacs', '@furiapubg'], random.randint(1, 3))}")
        )

    with col2:
        st.session_state.setdefault("instagram_user", "furia_lover")
        simulate_social_login(
            "Instagram",
            "instagram_user",
            "instagram_permission_requested",
            "instagram_token_obtained",
            lambda: st.write(f"- Seguindo páginas da FURIA: {random.sample(['@furiagg', '@furiacsgo', '@furiapontoextra'], random.randint(1, 2))}\n- Curtidas recentes em posts da FURIA: {random.randint(3, 15)}")
        )

    with col3:
        st.session_state.setdefault("twitch_user", "furia_streamer_fan")
        simulate_social_login(
            "Twitch",
            "twitch_user",
            "twitch_permission_requested",
            "twitch_token_obtained",
            lambda: st.write(f"- Canais da FURIA seguidos: {random.sample(['furiatv', 'gaules', 'alanzoka'], random.randint(1, 2))}\n- Tempo assistido em canais da FURIA (último mês): {random.randint(1, 10)} horas (simulação)")
        )

    with col4:
        st.session_state.setdefault("tiktok_user", "furia_tiktok_fan")
        simulate_social_login(
            "TikTok",
            "tiktok_user",
            "tiktok_permission_requested",
            "tiktok_token_obtained",
            lambda: st.write(f"- Seguindo perfis relacionados à FURIA: {random.sample(['@furia', '@furiacsgo'], random.randint(0, 2))}\n- Interações recentes com vídeos da FURIA: {random.randint(2, 8)} likes/comentários")
        )
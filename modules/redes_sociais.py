import streamlit as st
import time
import random

def vincular_redes_sociais():
    st.subheader("Vincular Redes Sociais (Simulação)")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🐦 Twitter", key="twitter_auth_start"):
            st.session_state["twitter_login_simulated"] = True
            st.session_state["twitter_permission_requested"] = False
            st.session_state["twitter_token_obtained"] = False
            st.session_state["twitter_data_shown"] = False

        if "twitter_login_simulated" in st.session_state and st.session_state["twitter_login_simulated"]:
            st.info("Simulando: Tela de login do Twitter (usuário fictício 'fã_da_furia' logado).")
            if st.button("Simular Permitir acesso aos dados?", key="twitter_permit_button"):
                st.session_state["twitter_permission_requested"] = True

        if "twitter_permission_requested" in st.session_state and st.session_state["twitter_permission_requested"]:
            st.info("Simulando: Trocando código de autorização por token de acesso...")
            time.sleep(1.5)
            st.success("Simulação: Token de acesso do Twitter obtido.")
            st.session_state["twitter_token_obtained"] = True

        if "twitter_token_obtained" in st.session_state and st.session_state["twitter_token_obtained"]:
            st.info("Dados coletados (simulação):")
            st.write("- Interações recentes com a FURIA:", random.randint(5, 20), "tweets/retweets")
            st.write("- Seguindo páginas relacionadas à FURIA:", random.sample(["@furiagg", "@furiacs", "@furiapubg"], random.randint(1, 3)))

    with col2:
        if st.button("📸 Instagram", key="instagram_auth_start"):
            st.session_state["instagram_login_simulated"] = True
            st.session_state["instagram_permission_requested"] = False
            st.session_state["instagram_token_obtained"] = False
            st.session_state["instagram_data_shown"] = False

        if "instagram_login_simulated" in st.session_state and st.session_state["instagram_login_simulated"]:
            st.info("Simulando: Tela de login do Instagram (usuário fictício 'furia_lover').")
            if st.button("Simular Permitir acesso aos dados?", key="instagram_permit_button"):
                st.session_state["instagram_permission_requested"] = True

        if "instagram_permission_requested" in st.session_state and st.session_state["instagram_permission_requested"]:
            st.info("Simulando: Trocando código de autorização por token de acesso...")
            time.sleep(1.5)
            st.success("Simulação: Token de acesso do Instagram obtido.")
            st.session_state["instagram_token_obtained"] = True

        if "instagram_token_obtained" in st.session_state and st.session_state["instagram_token_obtained"]:
            st.info("Dados coletados (simulação):")
            st.write("- Seguindo páginas da FURIA:", random.sample(["@furiagg", "@furiacsgo", "@furiapontoextra"], random.randint(1, 2)))
            st.write("- Curtidas recentes em posts da FURIA:", random.randint(3, 15))

    # Repita a lógica para Twitch e TikTok de forma similar, ajustando as keys e os textos.
    # ... (código para Twitch e TikTok)

    with col3:
        if st.button("🟣 Twitch", key="twitch_auth_start"):
            st.session_state["twitch_login_simulated"] = True
            st.session_state["twitch_permission_requested"] = False
            st.session_state["twitch_token_obtained"] = False
            st.session_state["twitch_data_shown"] = False

        if "twitch_login_simulated" in st.session_state and st.session_state["twitch_login_simulated"]:
            st.info("Simulando: Tela de login do Twitch (usuário fictício 'furia_streamer_fan').")
            if st.button("Simular Permitir acesso aos dados?", key="twitch_permit_button"):
                st.session_state["twitch_permission_requested"] = True

        if "twitch_permission_requested" in st.session_state and st.session_state["twitch_permission_requested"]:
            st.info("Simulando: Trocando código de autorização por token de acesso...")
            time.sleep(1.5)
            st.success("Simulação: Token de acesso do Twitch obtido.")
            st.session_state["twitch_token_obtained"] = True

        if "twitch_token_obtained" in st.session_state and st.session_state["twitch_token_obtained"]:
            st.info("Dados coletados (simulação):")
            st.write("- Canais da FURIA seguidos:", random.sample(["furiatv", "gaules", "alanzoka"], random.randint(1, 2)))
            st.write("- Tempo assistido em canais da FURIA (último mês):", random.randint(1, 10), "horas (simulação)")

    with col4:
        if st.button("🎶 Tiktok", key="tiktok_auth_start"):
            st.session_state["tiktok_login_simulated"] = True
            st.session_state["tiktok_permission_requested"] = False
            st.session_state["tiktok_token_obtained"] = False
            st.session_state["tiktok_data_shown"] = False

        if "tiktok_login_simulated" in st.session_state and st.session_state["tiktok_login_simulated"]:
            st.info("Simulando: Tela de login do TikTok (usuário fictício 'furia_tiktok_fan').")
            if st.button("Simular Permitir acesso aos dados?", key="tiktok_permit_button"):
                st.session_state["tiktok_permission_requested"] = True

        if "tiktok_permission_requested" in st.session_state and st.session_state["tiktok_permission_requested"]:
            st.info("Simulando: Trocando código de autorização por token de acesso...")
            time.sleep(1.5)
            st.success("Simulação: Token de acesso do TikTok obtido.")
            st.session_state["tiktok_token_obtained"] = True

        if "tiktok_token_obtained" in st.session_state and st.session_state["tiktok_token_obtained"]:
            st.info("Dados coletados (simulação):")
            st.write("- Seguindo perfis relacionados à FURIA:", random.sample(["@furia", "@furiacsgo"], random.randint(0, 2)))
            st.write("- Interações recentes com vídeos da FURIA:", random.randint(2, 8), "likes/comentários")
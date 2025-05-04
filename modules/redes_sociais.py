import streamlit as st

def vincular_redes_sociais():
    st.subheader("Vincular Redes Sociais (Simulação)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🐦 Twitter", key="twitter"):
            st.info("Simulando pedido de permissão para acessar dados do Twitter...")
            st.write("Permissão concedida (simulação). Lendo dados...")
            st.write("- Interações recentes com a FURIA: [Simulado]")
    with col2:
        if st.button("📸 Instagram", key="instagram"):
            st.info("Simulando pedido de permissão para acessar dados do Instagram...")
            st.write("Permissão concedida (simulação). Lendo dados...")
            st.write("- Páginas da FURIA seguidas: [Simulado]")
    with col3:
        if st.button("🟣 Twitch", key="twitch"):
            st.info("Simulando pedido de permissão para acessar dados do Twitch...")
            st.write("Permissão concedida (simulação). Lendo dados...")
            st.write("- Canais da FURIA seguidos: [Simulado]")
    with col4:
        if st.button("🎶 Tiktok", key="tiktok"):
            st.info("Simulando pedido de permissão para acessar dados do TikTok...")
            st.write("Permissão concedida (simulação). Lendo dados...")
            st.write("- Canais da FURIA seguidos: [Simulado]")
import streamlit as st

def coletar_interesses_atividades():
    st.subheader("Interesses, Atividades, Eventos e Compras no último ano")
    jogos_competitivos_opcoes = ["Counter-Strike", "League of Legends", "VALORANT", "Dota 2", "Rainbow Six Siege", "Rocket League", "Kings League", "Outros"]
    interesses = st.multiselect("Quais jogos do cenário competitivo você costuma acompanhar?", jogos_competitivos_opcoes, key="interesses")
    atividades = st.multiselect("Quais jogos você costuma jogar?", jogos_competitivos_opcoes, key="atividades")
    streamers = st.text_area("Quais streamers você acompanha?", key="streamers")
    eventos_opcoes = ["Sim, participei", "Sim, apenas assisti online", "Sim, participei e assisti online", "Não"]
    eventos = st.radio("Você acompanhou ou participou de eventos de esports no último ano?", eventos_opcoes, key="eventos")
    compras_opcoes = ["Sim, roupas e acessorios", "Sim, skins/bundle virtuais", "Sim, outros", "Não"]
    compras = st.multiselect("Você fez alguma compra relacionada a esports no ultimo ano?", compras_opcoes, key="compras")
    return interesses, atividades, streamers, eventos, compras
import streamlit as st

st.title("Know Your Fan - Coleta de Dados")

st.subheader("Informações Pessoais")
nome = st.text_input("Nome Completo")
endereco = st.text_area("Endereço")
cpf = st.text_input("CPF")
faixa_idade_opcoes = ["Menos de 18", "18-24", "25-34", "35-44", "45 anos ou mais"]
idade = st.selectbox("Faixa de idade", faixa_idade_opcoes)
genero_opcoes = ["Masculino", "Feminino", "Não binário", "Outro", "Prefiro não dizer"]
genero = st.selectbox("Gênero", genero_opcoes)

st.subheader("Interesses, Atividades, Eventos e Compras no último ano")
jogos_competitivos_opcoes = ["Counter-Strike", "League of Legends", "VALORANT", "Dota 2", "Rainbow Six Siege", "Rocket League", "Kings League", "Outros"]
interesses = st.multiselect("Quais jogos do cenário competitivo você costuma acompanhar?", jogos_competitivos_opcoes)
jogos_jogar_opcoes = ["Counter-Strike", "League of Legends", "VALORANT", "Dota 2", "Rainbow Six Siege", "Rocket League", "Kings League", "Outros"]
atividades = st.multiselect("Quais jogos você costuma jogar?", jogos_jogar_opcoes)
streamers = st.text_area("Quais streamers você acompanha?")
eventos_opcoes = ["Sim, participei", "Sim, apenas assisti online", "Sim, participei e assisti online", "Não"]
eventos = st.radio("Você acompanhou ou participou de eventos de esports no último ano?", eventos_opcoes)
compras_opcoes = ["Sim, roupas e acessorios", "Sim, skins/bundle virtuais", "Sim, outros", "Não"]
compras = st.multiselect("Você fez alguma compra relacionada a esports no ultimo ano?", compras_opcoes)

st.subheader("Upload de Documento (Opcional)")
documento = st.file_uploader("Faça o upload de um documento (ex: RG)")
if documento is not None:
    st.write("Documento carregado:", documento.name)
    if st.button("Simular Validação do Documento"):
        # Lógica de validação IA para o documento,
        # como verificar o tipo do arquivo (se permitido) ou exibir mensagens diferentes.
        st.success("Documento validado com sucesso (simulação)!")

st.subheader("Vincular Redes Sociais (Simulação)")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🐦 Twitter"):
        st.info("Simulando pedido de permissão para acessar dados do Twitter...")
        st.write("Permissão concedida (simulação). Lendo dados...")
        st.write("- Interações recentes com a FURIA: [Simulado]")
        # Adicione aqui mais informações simuladas do Twitter
with col2:
    if st.button("📸 Instagram"):
        st.info("Simulando pedido de permissão para acessar dados do Instagram...")
        st.write("Permissão concedida (simulação). Lendo dados...")
        st.write("- Páginas da FURIA seguidas: [Simulado]")
        # Adicione aqui mais informações simuladas do Instagram
with col3:
    if st.button("🟣 Twitch"):
        st.info("Simulando pedido de permissão para acessar dados do Twitch...")
        st.write("Permissão concedida (simulação). Lendo dados...")
        st.write("- Canais da FURIA seguidos: [Simulado]")
        # Adicione aqui mais informações simuladas do Twitch
with col4:
    if st.button("🎶 Tiktok"):
        st.info("Simulando pedido de permissão para acessar dados do TikTok...")
        st.write("Permissão concedida (simulação). Lendo dados...")
        st.write("- Canais da FURIA seguidos: [Simulado]")
        # Adicione aqui mais informações simuladas do TikTok

st.subheader("Validar Links de Perfis da FURIA (Simulação)")
link_perfil = st.text_input("Link do seu perfil no site FURIA:")
if st.button("Simular Validação do Link"):
    if link_perfil:
        st.info(f"Simulando a análise do link: {link_perfil}...")
        # Lógica de simulação para verificar
        # se o link parece ser de um site da furia e se o
        # conteúdo simulado é relevante para o perfil de um fã.
        if "furia" in link_perfil.lower() or "cstrike" in link_perfil.lower():
            st.success("Link validado! Conteúdo relevante para o perfil de um fã de FURIA.")
        else:
            st.warning("Link validado (simulação), mas o conteúdo pode não ser altamente relevante para a FURIA.")
    else:
        st.warning("Por favor, cole um link de perfil.")

if st.button("Enviar Dados"):
    dados = {
        "Nome": nome,
        "Endereço": endereco,
        "CPF": cpf,
        "Faixa de idade": idade,
        "Gênero": genero,
        "Interesses": interesses,
        "Atividades": atividades,
        "Streamers": streamers,
        "Eventos": eventos,
        "Compras": compras
    }
    st.write("Dados Coletados:")
    st.json(dados)
    st.success("Coleta de dados bem sucedida!")
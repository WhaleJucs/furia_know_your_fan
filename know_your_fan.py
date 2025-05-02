import streamlit as st

st.title("Know Your Fan - Coleta de Dados")

st.subheader("Informações Pessoais")
nome = st.text_input("Nome Completo")
endereco = st.text_area("Endereço")
cpf = st.text_input("CPF")

st.subheader("Interesses, Atividades, Eventos e Compras no último ano")
interesses = st.text_area("Principais interesses")
atividades = st.text_area("Principais Atividades")
eventos = st.text_area("Eventos de esports que você acompanhou ou participou no último ano")
compras = st.text_area("Compras que foram feitas no último ano")

st.subheader("Upload de Documento (Opcional)")
documento = st.file_uploader("Faça o upload de um documento (ex: RG)")
if documento is not None:
    st.write("Documento carregado:", documento.name)
    if st.button("Simular Validação do Documento"):
        # Lógica de validação IA para o documento,
        # como verificar o tipo do arquivo (se permitido) ou exibir mensagens diferentes.
        st.success("Documento validado com sucesso (simulação)!")

st.subheader("Vincular Redes Sociais (Simulação)")
col1, col2, col3 = st.columns(3)
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
        "Interesses": interesses,
        "Atividades": atividades,
        "Eventos": eventos,
        "Compras": compras
    }
    st.write("Dados Coletados:")
    st.json(dados)
    st.success("Coleta de dados bem sucedida!")
import streamlit as st
import re

def coletar_informacoes_pessoais():
    st.subheader("Informações Pessoais")
    nome = st.text_input("Nome Completo", key="nome")
    endereco = st.text_area("Endereço", key="endereco")
    cpf = st.text_input("CPF", key="cpf")
    idade_opcoes = ["Menos de 18", "18-24", "25-34", "35-44", "45 anos ou mais"]
    idade = st.selectbox("Faixa de idade", idade_opcoes, key="idade")
    genero_opcoes = ["Masculino", "Feminino", "Não binário", "Outro", "Prefiro não dizer"]
    genero = st.selectbox("Gênero", genero_opcoes, key="genero")
    return nome, endereco, cpf, idade, genero

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

def upload_documento():
    st.subheader("Upload de Documento (Opcional)")
    documento = st.file_uploader("Faça o upload de um documento (ex: RG)", key="documento_upload")
    if documento:
        st.write("Documento carregado:", documento.name)
        if st.button("Simular Validação do Documento", key="validar_documento"):
            st.success("Documento validado com sucesso (simulação)!")
    return documento

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

def validar_dados(nome, endereco, cpf):
    erros = []
    if not nome:
        erros.append("O nome é obrigatório.")
    if not endereco:
        erros.append("O endereço é obrigatório.")
    if not cpf:
        erros.append("O CPF é obrigatório.")
    elif not re.match(r'^\d{11}$', cpf):
        erros.append("O CPF deve conter 11 dígitos numéricos.")
    return erros

def exibir_dados_coletados(dados):
    st.subheader("Dados Coletados:")
    st.json(dados)
    st.success("Coleta de dados bem sucedida!")

def main():
    st.title("Know Your Fan - Coleta de Dados")

    nome, endereco, cpf, idade, genero = coletar_informacoes_pessoais()
    interesses, atividades, streamers, eventos, compras = coletar_interesses_atividades()
    upload_documento()
    vincular_redes_sociais()
    validar_links_furia()

    if st.button("Enviar Dados"):
        erros = validar_dados(nome, endereco, cpf)
        if erros:
            for erro in erros:
                st.error(erro)
        else:
            dados = {
                "Nome": nome,
                "Endereço": endereco,
                "CPF": cpf,
                "Faixa de idade": idade,
                "Gênero": genero,
                "Interesses": interesses,
                "Atividades": atividades,
                "Streamers": st.session_state.get("streamers", ""),
                "Eventos": eventos,
                "Compras": compras
            }
            exibir_dados_coletados(dados)

if __name__ == "__main__":
    main()
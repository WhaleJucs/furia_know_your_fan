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
redes_sociais = ["Twitter", "Instagram", "Twitch"]
rede_selecionada = st.selectbox("Selecione a rede social para vincular:", redes_sociais)
if st.button(f"Simular Leitura de Dados do {rede_selecionada}"):
    st.info(f"Simulando a leitura de interações, páginas seguidas e atividades relacionadas a esports da sua conta de {rede_selecionada}...")
    # Aqui você poderia adicionar informações simuladas diferentes dependendo da rede selecionada.
    st.write("Informações simuladas:")
    st.write(f"- Número de interações recentes relacionadas à FURIA: [Número Aleatório]")
    st.write(f"- Páginas de esports seguidas: [Lista de Páginas Simuladas]")
    st.write(f"- Atividades recentes relacionadas à FURIA: [Descrição de Atividades Simuladas]")

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
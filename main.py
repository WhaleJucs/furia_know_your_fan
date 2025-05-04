import streamlit as st
from modules.informacoes_pessoais import coletar_informacoes_pessoais
from modules.interesses_atividades import coletar_interesses_atividades
from modules.upload_documento import upload_documento
from modules.redes_sociais import vincular_redes_sociais
from modules.validacao_links import validar_links_furia
from modules.validacao_dados import validar_dados
from modules.exibicao_dados import exibir_dados_coletados

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
                "Streamers": streamers,
                "Eventos": eventos,
                "Compras": compras
            }
            exibir_dados_coletados(dados)

if __name__ == "__main__":
    main()
# Know Your Fan - Plataforma de Coleta de Dados para Fãs de Esports (Challenge #2 - HARD)

## Breve Descrição

Este projeto consiste em um **aplicativo web interativo construído com Streamlit**, uma biblioteca Python de código aberto que facilita a criação rápida de interfaces web personalizadas para aprendizado de máquina e ciência de dados. 
O aplicativo foi desenvolvido para coletar informações abrangentes sobre fãs de e-sports, com foco em entusiastas da FURIA. O objetivo é simular uma solução que permitiria à organização conhecer melhor seus fãs, possibilitando a oferta de experiências e serviços exclusivos no futuro.

## Funcionalidades Principais

Este protótipo navegável implementa as seguintes funcionalidades (com algumas simulações devido às limitações de tempo e escopo):

* **Coleta de Dados Pessoais:** Permite aos usuários inserir informações básicas como nome completo, endereço, CPF, faixa de idade e gênero.
* **Registro de Interesses e Atividades:** Coleta dados sobre os jogos competitivos que o usuário acompanha e joga, os streamers que assiste, o envolvimento em eventos de esports no último ano e compras relacionadas ao cenário.
* **Upload de Documento (Simulado):** Oferece a funcionalidade de upload de um documento (com simulação de análise de identificação por IA para imagens, com detecção do tipo de arquivo e um slider para simular a confiança da validação). 
A integração de uma análise de identificação por IA em tempo real exigiria a utilização de serviços externos de aprendizado de máquina e o desenvolvimento de um pipeline de processamento complexo, o que demandaria um tempo de desenvolvimento significativamente maior. Dada a natureza deste desafio e as restrições de tempo, optou-se por simular a funcionalidade para demonstrar o conceito.
* **Vinculação de Redes Sociais (Simulação):** Simula a vinculação de contas do Twitter, Instagram, Twitch e TikTok, exibindo dados fictícios sobre interações recentes e páginas seguidas relacionadas à FURIA. A implementação real da vinculação de redes sociais envolveria a utilização das APIs específicas de cada plataforma. Isso exigiria a criação de aplicações de desenvolvedor em cada rede social, o gerenciamento de processos de autenticação OAuth 2.0 (que envolvem redirecionamentos e consentimento do usuário), e o tratamento das políticas de privacidade e termos de serviço de cada plataforma. Além disso, a leitura e interpretação dos dados das APIs para extrair informações relevantes sobre a interação com a FURIA demandaria um esforço de desenvolvimento considerável, optando-se por uma simulação para ilustrar a potencialidade da funcionalidade.
* **Validação de Links de Perfis de E-sports (Simulação de IA):** Permite ao usuário inserir um link de um perfil em um site de esports e simula uma análise por IA para determinar a relevância do conteúdo para um fã da FURIA, com base em palavras-chave e um nível de confiança simulado. Uma análise real por IA envolveria processamento de linguagem natural mais sofisticado.
* **Exibição dos Dados Coletados:** Apresenta um resumo dos dados inseridos pelo usuário após o envio do formulário.

## Como Executar Localmente (Instruções)

Para executar este aplicativo localmente, siga os seguintes passos:

1.  **Certifique-se de ter Python instalado** (versão 3.7 ou superior é recomendada). Você pode verificar sua versão com o comando `python --version` ou `python3 --version`.
2.  **Clone este repositório do GitHub:**
    ```bash
    git clone [https://github.com/WhaleJucs/furia_know_your_fan.git](https://github.com/WhaleJucs/furia_know_your_fan.git)
    cd furia_know_your_fan
    ```
3.  **(Recomendado) Crie um ambiente virtual:**
    * **No Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * **No macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
4.  **Instale as dependências:** Embora este projeto possa não ter dependências externas significativas além do Streamlit, é uma boa prática criar um arquivo `requirements.txt` se você adicionar mais bibliotecas no futuro. Para executar o Streamlit, instale-o se ainda não o tiver:
    ```bash
    pip install streamlit
    ```
5.  **Execute o aplicativo:**
    ```bash
    streamlit run main.py
    ```

    Isso abrirá o aplicativo no seu navegador web.

## Explicação da estrutura do Código

O projeto "Know Your Fan" possui a seguinte estrutura de arquivos e pastas:
furia_know_your_fan/
├── main.py             # Arquivo principal que roda o aplicativo Streamlit
└── modules/            # Pasta contendo os módulos com as funcionalidades do aplicativo
    ├── exibicao_dados.py       # Módulo para exibir os dados coletados
    ├── informacoes_pessoais.py # Módulo para coletar informações pessoais
    ├── interesses_atividades.py # Módulo para coletar interesses e atividades de esports
    ├── redes_sociais.py       # Módulo para simular a vinculação de redes sociais
    ├── social_login_simulation.py # Módulo com a função genérica para simular login social
    ├── upload_documento.py    # Módulo para simular o upload de documentos
    ├── validacao_dados.py      # Módulo para validar os dados básicos inseridos
    └── validacao_links.py      # Módulo para simular a validação de links de esports

* **`main.py`**: Este é o arquivo principal do aplicativo Streamlit. Ele importa as funções de cada módulo dentro da pasta `modules` e define o fluxo principal do aplicativo, incluindo a coleta de dados, a validação e a exibição. Ao executar `streamlit run main.py`, este script é o ponto de entrada.

* **`modules/`**: Esta pasta contém os módulos Python que encapsulam a lógica de cada seção do aplicativo. Essa organização modular ajuda a manter o código limpo, reutilizável e fácil de entender.

    * **`exibicao_dados.py`**: Responsável por conter a função que formata e exibe os dados coletados do usuário na interface do Streamlit.
    * **`informacoes_pessoais.py`**: Contém a função que cria os campos de entrada para coletar informações pessoais básicas do usuário (nome, endereço, CPF, etc.).
    * **`interesses_atividades.py`**: Inclui a função para coletar dados sobre os interesses do usuário em jogos de esports, suas atividades de jogo, os streamers que acompanha, seu envolvimento em eventos e compras relacionadas.
    * **`redes_sociais.py`**: Contém a lógica para simular a vinculação de diferentes plataformas de redes sociais e exibir informações fictícias sobre a interação do usuário com a FURIA nessas plataformas.
    * **`social_login_simulation.py`**: Fornece uma função reutilizável para simular o processo de login em uma plataforma social, usada pelo módulo `redes_sociais.py`.
    * **`upload_documento.py`**: Implementa a funcionalidade de upload de um documento e simula uma análise básica do tipo de arquivo e uma avaliação de confiança da "validação" por IA.
    * **`validacao_dados.py`**: Contém a função para realizar uma validação simples dos dados de entrada do usuário, como garantir que campos obrigatórios não estejam vazios e que o CPF tenha o formato correto.
    * **`validacao_links.py`**: Implementa a simulação da validação de links de perfis de esports, analisando o conteúdo do link (através de palavras-chave) para determinar sua relevância para um fã da FURIA.

Essa estrutura modular facilita a manutenção do código e a adição de novas funcionalidades no futuro.

## Link do Aplicativo Hospedado (Streamlit Community Cloud)

[(https://furiaknowyourfan-d9wriq8pcpecthcweqb2lt.streamlit.app/)]